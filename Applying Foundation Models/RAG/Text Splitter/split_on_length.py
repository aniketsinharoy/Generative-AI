#Example of using CharacterTextSplitter to split text into chunks of a specified length without overlap.

from langchain_text_splitters import CharacterTextSplitter

text = "This is a test string to be split into chunks of a specified length. The splitter will create chunks of 10 characters each without any overlap."

splitter = CharacterTextSplitter(
    chunk_size = 10, 
    chunk_overlap = 0,
    separator=''
)
chunks = splitter.split_text(text)
print(chunks)