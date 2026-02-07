from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

template = PromptTemplate(
    template='Generate name, age, city for a frictional character living in India',
    input_variables=[]
)

chain = template | model | parser

response = chain.invoke({})
print(response)