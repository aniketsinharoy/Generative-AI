#Example of splitting text based on text structure using RecursiveCharacterTextSplitter from langchain_text_splitters

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
No matter which branch you chose — Mechanical, Civil, Electrical, ECE, IT, or even Computer Science — your degree does not decide your destiny.

Yes, you read that right.

I've seen non-CS students crack top product-based companies.
I've also seen Computer Science graduates struggle.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0
)
chunks = splitter.split_text(text)
print(chunks)