#Example of reading a CSV file using CSVLoader from langchain_community.document_loaders
from langchain_community.document_loaders import CSVLoader
from pathlib import Path

csv_file_path = Path(__file__).parent.parent.joinpath("Data").joinpath("people.csv")

loader = CSVLoader(file_path=csv_file_path, encoding='utf-8')
documents = loader.load()

#Length of documents is equal to number of rows in the CSV file
print(len(documents))

#Each document page_conetent is the content of the row in the CSV file
print(documents[0].page_content)

#Each document metadata is a dictionary having metadata details
print(documents[0].metadata)