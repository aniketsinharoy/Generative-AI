from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

model_cohere = ChatCohere(model="command-a-03-2025")

class Person(BaseModel):
    sentiment: Literal["positive","negative"] = Field(description="The person sentiment about his life.")
    thought: str = Field(description="Thoughts of the person on life")

parser_pydantic = PydanticOutputParser(pydantic_object=Person)
parser_str = StrOutputParser()

prompt_sentiment = PromptTemplate(
    template="Predict the sentiment of the user about his life: {thought} \n {inst}",
    input_variables=['thought'],
    partial_variables={'inst': parser_pydantic.get_format_instructions()}
)

prompt_motivation = PromptTemplate(
    template="Write a short motivational speech for a person having this thought: {thought}",
    input_variables=['thought']
)

prompt_thank_you = PromptTemplate(
    template="Just say thank youn in 1 line for a person having this thought: {thought}",
    input_variables=['thought']
)

thought_negative = """They see life through a lens of doubt, where hope feels fragile and every step seems heavier than it should be. Yet beneath the pessimism lies a tired heart, shaped more by disappointment than by the absence of worth or possibility.
"""
thought_positive = """They see challenges as lessons, not obstacles, and meet each day with calm confidence.
Guided by optimism and gratitude, they choose hope, growth, and kindness even in uncertainty.
"""

sentiment_chain = prompt_sentiment | model_cohere | parser_pydantic
conditional_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', {'thought': lambda x:x.thought} | prompt_thank_you | model_cohere | parser_str),
    (lambda x:x.sentiment == 'negative', {'thought': lambda x:x.thought} | prompt_motivation | model_cohere | parser_str),
    RunnableLambda(lambda x:"Life is beautiful. But can't understand what you told.")
)

chain = sentiment_chain | conditional_chain
response = chain.invoke({'thought':thought_negative})

print(response)
print(chain.get_graph().draw_ascii())