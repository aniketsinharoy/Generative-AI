#Basic example of using Anthropic chat model with LangChain (Claude)
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model='claude-2')
response = model.invoke("What is the capital of France?")
print(response.content)