#Example of reading a PDF file using PyPDFLoader from langchain_community.document_loaders
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

pdf_file_path = Path(__file__).parent.parent.joinpath("Data").joinpath("Strings.pdf")

loader = PyPDFLoader(file_path=pdf_file_path)
documents = loader.load()

#Length of documents is equal to number of pages in the PDF file
print(len(documents))

print(documents[0].page_content)