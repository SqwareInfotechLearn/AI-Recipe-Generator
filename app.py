from phi.agent import Agent
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.model.groq import Groq
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Local Embedder using Sentence Transformers
class LocalEmbedder:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dimensions = len(self.model.encode("test"))

    def get_embedding(self, text: str):
        return self.model.encode(text)

    def get_embedding_and_usage(self, text: str):
        # Generate the embedding and return usage
        embedding = self.get_embedding(text)
        usage = {"tokens": len(text.split())} 
        return embedding, usage

# Create a knowledge base from a PDF
knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "https://www.poshantracker.in/pdf/Awareness/MilletsRecipeBook2023_Low%20Res_V5.pdf",
        "https://www.cardiff.ac.uk/__data/assets/pdf_file/0003/123681/Recipe-Book.pdf",
    ],
    # Use LanceDB as the vector database
    vector_db=LanceDb(
        table_name="recipe",
        uri="tmp\lancedb",
        search_type=SearchType.vector,
        embedder=LocalEmbedder()
    ),
)

# Load the knowledge base
knowledge_base.load()

agent = Agent(
    name="RecipeGenie",
    model=Groq(id="llama-3.3-70b-versatile"),
    # Add the knowledge base to the agent
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Search for recipes based on the ingredients and time available from the knowledge base.",
        "Include the exact calories, preparation time, cooking instructions, and highlight allergens for the recommended recipes.",
        "Provide a list of recipes that match the user's requirements and preferences.",
    ]
)

def main():
    st.title("AI Receipe Creator")

    question = st.text_area("Enter your question:")

    if st.button("Run Flow"):
        if not question.strip():
            st.error("Please enter a question")
            return
        
        try:
            with st.spinner("Processing your question..."):
                response = agent.run(question)
                st.markdown(response.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
