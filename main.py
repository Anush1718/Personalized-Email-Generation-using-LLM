import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect
    
    Below is email, tone, dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR RESPONSE:
"""

prompt = PromptTemplate(
   input_variables=["tone", "dialect", "email"],
   template=template,
)


def load_LLM():
   llm = OpenAI(temperature=0.9, openai_api_key=" YOUR API KEY")
   #llm = OpenAI(temperature=0.9)
   return llm

llm = load_LLM()
st.set_page_config(page_title="Vaanga palagalam", page_icon=":robot:")
st.header("Vaanga palagalam")

col1, col2 = st.columns(2)

with col1:
    st.markdown("nalla email venumaa")


st.markdown("## Epdi iruntha text")   

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'entha tone la venum?',
        ('Formal', 'Informal'))
    
with col2:
    option_dialect = st.selectbox(
        'Which English dialect?',
        ('American English', 'British English'))
    
    

def get_text():
    input_text = st.text_area(label="", placeholder="Unga email....", key="email_input")
    return input_text

email_input = get_text()

st.markdown("### Ipdi ayiduchu:")

if email_input:
    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)

    formatted_email = llm(prompt_with_email)
    st.write(formatted_email)