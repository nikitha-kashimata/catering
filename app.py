import pyrebase
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
   return render_template('index.html')

@app.route("/menu")
def menu():
   return render_template('menu.html')  

@app.route("/about")
def about():
   return render_template('about.html')

@app.route("/reservation")
def reservation():
	return render_template('reservation.html')

@app.route("/gallery")
def gallery():
	return render_template('gallery.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

firebaseConfig = {
    "apiKey": "AIzaSyCf-90YLu78oyfdqqjBQmW5N3z41wS9R38",
    "authDomain": "caterer-cd2e1.firebaseapp.com",
    "databaseURL": "https://caterer-cd2e1.firebaseio.com",
    "projectId": "caterer-cd2e1",
    "storageBucket": "caterer-cd2e1.appspot.com",
    "messagingSenderId": "906930722238",
    "appId": "1:906930722238:web:e92764a377c0d7574215ef"
};
 # Initialize Firebase
firebase=pyrebase.initialize_app(firebaseConfig);


if __name__ == "__main__":
   app.run(debug=True)