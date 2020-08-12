import pyrebase
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import Flask, render_template, request, redirect, url_for, session
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

# Use a service account
cred = credentials.Certificate('C:/Users/Dell/Downloads/caterer-cd2e1-ff5caaa728f1.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/menu")
def menu():
   return render_template('menu.html')  

@app.route("/about")
def about():
   return render_template('about.html')

@app.route("/confirm")
def confirm():
   return render_template('confirm.html')


@app.route("/reservation",methods=['POST','GET'])
def reservation():
                error=None
                if request.method=='POST':

                        date=request.form['date']
                        time=request.form['time']
                        persons=request.form['persons']
                        name=request.form['name']
                        email=request.form['email']
                        number=request.form['number']
                        data={
                        u'date':date,
                        u'time':time,
                        u'persons':persons,
                        u'name':name,
                        u'email':email,
                        u'phone':number
                        }
                        db.collection(u'reserve').document(number).set(data)
                        docs = db.collection(u'reserve').where(u'phone',u'==',number).stream()
                        return render_template("retrieve.html",docs=docs)
                        # return redirect(url_for('retrieve'))

                return render_template('reservation.html',error=error)
            
        # if request.method=='POST':
        #     #if request.form['submit']:
        #         date=request.form['date']
        #         time=request.form['time']
        #         persons=request.form['persons']
        #         name=request.form['name']
        #         email=request.form['email']
        #         number=request.form['number']
        #         data={
        #         u'date':date,
        #         u'time':time,
        #         u'persons':persons,
        #         u'name':name,
        #         u'email':email,
        #         u'phone':number
        #         }
        #         db.collection(u'reserve').document(u'20').set(data)

        #         return redirect(url_for('confirm'))

            # except:
            #     error='Please Enter all data'
            #     return render_template('reservation.html',error=error)

        

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
    if 'username' in session:
        return redirect(url_for('reservation'))

    session.pop('username',None)
    error=None
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        
        try:
            user=auth.sign_in_with_email_and_password(username,password)
            session['username']=user
            session['logged_in'] = True

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

@app.route("/logout")
def logout():
    session.pop('username',None)
    return render_template("index.html")

@app.route("/retrieve")
def retrieve():
    # docs = db.collection(u'reserve').where(u'name',u'==',u'Raksha').stream()
    return render_template("retrieve.html")


if __name__ == "__main__":
   app.secret_key='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
   app.run(debug=True)