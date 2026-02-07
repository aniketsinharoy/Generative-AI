from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

model = ChatCohere(model="command-a-03-2025", temperature=1.5)

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(description='Age of the person', gt=0)
    city: str = Field(description='Birth Place of the person')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate name, age, city for a frictional character living in {country}. \n {inst}',
    input_variables=['country'],
    partial_variables={'inst':parser.get_format_instructions()}
)

prompt = template.invoke({'country':'India'})
response = model.invoke(prompt)
paresed_response = parser.parse(response.content)

print(type(paresed_response))
print(paresed_response)