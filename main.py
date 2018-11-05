from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = "supersekrit"

@app.route('/')
def home():
    return "hello world"
