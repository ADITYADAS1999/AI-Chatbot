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
git clone https://github.com/VRohit1901/ChatBot-Flask
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

```

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import os
from flask import Flask, render_template, request, jsonify

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

![00000005](https://user-images.githubusercontent.com/58718316/179664616-63f715a3-fa43-44c9-9891-2ee4ee42c6af.PNG)


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

## JINJA2 Template


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
  
  
  
  
  
  
  
  Congratulations 🎉🎊
  
![ezgif com-gif-maker](https://user-images.githubusercontent.com/58718316/195966856-71b1533e-3eff-4d66-b117-d2c618274d22.gif)


  
