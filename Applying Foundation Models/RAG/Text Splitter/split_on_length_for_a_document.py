#Example of splitting a document into chunks of a specified length using CharacterTextSplitter from langchain_text_splitters.

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from pathlib import Path

text_file_path = Path(__file__).parent.parent.joinpath("Data").joinpath("life.txt")
loader = TextLoader(text_file_path)
documents = loader.load()

print(f"Original document: {documents[0].page_content}")

splitter = CharacterTextSplitter(
    chunk_size = 10, 
    chunk_overlap = 0,
    separator=''
)
chunks = splitter.split_documents(documents)
print(f"Split documents: {chunks}")

print(f"Number of chunks: {len(chunks)}")
print(f"First chunk: {chunks[0].page_content}")