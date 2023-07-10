'''
    Loading the LLM model..
    
'''
## Importing modules
### Models
# from langchain import OpenAI
from langchain.llms import OpenAI

## importing agents
from langchain.agents import AgentType
from langchain.agents import initialize_agent

## importing tools
from langchain.agents import Tool
from langchain.agents import load_tools

## imporing the memory
from langchain.memory import ConversationBufferMemory

## importing some utilities
# from langchain.utilities import SerpAPIWrapper
from langchain.tools import BraveSearch
import os


### defining the keys
key =  os.environ["OPENAI_KEY"]
brave_key = os.environ["BRAVE_KEY"]


## loading the model
llm = OpenAI(temperature=0, openai_api_key=key)

## defining tool
search = BraveSearch.from_api_key(api_key=brave_key) ## integrating the bravesearch
tools = [
    Tool(
        name = "Current Search",
        func = search.run,
        description = "useful for when you need to answer questions about technology only"
    )
]

## Initializing the memory
memory = ConversationBufferMemory(memory_key="chat_history")

## Initializing the agents
agent_kwargs = {'prefix':f'You are friendly  tech-bot. you need to answer question about technology only.'}


# initialize the LLM agent
agent = initialize_agent(tools, 
                         llm, 
                         agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, 
                         verbose=False, 
                         memory=memory,
                         agent_kwargs=agent_kwargs
                         )


def get_response(input_):
    response = agent.run(input_)
    return response


