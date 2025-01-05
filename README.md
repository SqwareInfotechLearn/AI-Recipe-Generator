# AI Recipe Generator

**AI Recipe Generator** is an intelligent application that leverages advanced natural language processing models to create personalized recipes based on user queries. The application uses **Groq LLM**, **LanceDB**, and **Sentence Transformers** to search for recipes from provided PDF sources and generate relevant recipe suggestions. Built with **Streamlit**, it provides an intuitive interface for users to explore recipes by ingredients, preparation time, and dietary preferences.

## Features

- **PDF Knowledge Base**: Recipes are sourced from PDFs, ensuring a diverse and rich collection.
- **Custom Embeddings**: Uses a local embedder (Sentence Transformers) for efficient and accurate vector-based similarity searches.
- **Interactive UI**: Built with Streamlit for a user-friendly experience.
- **Advanced Search**: Powered by LanceDB for fast vector search capabilities.
- **AI-Powered Recommendations**: Utilizes Groq's LLM for detailed and contextual recipe generation.

## Demo

### User Workflow
1. Enter a question or query in the text area (e.g., "Show me recipes using millet").
2. Click on **Run Flow**.
3. The AI processes the query and returns relevant recipes, including:
   - Ingredients
   - Preparation time
   - Cooking instructions
   - Calorie information
   - Allergen warnings

## Technologies Used

- **Python**: Core language for the application.
- **Streamlit**: Frontend framework for building the user interface.
- **Groq LLM**: Large Language Model for contextual understanding and response generation.
- **LanceDB**: Vector database for storing and querying embeddings.
- **Sentence Transformers**: Model for generating text embeddings.
- **Phi**: Framework used for building agents and knowledge bases.
- **Dotenv**: For managing environment variables.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/SqwareInfotechLearn/AI-Recipe-Generator.git
   cd AI-Recipe-Generator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Add environment variables:
   - Create a `.env` file in the root directory.
   - Add any necessary environment variables (e.g., API keys for Groq LLM).

5. Run the application:
   ```
   streamlit run app.py
   ```

## Project Structure

```
.
├── app.py                     # Main application file
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── tmp/                       # Directory for LanceDB database
├── .env                       # Environment variables
```

## Example Queries

- "Show recipes for a quick 15-minute snack."
- "Find recipes that use chicken and rice."
- "List vegetarian recipes without gluten."
