from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()


class Review(TypedDict):
    reviewer_name: str
    summary: str
    pros: list[str]
    cons: list[str]
    sentiment: str

model = ChatGroq(model="llama-3.3-70b-versatile")

structure_model = model.with_structured_output(Review)

review_prompt = """Product: LumioSip Insulated Travel Mug (16 oz)
                    Reviewer: Jamie K.

                    Review:
                    I picked this up on a whim because my old mug leaked all over my backpack (RIP notebook). After a week of daily use, I'm honestly impressed—mostly.

                    Pros:
                    * Keeps coffee hot for *hours* (still warm after my morning meetings ☕)
                    * Leak-proof lid actually lives up to the claim
                    * Comfortable grip and fits in my car’s cup holder
                    * Easy to clean—no weird smells sticking around

                    Cons:
                    * Lid takes a second to line up correctly
                    * A bit heavier than expected when full
                    * Pricey compared to basic mugs

                    Overall:
                    Not perfect, but solid. If you commute or travel a lot and hate spills, this mug does its job well. I'd buy it again—just maybe on sale.
                """

response = structure_model.invoke(review_prompt)
print(f"Reviewer Name: {response['reviewer_name']}")
print(f"Sentiment: {response['sentiment']}")