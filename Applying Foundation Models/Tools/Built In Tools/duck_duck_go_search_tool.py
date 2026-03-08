# Example of built in tool DuckDuckGoSearchRun to search latest things from web

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke("News on ICC T20 World Cup 2026 Final")
print(result)