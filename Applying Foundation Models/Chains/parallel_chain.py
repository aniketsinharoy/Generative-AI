from langchain_cohere import ChatCohere
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

model_cohere = ChatCohere(model="command-a-03-2025")
model_groq = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt_create_summary = PromptTemplate(
    template="Create summary of the following document: {document}",
    input_variables=['document']
)

prompt_create_quiz = PromptTemplate(
    template="Create 5 quiz questions and answers on the following document: {document}",
    input_variables=['document']
)

prompt_merge = PromptTemplate(
    template="Merge the notes: {notes} and quiz: {quiz} together.",
    input_variables=['notes', 'quiz']
)

parallel_chain = RunnableParallel(
    {
        "notes": prompt_create_summary | model_cohere | parser,
        "quiz": prompt_create_quiz | model_groq | parser
    }
)

merge_chain = prompt_merge | model_cohere | parser

chain = parallel_chain | merge_chain

document = """Life is a quiet teacher, shaping us through joy, loss, effort, and time. It unfolds in ordinary moments: shared meals, long walks, mistakes, laughter, and silence. We chase meaning, stumble often, learn slowly, and grow unexpectedly. Life asks patience when answers delay, courage when fear speaks loudest, and kindness when it seems undeserved. It reminds us that change is constant, control is limited, and connection matters most. In the end, life is not measured by perfection or speed, but by awareness, resilience, and the love we choose to give and receive. Every day invites presence, humility, curiosity, gratitude, and hope."""

response = chain.invoke({'document': document})

print(response)
print(chain.get_graph().draw_ascii())