#Example of creating a simple sequence chain that generates a joke based on a given topic using RunnableSequence
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

template_explain_joke = PromptTemplate(
    template="Explain the joke: {joke}",
    input_variables=['joke']
)

str_parser = StrOutputParser()

#simple sequence chain
sequence_chain_make_joke = RunnableSequence(template_joke, model, str_parser)
joke = sequence_chain_make_joke.invoke({'topic':'School'})

#adding one sequence runnable to another
sequence_chain_exaplain_joke = RunnableSequence(sequence_chain_make_joke, template_explain_joke, model, str_parser)
print(sequence_chain_exaplain_joke.invoke({'topic': 'school'}))
