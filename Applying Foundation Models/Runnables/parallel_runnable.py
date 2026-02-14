#Example of using RunnableParallel to create a chain that generates both a joke and a sentence based on a given topic in parallel
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatCohere(model="command-a-03-2025")

template_joke = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

template_sentence = PromptTemplate(
    template="Write a sentence on: {topic}",
    input_variables=['topic']
)

str_parser = StrOutputParser()

#simple sequence chain
sequence_chain_make_joke = RunnableSequence(template_joke, model, str_parser)
sequence_chain_make_sentence = RunnableSequence(template_sentence, model, str_parser)


#parallel chain
parallel_chain = RunnableParallel({
    'joke': sequence_chain_make_joke,
    'sentence': sequence_chain_make_sentence
})

response = parallel_chain.invoke({'topic':'school'})
print(response)
