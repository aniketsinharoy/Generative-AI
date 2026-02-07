from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
)

parser = JsonOutputParser()

template = PromptTemplate(
    template= 'Generate name, age, city for a frictional character living in {country}. \n {format_instruction}',
    input_variables=['country'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)

prompt = template.invoke({'country':'India'})
response = model.invoke(prompt)
parsed_response = parser.parse(response.content)

print(type(parsed_response))
print(parsed_response)