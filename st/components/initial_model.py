import os

import streamlit as st

from neo4j_runway import GraphDataModeler, LLM

def initial_model(show: bool = True) -> None:
    """
    Display the intial data model JSON and visual.
    """
    with st.status("Data Model V1", expanded=show):

        # only run the first time!
        if st.session_state["initial_model_created"] == False:
            st.session_state["modeler"] = GraphDataModeler(llm=LLM(
                            model=st.session_state["model_name"], open_ai_key=os.getenv("OPENAI_API_KEY")
                        ), discovery=st.session_state["discovery"])
            st.session_state["modeler"].create_initial_model()
            # we iterate once to refine the first displayed model
            st.session_state["modeler"].iterate_model(iterations=1)
            st.session_state["initial_model_created"] = True

        st.json(st.session_state["modeler"].model_history[1].model_dump(), expanded=False)
        st.graphviz_chart(
            st.session_state["modeler"].model_history[1].visualize(),
            use_container_width=True,
        )
