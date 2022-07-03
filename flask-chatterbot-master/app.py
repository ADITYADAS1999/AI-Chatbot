from flask import Flask, render_template, request   # render_template is a Flask function from the flask. templating package. render_template is used to generate output from a template file based on the Jinja2 engine that is found in the application's templates folder.
from chatterbot import ChatBot                      # A chatbot is a computer program that simulates human conversation through voice commands or text chats or both. Chatbot, short for chatterbot, is an artificial intelligence (AI) feature that can be embedded and used through any major messaging application       
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)                               # Flask constructor takes the name of current module (__name__) as argument. The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")  # The SQLStorageAdapter allows ChatterBot to store conversation data in any database supported by the SQL Alchemy ORM. 
trainer = ChatterBotCorpusTrainer(english_bot)  # This is a corpus of dialog data that is included in the chatterbot module. Additional information about the chatterbot-corpus module can be found in the ChatterBot Corpus Documentation.
trainer.train("chatterbot.corpus.english")

@app.route("/")                             # This is called the decorator fucntion in python. This essentially wrap our functions inside the app.route fuction.
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":                     # This application run by the python interpreter gives a name variable that set the actual name of the program file.
    app.run()                           #Run my application in local machine.
