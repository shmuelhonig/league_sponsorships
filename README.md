# league_sponsorships

## Usage

In order to properly use this web application, please ensure the following:
1. Install pipenv [link](https://pipenv.readthedocs.io/en/latest/)
2. Run `pipenv install` to create a virtual environment and install dependencies
3. Run `pipenv run python models.py` to create the database/schema
4. Run `FLASK_APP=main.py FLASK_ENV=development pipenv run flask run` to run the application in developer mode with debugger on
5. Visit `localhost:5000` or `localhost:5000/find-leagues` in your browser. The latter url accepts three arguments: `location` (a latitude/longitude pair), `radius`, and `budget`
