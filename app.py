import pyrebase
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
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
auth=firebase.auth()

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

@app.route("/forgot",methods=['POST','GET'])
def forgot():
    error=None
    if request.method=='POST':
        email = request.form['email']

        try:
            auth.send_password_reset_email(email)
            return redirect(url_for('login'))

        except:
            error='Enter correct email'
            return render_template('forgot.html',error=error)

    return render_template('forgot.html',error=error)

@app.route("/login",methods=['POST','GET'])
def login():
    error=None
    if request.method=='POST':
        email=request.form['username']
        password=request.form['password']
        
        try:
            user=auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('reservation'))

        except:
            error='Invalid Credentials. Please try again.'
            return render_template('login.html',error=error)

    return render_template('login.html',error=error)

    

@app.route("/signup",methods=['POST','GET'])
def signup():
    error=None
    if request.method == 'POST':
        name=request.form['username']
        password=request.form['password']
        cpassword=request.form['confirmpassword']
        if(cpassword==password):
            user=auth.create_user_with_email_and_password(name, password)
            return redirect(url_for('login'))

        else:
            error='Invalid Credentials. Please try again.'

    return render_template('signup.html',error=error)




if __name__ == "__main__":
   app.run(debug=True)