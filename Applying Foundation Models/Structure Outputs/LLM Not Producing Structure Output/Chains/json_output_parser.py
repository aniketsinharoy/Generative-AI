from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
        model='openai/gpt-oss-20b:free',
        base_url="https://openrouter.ai/api/v1",
        temperature=0.7
)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Generate name, age, city for a frictional character living in {country}. \n {instructions}',
    input_variables=['country'],
    partial_variables={'instructions': parser.get_format_instructions()}
)

chain = template | model | parser
response = chain.invoke({'country':'Sri Lanka'})

print(type(response))
print(response)