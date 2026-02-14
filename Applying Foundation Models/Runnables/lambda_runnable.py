#Example of using RunnableLambda to create a custom function that can be used in a chain
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

def count_words(document: str):
    return len(document.split())

model = ChatCohere(model="command-a-03-2025")

template_joke = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)


str_parser = StrOutputParser()

count_words_runnable = RunnableLambda(count_words)

sequence_chain_count_joke_words = RunnableSequence(template_joke, model, str_parser, count_words_runnable)


response = sequence_chain_count_joke_words.invoke({'topic':'school'})
print(response)
