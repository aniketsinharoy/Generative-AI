# Example of ShellTool, which allows to execute shell commands and get the output

from langchain_community.tools import ShellTool

shell_tool = ShellTool()
result = shell_tool.invoke("whoami")
print(result)