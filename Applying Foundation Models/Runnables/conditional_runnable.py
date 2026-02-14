#Example of using RunnableBranch to create a conditional chain that branches based on the length of the input text
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatCohere(model="command-a-03-2025")

template_detailed_report = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template_summary = PromptTemplate(
    template="Summarize the topic: {topic}",
    input_variables=['topic']
)

template_joke = PromptTemplate(
    template="Make a joke on: {topic}",
    input_variables=['topic']
)

str_parser = StrOutputParser()

#simple sequence chain
sequence_chain_make_detailed_report = RunnableSequence(template_detailed_report, model, str_parser)
sequence_chain_make_summary = RunnableSequence(template_summary, model, str_parser)
sequence_chain_make_joke = RunnableSequence(template_joke, model, str_parser)


#conditional chain
#if the input text has more than 300 words then summarize else make a joke on the topic
conditional_chain = RunnableBranch(
    (lambda x:len(x.split()) > 300, sequence_chain_make_summary),
    sequence_chain_make_joke
)

main_chain = RunnableSequence(sequence_chain_make_detailed_report, conditional_chain)

response = main_chain.invoke({'topic':'school'})
print(response)
