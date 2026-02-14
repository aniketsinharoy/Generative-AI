#Example of loading a website using WebBaseLoader from langchain_community.document_loaders. 
#This loader fetches the content of the specified URL and extracts the text and metadata.
from langchain_community.document_loaders import WebBaseLoader

website_url = "https://www.flipkart.com/samsung-galaxy-watch7-44mm-lte/p/itmf8bef51645876?pid=SMWH2EHFNQMJHPHC&lid=LSTSMWH2EHFNQMJHPHCAGOZZ1&marketplace=FLIPKART&param=2871&BU=EmergingElectronics&pageUID=1771091167335"

loader = WebBaseLoader(website_url)
documents = loader.load()

print(len(documents))

print(documents[0].page_content[:500])

print(documents[0].metadata)