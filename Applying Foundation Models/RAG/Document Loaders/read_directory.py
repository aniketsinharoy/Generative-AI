#Example of loading multiple CSV files from a directory using DirectoryLoader and CSVLoader
from langchain_community.document_loaders import CSVLoader, DirectoryLoader
from pathlib import Path

data_dir = Path(__file__).parent.parent.joinpath("Data")

loader = DirectoryLoader(
    data_dir, 
    glob="**/*.csv", 
    loader_cls=CSVLoader
)

documents = loader.load()

#Length of documents is equal to total number of rows in all the CSV files in the directory
print(len(documents))

print(documents[0].page_content)