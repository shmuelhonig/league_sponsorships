from flask import Flask, render_template, request, url_for, redirect, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Leagues

from geopy.distance import geodesic

# create session object to communicate with database
engine = create_engine('sqlite:///leagues.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
app.secret_key = "supersekrit"


@app.route('/', methods=['GET', 'POST'])
@app.route('/add-league/', methods=['GET', 'POST'])
def add_league():
    if request.method == 'POST':
        # create new League instance using form data
        newLeague = Leagues(
            name=request.form['name'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude'],
            price=request.form['price']
        )
        session.add(newLeague)
        session.commit()
        return redirect(url_for('add_league'))
    else:
        return render_template('addLeague.html')

@app.route('/find-leagues/')
def find_leagues():
    # extract values of query arguments
    location = request.args.get('location')
    radius = request.args.get('radius')
    budget = request.args.get('budget')
    # convert location parameter to tuple
    location_tuple = (location.split(',')[0], location.split(',')[1])
    # extract list of leagues from database
    leagues = session.query(Leagues).all()
    # get list of all leagues within given radius
    nearby_leagues = []
    for league in leagues:
        distance = geodesic((league.latitude, league.longitude), location_tuple).miles
        if distance < float(radius):
            nearby_leagues.append(league)
    return render_template('findLeagues.html', leagues=leagues, location=location, radius=radius, budget=budget, nearby_leagues=nearby_leagues)
