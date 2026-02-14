#Example of using LCEL to create a simple chain that generates a joke based on a given topic
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatCohere(model="command-a-03-2025")

template_joke = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

str_parser = StrOutputParser()

#simple sequence chain
sequence_chain_make_joke = RunnableSequence(template_joke, model, str_parser)

#LCEL Expression
sequence_chain_make_joke = template_joke | model | str_parser