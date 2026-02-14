#Example of using RunnablePassthrough to create a chain that simply returns the input without any modifications
from langchain_core.runnables import RunnablePassthrough

pass_through = RunnablePassthrough()
output = pass_through.invoke({'topic':'school'})
print(output)

output = pass_through.invoke(2)
print(output)