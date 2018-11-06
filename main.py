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
        flash('New league added successfully')
        return redirect(url_for('add_league'))
    else:
        return render_template('addLeague.html')


@app.route('/find-leagues/')
def find_leagues():
    # extract values of query arguments
    location = request.args.get('location')
    radius = request.args.get('radius', default=0)
    budget = request.args.get('budget')
    # convert location parameter to tuple
    location_tuple = (location.split(',')[0], location.split(',')[1])
    # extract list of leagues from database
    leagues = session.query(Leagues).order_by('price').all()
    # get list of all leagues within given radius
    nearby_leagues = []
    for league in leagues:
        distance = geodesic((league.latitude, league.longitude),
                            location_tuple).miles
        if distance < float(radius):
            nearby_leagues.append(league)
    # remove last (most expensive) league if over budget
    total_price = 0
    for league in nearby_leagues:
        total_price = total_price + league.price
    final_price = total_price
    while final_price > int(budget):
        truncated = nearby_leagues.pop()
        final_price = final_price - truncated.price

    return render_template(
        'findLeagues.html',
        leagues=leagues,
        location=location,
        radius=radius,
        budget=budget,
        nearby_leagues=nearby_leagues
    )
