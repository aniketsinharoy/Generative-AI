from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatCohere(model="command-a-03-2025")

prompt = PromptTemplate(
    template="Create name, age, city of a frictioanl character who lives in {country}",
    input_variables=['country']
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'country':'India'})

print(response)