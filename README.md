# Neo4j Runway Examples
Neo4j Runway is a Python library that simplifies the process of migrating your relational data into a graph. It provides tools that abstract communication with OpenAI to run discovery on your data and generate a data model, as well as tools to generate ingestion code and load your data into a Neo4j instance.
The examples here will demonstrate these capabilities.

## Key Features

- **Data Discovery**: Harness OpenAI LLMs to provide valuable insights from your data
- **Graph Data Modeling**: Utilize OpenAI and the [Instructor](https://github.com/jxnl/instructor) Python library to create valid graph data models
- **Code Generation**: Generate ingestion code for your preferred method of loading data
- **Data Ingestion**: Load your data using Runway's built in implementation of [PyIngest](https://github.com/neo4j-field/pyingest) - Neo4j's popular ingestion tool

## Requirements
Runway uses graphviz to visualize data models. To enjoy this feature please download [graphviz](https://www.graphviz.org/download/).

You'll need a Neo4j instance to fully utilize Runway. Start up a free cloud hosted [Aura](https://console.neo4j.io) instance or download the [Neo4j Desktop app](https://neo4j.com/download/).

It's recommended to run these examples in a virtual environment. To install run the following from the command line in the project root directory. 

```
pip install -r requirements.txt
```

## Demos

### Country Data Walkthrough

Walkthrough each of the 4 key features with country data. This will cover discovery and data modeling with an LLM, ingestion code generation and ingestion into a Neo4j graph.

### arrows.app Integration

Learn how to create a model in [arrows.app](https://arrows.app/), then import it into Neo4j Runway to generate code and ingest into a graph.

### Streamlit Application

This is an Streamlit implementation of Neo4j Runway that guides the user through each key feature using their own data. 


