from flask import Flask, render_template, request
import os
import openai  # or swap with your model

app = Flask(__name__)

# Setup environment variable in .env or replace with your API key directly
openai.api_key = os.getenv("OPENAI_API_KEY")  # or set manually

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    response = ''
    
    if request.method == 'POST':
        user_input = request.form['user_input']

        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or another if needed
                messages=[
                    {"role": "system", "content": "You are a helpful travel advisor."},
                    {"role": "user", "content": user_input}
                ]
            )
            response = completion.choices[0].message.content.strip()
        except Exception as e:
            response = f"Error: {str(e)}"

    return render_template('index.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)
