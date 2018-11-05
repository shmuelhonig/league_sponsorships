from flask import Flask, render_template, request, url_for, redirect, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Leagues

# create session object to communicate with database
engine = create_engine('sqlite:///leagues.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
app.secret_key = "supersekrit"


@app.route('/')
def home():
    return "hello world"
