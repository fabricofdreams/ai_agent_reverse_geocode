## Where is it?

This application utilizes the Streamlit framework along with various Python libraries to interactively determine the site and country names based on provided coordinates.

#### Installation

Ensure you have the required dependencies installed by running:

```bash
pip install -r requirements.txt
```

#### Usage

1. **Setting up environment variables:**

   Ensure you have a `.env` file configured with necessary environment variables. Use `load_dotenv()` to load these variables.

2. **Initializing AI and tools:**

   - Initialize the ChatOpenAI model with the desired parameters.
   - Define tools for additional functionalities, such as reverse geocoding.

3. **Setting up chat prompt:**

   Configure a chat prompt template including system templates, human templates, and placeholders for dynamic content.

4. **Creating the agent:**

   Utilize the `create_openai_functions_agent` function to create an agent for AI-based interactions using the configured model and tools.

5. **Setting up Streamlit page:**

   Configure the Streamlit page with a custom title and icon.

6. **Handling user interaction:**

   - Receive user input for coordinates through the chat interface.
   - Display conversation history between the user and the AI agent.

7. **Processing user query:**

   Parse user-provided coordinates and generate a template for the AI agent to understand the request.

8. **Running the agent:**

   Invoke the agent to process the user's query, providing latitude and longitude as input.

9. **Displaying results:**

   Show the AI agent's response in the chat interface along with the site and country names corresponding to the provided coordinates.

#### Note

Ensure proper handling of user input errors and exceptions to provide a smooth user experience.

---

This documentation outlines the functionality and usage of the provided Python script for determining site and country names based on coordinates using AI-based interactions within a Streamlit application.
