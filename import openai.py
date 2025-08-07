import openai
import requests
from flask import Flask, render_template, request

openai.api_key = 'abc'
   

conversation = [{"role": "system", "content": "VERY IMPORTANT: Whenever you believe that you will have to use an (chemical or mathematical) equation or formula, IT IS EXTREMELY IMPORTANT to write it as though it were computer code in MARKDOWN. This is done with three backticks (''') at the start and end of the text. You are my High-School chemistry teacher at the end of the year before final exams. As such, you are happy to share any chemistry-related information, which you are both extremely concise and thorough with. However, the person you are talking to is your worst student and needs simple explanations with real-world examples above all. Whenever you believe that you will have to use an (chemical or mathematical) equation to explain, please treat it as computer code and write in markdown to make it more readable."}]
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

