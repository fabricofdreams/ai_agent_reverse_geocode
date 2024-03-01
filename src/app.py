# Requirements: streamlit python-dotenv googlemaps langchain langchain_openai global-land-mask
from dotenv import load_dotenv
from ai_config import template, human_template, information
from tools import reverse_geocode_agent
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage


load_dotenv()

# Set up
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = [reverse_geocode_agent]

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
    MessagesPlaceholder(variable_name="site_name", optional=True),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_openai_functions_agent(llm, tools, chat_prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# Set up page
st.set_page_config(page_title="Where is it?", page_icon="🗺️")
st.title("Where is it?")
st.info(information)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User query
user_query = st.chat_input("What are the coordinates of the site?")

# Conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)

if user_query is not None and user_query != "":
    try:
        latitude, longitude = user_query.split(",")
    except:
        st.error(
            "I'm sorry, this application only recieves pair of numbers. Please, provide the coordinates in the following format: 40.4168,-3.7038")
        st.stop()

    text_template = "Give me the site and country names for this latitude and latitude respectly: {} and {}.".format(
        latitude, longitude)
    st.session_state.chat_history.append(HumanMessage(text_template))

    with st.chat_message("Human"):
        st.write(text_template)

    # Run agent
    with st.chat_message("AI"):
        output = agent_executor.invoke(
            {"latitude": latitude, "longitude": longitude})
        ai_response = output['output']
        st.write(ai_response)

    st.session_state.chat_history.append(AIMessage(output['output']))
