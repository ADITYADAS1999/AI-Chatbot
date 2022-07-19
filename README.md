# MLH(Major League Hacking)-Project_Repo

# 1. How the project works ?


# 2. Tools & Requirements of the project ?

 Used by pip to install required python packages
 Usage: pip install -r requirements.txt

Flask>=1.0.0
chatterbot>=1.0.0
chatterbot-corpus>=1.2.0
SQLAlchemy>=1.2

# flask-chatterbot

#### A web implementation of ChatterBot using Flask.

## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py* with `python app.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)



# 3. Function & Paremiter that use in our code / Explain each function works?

![00000005](https://user-images.githubusercontent.com/58718316/179664616-63f715a3-fa43-44c9-9891-2ee4ee42c6af.PNG)


In our case object of flask class are WSGI application. However flask constructor takes the name of the current module as a argument.



![00001](https://user-images.githubusercontent.com/58718316/179664638-4637d70a-5423-4743-8907-9a63919d1401.PNG)

The route function of flask class is a decorator in python. It actually tells the application which URL associate with that particular function. The / is the URL that bound to the home function.


![00002](https://user-images.githubusercontent.com/58718316/179664642-90c0d673-9f28-43ce-9af9-f7cb0bf90da9.PNG)

The host is basically the name of the host to which we listin to on. The default address is 127.0.0.1  that basically the local host. we set it to 0.0.0.0 when there is a external server available in our system.

The default post is 5000 but we can change it based on requiement.

To be forwarded to underlaying werkzerg server.

# 4. What is Flax! & how it will works!


Flask was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004. According to Ronacher, the idea was originally an April Fool's joke that was popular enough to make into a serious application. The name is a play on the earlier Bottle framework.

A framework is a collection of modules or packages which helps in writing web applications. While working on frameworks in python we don’t have to worry about the low level details such as protocols, sockets or thread management.
A Flask is a micro-framework. It is lightweight and its modular design makes it easily adaptable to developer’s needs. It has a number of out of the box features listed below:


![1_0G5zu7CnXdMT9pGbYUTQLQ](https://user-images.githubusercontent.com/58718316/178398817-bba1ae2e-ec30-4268-a130-d951f05d01a9.png)


- Built-in development server 
- A fast debugger
- Integrated support for unit testing
- Secure cookies support
- HTTP request handling  


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



# 5. How To Install ChatterBot In Python?

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







# 6. Reselt section:
  ## -Output
