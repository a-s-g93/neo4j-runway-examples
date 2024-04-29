import os
from typing import List, Dict, Tuple, Union
from enum import Enum

from openai import OpenAI
# import openai
import instructor

# import pandas as pd
from objects.data_model import DataModel
from resources.prompts.prompts import system_prompts
from resources.prompts.prompts import model_generation_rules

# MODEL = "gpt-3.5-turbo"
# MODEL = "gpt-4"

model_options = [
    'gpt-4', 
    'gpt-3.5-turbo',
    'gpt-4-0125-preview',
    'gpt-4-turbo-preview',
    'gpt-4-1106-preview',
    'gpt-4-0613',
    'gpt-4-32k',
    'gpt-4-32k-0613',
    'gpt-3.5-turbo-1106',
    'gpt-3.5-turbo-0125'
    ]

class LLM():
    """
    Interface for interacting with different LLMs.
    """
    
    def __init__(self, model: str = "gpt-4", open_ai_key: Union[str, None] = None) -> None:

        if model not in model_options:
            raise ValueError("model must be one of the following: ", model_options)
        self.llm_instance = instructor.patch(OpenAI(api_key=open_ai_key if open_ai_key is not None else os.environ.get("OPENAI_API_KEY")))
        self.model = model

    def get_discovery_response(self, formatted_prompt: str) -> DataModel:
        """
        Get a discovery response from the LLM.
        """

        response = self.llm_instance.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[
                {"role": "system", "content": system_prompts['discovery']},
                {"role": "user", "content": formatted_prompt}
            ]
        )
        return response.choices[0].message.content
        
    def get_data_model_response(self, formatted_prompt: str, csv_columns: List[str], max_retries: int = 3) -> DataModel:
        """
        Get a data model response from the LLM.
        """

        retries = 0
        valid_response = False
        while retries < max_retries and not valid_response:

            retries+=1 # increment retries each pass

            response = self.llm_instance.chat.completions.create(
                model=self.model,
                temperature=0,
                response_model=DataModel,
                messages=[
                    {"role": "system", "content": system_prompts['data_model']},
                    {"role": "user", "content": formatted_prompt}
                ],
            )

            validation = response.validate_model(csv_columns=csv_columns)
            if not validation['valid']:
                print("validation failed")
                cot = self.get_chain_of_thought_response(formatted_prompt=validation['message'])
                # formatted_prompt = validation['message']
                formatted_prompt = self._generate_retry_prompt(chain_of_thought_response=cot, 
                                                               errors_to_fix=validation["errors"],
                                                               model_to_fix=response)
                print("retry prompt: ", formatted_prompt)
            elif validation['valid']:
                print("recieved a valid response")
                valid_response = True
            
        return response

    def get_chain_of_thought_response(self, formatted_prompt: str) -> str:
        """
        Generate fixes for the previous data model.
        """
        print("performing chain of thought process...")
        response = self.llm_instance.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[
                {"role": "system", "content": system_prompts['retry']},
                {"role": "user", "content": formatted_prompt}
            ]
        )
        return response.choices[0].message.content
    
    def _generate_retry_prompt(self, chain_of_thought_response: str, errors_to_fix: str, model_to_fix: DataModel) -> str:
        """
        Generate a prompt to fix the data model using the errors found in previous model
        and the chain of thought response containing ideas on how to fix the errors.
        """

        return f"""
                Fix these errors in the data model by following the recommendations below and following the rules.
                Do not return the same model!
                {chain_of_thought_response}

                Errors:
                {errors_to_fix}

                Data Model:
                {model_to_fix}

                Rules that must be followed:
                {model_generation_rules}
                """