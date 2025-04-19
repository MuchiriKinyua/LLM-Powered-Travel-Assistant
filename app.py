from flask import Flask, render_template, request
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    response = ''

    if request.method == 'POST':
        user_input = request.form['user_input']

        try:
            # Specify the new model name
            model_name = 'gemini-1.5-flash'  # Or another supported model

            # Use the specified model
            model = genai.GenerativeModel(model_name=model_name)
            chat_completion = model.generate_content([{"role": "user", "parts": [user_input]}])
            response = chat_completion.text.strip()

        except Exception as e:
            response = f"Error: {str(e)}"

    return render_template('index.html', user_input=user_input, response=response)


if __name__ == '__main__':
    app.run(debug=True)