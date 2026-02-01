from langchain_core.prompts import PromptTemplate

templete = PromptTemplate(
    template="Write 5 lines poem on {topic} in a {tone} tone",
    input_variables=['topic','tone'],
    validate_template=True
)
templete.save("./Prompts/poem_templete.json")