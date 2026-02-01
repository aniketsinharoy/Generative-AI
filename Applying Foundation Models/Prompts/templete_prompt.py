from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

topic = input("Enter topic name: ")
tone = input("Enter poem tone: ")

templete = PromptTemplate(
    template="Write 5 lines poem on {topic} in a {tone} tone",
    input_variables=['topic', 'tone'],
    validate_template=True
)

prompt = templete.invoke({
    'topic':topic,
    'tone': tone
})

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )

response = model.invoke(prompt)
print(response.content)