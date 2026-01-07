from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from com.learnings.agent.tools.agent_tools import launch_browser, close_browser, click_element, enter_text_value, \
    get_page_source
from langchain.agents import create_agent

# print(dir(agents))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

model = ChatOllama(model="llama3.2")


def get_normal_template():
    return """
    
    you are news expert in answering the questions about current recents
    
    here are some relant news: {news}
    
    here is the question to answers : {question}
    
    """


def get_query(input_value="How many students are studying in the goldern gate school?"):
    return input_value


# 2. Prepare the Input Dictionary
# The key names must match the placeholders used in your ChatPromptTemplate:
# - 'input': Required, contains the user's query.
# - 'chat_history': Required by the prompt, even if empty for the first turn.
input_data = {
    "input": get_query(),
    "chat_history": []
}

prompt = ChatPromptTemplate.from_template(get_normal_template())
chain = prompt | model


def check_weather(location: str) -> str:
    '''Return the weather forecast for the specified location.'''
    return f"It's always sunny in {location}"


new_tools = [launch_browser, close_browser, click_element, enter_text_value, get_page_source]
graph = create_agent(
    model=model,
    tools=new_tools,
    system_prompt="You are a helpful assistant",
)

inputs = {"messages": [{"role": "user",
                        "content": "Open browser and go to https://demoqa.com/automation-practice-form and verify header has Practice Form value or not then close browser"}]}
"""
res = graph.invoke(inputs)
print(res)
"""

while (True):

    in_value = input("Enter the question or q to exit \n=>")
    if in_value == 'q':
        break
    # news = vector_retrivers.invoke(in_value)
    # result = chain.invoke({"news":[news],"question":in_value})
    #inputs = {"messages": [{"role": "user",
     #                       "content": f'{in_value}'}]}

    for chunk in graph.stream(inputs, stream_mode="updates"):

        try:
            print(f"Model: {chunk['model']['messages'][0].content}")
        except:
            print(f"Tools : {chunk['tools']['messages'][0].content}")
