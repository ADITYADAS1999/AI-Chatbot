# MLH(Major League Hacking)-Project_Repo

![picd](https://user-images.githubusercontent.com/58718316/199229225-778637f1-a71f-49d2-97ae-c366e7d7c04d.PNG)


# 1 Introduction about the project 📯

There are millions and millions of projects are evaluate and born each day. The technology, maintainers & contributors both are involve in different field of technology. Not only that emergency services are also depends on this technology like hospitality, management and reservation services. One minute of delay can generate huge impact on a specific service. Hence chatbot concept are really amazing and reliable concept to our daily life challenges. Also this concept use for many services and emergency usecases.


# 2. How this project works ⚙

ChatterBot is a Python library that makes it easy to generate automated responses to a user’s input. ChatterBot uses a selection of machine learning algorithms to produce different types of responses. This makes it easy for developers to create chat bots and automate conversations with users. The language independent design of ChatterBot allows it to be trained to speak any language. Additionally, the machine-learning nature of ChatterBot allows an agent instance to improve it’s own knowledge of possible responses as it interacts with humans and other sources of informative data.

Our project basically works in the following manner:

- Get the input from the user.
- Process the input.
- Returns the value that is generated with the highest confidence value.
- Return the response to the user.
- Working of the Project
- First, the chatbot is trained with a set of training data present in /data directory and creates a sqlite3 database. When the users inputs a query the bot searches for a response from the database if it finds an answer then it prints the response or else it will search for an answer from Wikipedia using web scraping and provide an appropriate response.


# 3. How to install the project in your local system 🖥🖱


- Clone the repository using

```
git https://github.com/ADITYADAS1999/MLH-Project_Repo-Major-League-Hacking-
```
- Open the terminal/cmd and navigate to the project folder.

```
cd ChatBot-Flask
```

- Install the requirments.txt using

```
pip install requirments.txt
```

- Requirments.txt will install all the required dependancies.

- Now run the chatbot.py using

```
python chatbot.py
```

The app should now be running on  http://localhost:5000

Open <mark> http://localhost:5000 </mark> in your browser to interact with the chatbot.


# 4. Where this technology basically uses ? 💁🏻‍♀️💁🏻‍♂️

There are different type of chatbot are use in different field, like simple chatbot(a user interacts with a chatbot to certain time of work, the flow of the conversation is set), smart chatbot(AI-enabled smart chatbots are designed to simulate near-human interactions with user. for eample virtual assistent like Apple siri, Amazon alexa), Hybrid chatbots(Chatbots that help with a medical diagnosis combine the capabilities of both simple and smart chatbots.) In this project we basically use simple chatbot technique. This bot basically trained by custom yaml files and according to the flow bot interact with user, also with a voice feature. This bot better to use in emergency services in different field like hospitality, management services, reservation services etc. For example a user have some problem regarding flight reservation and can't find a particular sloution, in this condition bot services are the life line, It does't need a human sit ohersite and response, the bot service automatocally done all the things. 


# 5. Why this project ? 👨‍🏫

I build this project because first of all I have some interest in this technology and also good knowledge in python programming. My main goal is that make this project cost optimestic and less complexcity. By optimizing the cost many organisation and user try to use this technology. And any contributors and maintainer can involve and contribute in less complex projects so it is easy the maintain and modify anytime infuture. 


# 6. Project code details ❗🔭📑📚


### About ChatterBot

![banner](https://user-images.githubusercontent.com/58718316/200725793-a73040ca-ec81-48b3-b082-4ebd4c60a51f.png)

ChatterBot is a Python library that makes it easy to generate automated responses to a user’s input. ChatterBot uses a selection of machine learning algorithms to produce different types of responses. This makes it easy for developers to create chat bots and automate conversations with users. For more details about the ideas and concepts behind ChatterBot see the process flow diagram.

![yu](https://user-images.githubusercontent.com/58718316/200725855-71d8583b-445e-41f8-ae02-abca31e7110a.PNG)


```
# import python libraries 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import os
from flask import Flask, render_template, request, jsonify

```

## Training

ChatterBot includes tools that help simplify the process of training a chat bot instance. ChatterBot’s training process involves loading example dialog into the chat bot’s database. This either creates or builds upon the graph data structure that represents the sets of known statements and responses. When a chat bot trainer is provided with a data set, it creates the necessary entries in the chat bot’s knowledge graph so that the statement inputs and responses are correctly represented.

![000002](https://user-images.githubusercontent.com/58718316/200607465-3f9a2bf3-b632-493a-b65e-b06e7e64d3c3.PNG)

Several training classes come built-in with ChatterBot. These utilities range from allowing you to update the chat bot’s database knowledge graph based on a list of statements representing a conversation, to tools that allow you to train your bot based on a corpus of pre-loaded training data.

You can also create your own training class. This is recommended if you wish to train your bot with data you have stored in a format that is not already supported by one of the pre-built classes listed below.

## Setting the training class 

ChatterBot comes with training classes built in, or you can create your own if needed. To use a training class you call train() on an instance that has been initialized with your chat bot.


### Training classes

### Training via list data :
For the training process, you will need to pass in a list of statements where the order of each statement is based on its placement in a given conversation.

For example, if you were to run bot of the following training calls, then the resulting chatterbot would respond to both statements of “Hi there!” and “Greetings!” by saying “Hello”.

chatbot.py
```
 chatbot = ChatBot('Training Example')
 
```
train.py
```
from chatbot import chatbot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Greetings!",
    "Hello",
])

```

You can also provide longer lists of training conversations. This will establish each item in the list as a possible response to it’s predecessor in the list.

train.py

```
trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])

```


### Training with corpus data :

ChatterBot comes with a corpus data and utility module that makes it easy to quickly train your bot to communicate. To do so, simply specify the corpus data modules you want to use.

chatbot.py
```
 chatbot = ChatBot('Training Example')
 
 ```
 
 
 train.py
 
 ```
 
 from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

```
### Specifying corpus scope :

It is also possible to import individual subsets of ChatterBot’s corpus at once. For example, if you only wish to train based on the english greetings and conversations corpora then you would simply specify them.
 
train.py

```

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

```

You can also specify file paths to corpus files or directories of corpus files when calling the train method.

train.py

```

trainer.train(
    "./data/greetings_corpus/custom.corpus.json",
    "./data/my_corpus/"
)

```



```

# Flask constructor takes the name of current module (__name__) as argument.

app = Flask(__name__)

bot= ChatBot('ChatBot')

trainer = ListTrainer(bot)

for file in os.listdir('C:/Users/Anonymous/Desktop/ChatBot-Flask/data/'):

    chats = open('C:/Users/Anonymous/Desktop/ChatBot-Flask/data/' + file, 'r').readlines()

    trainer.train(chats)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():

    message = str(request.form['messageText'])

    bot_response = bot.get_response(message)

    while True:

        if bot_response.confidence > 0.1:

            bot_response = str(bot_response)      
            print(bot_response)
            return jsonify({'status':'OK','answer':bot_response})
 
        elif message == ("bye"):

            bot_response='Hope to see you soon'

            print(bot_response)
            return jsonify({'status':'OK','answer':bot_response})

            break

        else:
        
            try:
                url  = "https://en.wikipedia.org/wiki/"+ message
                page = get(url).text
                soup = BeautifulSoup(page,"html.parser")
                p    = soup.find_all("p")
                return jsonify({'status':'OK','answer':p[1].text})

            except IndexError as error:

                bot_response = 'Sorry i have no idea about that.'
            
                print(bot_response)
                return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run()
  
  
```

### Training with the Ubuntu dialog corpus

```

Warning

The Ubuntu dialog corpus is a massive data set. Developers will currently experience significantly decreased performance in the form of delayed training and response times from the chat bot when using this corpus.

```
    
# 7. Tools & Requirements of the project ? 🗝🛠🔩

 Used by pip to install required python packages
 Usage: pip install -r requirements.txt

Flask>=1.0.0
chatterbot>=1.0.0
chatterbot-corpus>=1.2.0
SQLAlchemy>=1.2

- # flask-chatterbot

![robo_small](https://user-images.githubusercontent.com/58718316/180588383-1ed169d5-2d9d-4683-9808-7ce92e45dc55.gif)


#### A web implementation of ChatterBot using Flask.

- ## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py* with `python app.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)



# 8. Function & Paremiter that use in our code / Explain each function works? ⚙💽💾




In our case object of flask class are WSGI application. However flask constructor takes the name of the current module as a argument.



![00001](https://user-images.githubusercontent.com/58718316/179664638-4637d70a-5423-4743-8907-9a63919d1401.PNG)

The route function of flask class is a decorator in python. It actually tells the application which URL associate with that particular function. The / is the URL that bound to the home function.


![00002](https://user-images.githubusercontent.com/58718316/179664642-90c0d673-9f28-43ce-9af9-f7cb0bf90da9.PNG)

The host is basically the name of the host to which we listin to on. The default address is 127.0.0.1  that basically the local host. we set it to 0.0.0.0 when there is a external server available in our system.

The default post is 5000 but we can change it based on requiement.

To be forwarded to underlaying werkzerg server.

# 9. What is Flask! & how it will works! 🎯🎮👨‍💻


Flask was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004. According to Ronacher, the idea was originally an April Fool's joke that was popular enough to make into a serious application. The name is a play on the earlier Bottle framework.

A framework is a collection of modules or packages which helps in writing web applications. While working on frameworks in python we don’t have to worry about the low level details such as protocols, sockets or thread management.
A Flask is a micro-framework. It is lightweight and its modular design makes it easily adaptable to developer’s needs. It has a number of out of the box features listed below:


![1_0G5zu7CnXdMT9pGbYUTQLQ](https://user-images.githubusercontent.com/58718316/178398817-bba1ae2e-ec30-4268-a130-d951f05d01a9.png)


- Built-in development server 
- A fast debugger
- Integrated support for unit testing
- Secure cookies support
- HTTP request handling  


## WSGI

![download](https://user-images.githubusercontent.com/58718316/200734336-48538613-7082-4dba-9afb-60b2a64b8b2b.jpg)

Flask is a WSGI application. A WSGI server is used to run the application, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses. WSGI stands for "Web Server Gateway Interface". It is used to forward requests from a web server (such as Apache or NGINX) to a backend Python web application or framework. From there, responses are then passed back to the webserver to reply to the requestor.

![wsgi-interface](https://user-images.githubusercontent.com/58718316/200732153-45e37f44-9433-406a-a87e-45380a2e9ee4.png)

To serving thousands of requests for dynamic content at once is the domain of WSGI servers, not frameworks. WSGI servers handle processing requests from the web server and deciding how to communicate those requests to an application framework's process. The segregation of responsibilities is important for efficiently scaling web traffic.

![web-browser-server-wsgi](https://user-images.githubusercontent.com/58718316/200732626-3fc2efd1-b9f0-498e-97bf-2e2c1c88c928.png)

## JINJA2 Template

![1200px-Jinja_software_logo svg](https://user-images.githubusercontent.com/58718316/200734657-413e97ef-d57a-411a-a7b8-a5af15eb38a9.png)


The name Jinja was chosen because it's the name of a Japanese temple and template share a similar pronunciation. Jinja2 is a commonly-used templating engine for web frameworks such as Flask, Bottle, Morepath and, as of its 1.8 update, optionally Django as well. Jinja2 is also used as a template language by configuration management tool Ansible and the static site generator Pelican, among many other similar tools.


### How to actually install flask

- Step-1: 

Download python > 2.7.0
 ```
 https://www.python.org/  
 ```

- Step-2: 

virtual env -> Virtual python environment builder

- For windows
 ```
 pip install  virtualenv
 ```
 
- For Linux
 ```
 sudo apt-get install virtualenv
 ```

- Step-3: 

Once install new virtual environment is created in a folder.
```
mldir newproj
cd newproj
virtualenv venv
```

- Step-4: 

To activate corresponding environment use the following command.

```
venv\script\active
```

- Step-5: 

Finally install flask

```
!pip install flask
```


- ### 4.1. WSGI


- ### 4.2. Jinja2
 
# 10. How To Install ChatterBot In Python? 🤖🐍

- To install ChatterBot from PyPi (Python Package Index) using pip run the following command in your terminal.

```
pip install chatterbot
```

- You can install the latest development version of ChatterBot directly from GitHub using pip.
```
pip install git+git://github.com/gunthercox/ChatterBot.git@master
```


- Download a copy of the code from GitHub. You may need to install git.

```
git clone https://github.com/gunthercox/ChatterBot.git
```

- If you already have ChatterBot installed and you want to check what version you have installed you can run the following command.

```
python -m chatterbot --version
```



## 11. Result section ⚗🧪🔬

  - ## Output
  
  
 
## 12. Future scope 🚩

  
So in this project, this is only a part or called it as version 0.1. According to our project our ultimate goal is to productivity high and cost low that is we add more feature, functionality. In future we involve more contributors, maintainers to make this project beneficial and useful, and user friendly for every user in any other platform.
  
  
   
  Congratulations 🎉🎊
  
![ezgif com-gif-maker](https://user-images.githubusercontent.com/58718316/195966856-71b1533e-3eff-4d66-b117-d2c618274d22.gif)


  
