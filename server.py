from flask import Flask, render_template
import datetime
import requests

GENDERIZE_API = "https://api.genderize.io?name="
AGIFY_API = "https://api.agify.io?name="
INDEX_HTML = 'index.html'
GUESS_HTML = 'guess.html'
GENDER_KEY = "gender"
AGE_KEY = "age"


app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template(INDEX_HTML, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_response = api_request(url=GENDERIZE_API, name=name)
    gender_data = gender_response.json()
    age_response = api_request(url=AGIFY_API, name=name)
    age_data = age_response.json()
    return render_template(GUESS_HTML, name=name, gender=gender_data[GENDER_KEY], age=age_data[AGE_KEY])


def api_request(url: str, name: str):
    return requests.get(url + name)


if __name__ == "__main__":
    app.run(debug=True)
