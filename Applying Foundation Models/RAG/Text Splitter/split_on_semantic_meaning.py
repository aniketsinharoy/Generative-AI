#Example of splitting text based on semantic meaning using the SemanticChunker from langchain_experimental. This splitter uses Cohere's embeddings to determine where to split the text based on semantic similarity, allowing for more meaningful chunks of text that preserve context.

from langchain_experimental.text_splitter import SemanticChunker
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
load_dotenv()

splitter = SemanticChunker(
    embeddings= CohereEmbeddings(model="embed-english-v2.0"),
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

text = """
Artificial intelligence is transforming modern healthcare by enabling faster diagnoses, personalized treatment plans, and improved patient monitoring through wearable devices and predictive analytics. At the same time, sustainable energy is reshaping the global economy as countries invest in solar, wind, and battery technologies to reduce carbon emissions and combat climate change. Both fields rely heavily on innovation and data-driven decision-making, yet they address entirely different challenges—one focused on human health and the other on environmental sustainability.

Meanwhile, space exploration continues to push the boundaries of human knowledge as private companies and national agencies collaborate on missions to the Moon and Mars. Advances in rocket reusability and satellite technology have significantly lowered costs, making space more accessible than ever before. These developments not only expand scientific discovery but also create new opportunities in communication, navigation, and global connectivity.
"""

documents = splitter.create_documents([text])
print(len(documents))
print(documents[0].page_content)