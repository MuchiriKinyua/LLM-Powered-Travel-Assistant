from flask import Flask, render_template, request
import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
from flask import jsonify

load_dotenv()
app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Store history in memory
chat_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    response = ''

    if request.method == 'POST':
        user_input = request.form['user_input']

        try:
            model_name = 'gemini-1.5-flash'
            model = genai.GenerativeModel(model_name=model_name)
            chat_completion = model.generate_content([{"role": "user", "parts": [user_input]}])
            response = chat_completion.text.strip()

            # Save the interaction to history
            chat_history.append({
                "question": user_input,
                "answer": response,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        except Exception as e:
            response = f"Error: {str(e)}"

    return render_template('index.html', user_input=user_input, response=response, history=chat_history)

@app.route('/delete_history', methods=['POST'])
def delete_history():
    index = int(request.form.get('index'))
    if 0 <= index < len(chat_history):
        del chat_history[index]
        return jsonify(success=True)
    return jsonify(success=False)


if __name__ == '__main__':
    app.run(debug=True)
