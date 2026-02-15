#Example of splitting a Python code snippet into chunks based on its structure using the RecursiveCharacterTextSplitter from the langchain_text_splitters library. 
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

text = """
class Dog:
    # A class attribute, shared by all instances
    species = "Canis familiaris"

    # The __init__ method acts as a constructor
    def __init__(self, name, age):
        self.name = name  # Instance attribute (unique to each object)
        self.age = age    # Instance attribute (unique to each object)

    # An instance method (a function defined within the class)
    def bark(self):
        return f"{self.name} says Woof!"

# Create instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Access attributes and call methods
print(f"{dog1.name} is {dog1.age} years old and a {Dog.species}.")
print(dog2.bark())
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=70,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(chunks)