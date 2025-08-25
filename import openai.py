import openai
import requests
from flask import Flask, render_template, request

openai.api_key = 'abc'
   

conversation = [{"role": "system", "content": "your role is such-and-such "}]
print("line 11 reached")
def get_response(message):
    conversation.append({"role":"user","content": message})
    response = openai.ChatCompletion.create(
    model ="gpt-3.5-turbo",
    messages = conversation, 
    temperature = 0,
    )
    conversation.append({"role": "assistant", "content":response['choices'][0]['message']['content']})
    print("function executed")
    return response['choices'][0]['message']['content']






app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = request.form['message']
    response = get_response(message)
    return response
if __name__ == "__main__":
    app.run()

