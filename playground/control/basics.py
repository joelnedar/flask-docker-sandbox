#!/usr/bin/env python3.6.3
from flask import jsonify
from playground import app
import random

""" ********* HEALTH CHECKS ********* """


@app.route("/")
def hello_check():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej']
    return jsonify(random.choice(greeting_list) + " World")
