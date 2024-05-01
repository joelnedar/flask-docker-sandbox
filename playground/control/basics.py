from playground import app
import random

""" ********* HEALTH CHECKS ********* """

@app.route("/")
def hello_check():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej']
    return random.choice(greeting_list) + " World"

@app.route("/names")
def hello_check_name():
    hello_world = hello_check()
    name_list = ['Jenny', 'Linnéa', 'Louise', 'Mikaela']
    return hello_world + ", " + random.choice(name_list)