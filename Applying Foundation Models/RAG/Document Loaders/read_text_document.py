#Example of loading a text document using TextLoader from langchain_community.document_loaders
from langchain_community.document_loaders import TextLoader
from pathlib import Path

text_file_path = Path(__file__).parent.parent.joinpath("Data").joinpath("life.txt")

loader = TextLoader(file_path=text_file_path, encoding='utf-8')

documents = loader.load()

#Documents is a list of Document objects
print(type(documents))

#Lenght of Text file loader is always 1
print(len(documents))

#Each document is a Document object with page_content and metadata attributes
print(type(documents[0]))

print(documents[0].page_content)
print(documents[0].metadata)   