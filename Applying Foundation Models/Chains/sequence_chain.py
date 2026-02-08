from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatCohere(model="command-a-03-2025")
parser = StrOutputParser()

prompt_create_character = PromptTemplate(
    template="Create name, age, city of a frictioanl character who lives in {country}",
    input_variables=['country']
)

prompt_create_story = PromptTemplate(
    template="Create a very short iteresting story on the charcter: {character}",
    input_variables=['character']
)

chain = prompt_create_character | model | parser | prompt_create_story | model | parser
response = chain.invoke({'country':'India'})

print(response)
print(chain.get_graph().draw_ascii())