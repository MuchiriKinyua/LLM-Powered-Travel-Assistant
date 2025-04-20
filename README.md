# LLM Powered Travel Assistant

![Screenshot from 2025-04-20 06-16-14](https://github.com/user-attachments/assets/da993ecf-4505-4069-92aa-1060cc180767)

# Overview

TravelDoc AI Assistant is a simple web application built with Flask that leverages the power of Google's Gemini language model to answer user queries. Users can input any question or prompt through a web interface, and the application will send it to the Gemini API and display the generated response.

This project demonstrates a basic implementation of integrating a large language model into a web application for conversational purposes.

# Features

* **User Interface:** A clean and intuitive web interface built with HTML and CSS.
* **LLM Integration:** Utilizes the Google Gemini API (`gemini-1.5-flash` model by default) to process user input and generate responses.
* **Environment Variable Configuration:** Uses `.env` file to securely manage the Google API key.
* **Basic Error Handling:** Includes a try-except block to catch and display potential errors from the API.
* **"Read More" Functionality:** For longer responses, the initial display is truncated with a "Read more" link to show the full text.

# Technologies Used

* **Python:** The primary programming language.
* **Flask:** A micro web framework for building the web application.
* **Google Generative AI (google-generativeai):** The official Python library for interacting with Google's Gemini models.
* **python-dotenv:** For loading environment variables from a `.env` file.
* **gunicorn:** A WSGI HTTP server for deploying Python web applications.

![Screenshot from 2025-04-20 06-17-05](https://github.com/user-attachments/assets/054da8ed-72cb-42b6-b407-8165237bf3c5)

# Installation

1.  **Clone the repository** (if you have one):
    ```bash
    git clone https://github.com/MuchiriKinyua/LLM-Powered-Travel-Assistant
    cd LLM-Powered-Travel-Assistant
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    * Create a `.env` file in the root of your project.
    * Add your Google API key to the `.env` file:
        ```
        GOOGLE_API_KEY=YOUR_API_KEY_HERE
        ```
        **Note:** Ensure you have obtained a Google API key from the Google Cloud Console.

# Running the Application (Development)

To run the application in development mode:

```bash
python app.py

