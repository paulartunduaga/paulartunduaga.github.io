#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:36:22 2020

@author: intern
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/polite')

def polite():
    return 'Hello ladies and gentlemen!'

@app.route('/rude')

def rude():
    return 'Hello you cunts'


@app.route('/firstfrontend')
def index():
    return render_template('first_front_end.html')

