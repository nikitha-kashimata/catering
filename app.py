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
db = firebase.firestore.client()

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
    data = {
    u'stringExample': u'Hello, World!',
    u'booleanExample': True,
    u'numberExample': 3.14159265,
    # u'dateExample': datetime.datetime.now(),
    u'arrayExample': [5, True, u'hello'],
    u'nullExample': None,
    u'objectExample': {
        u'a': 5,
        u'b': True
    }
    }

    db.collection(u'data').document(u'one').set(data)
        # error=None
        # if request.method=='POST':
        #     #if request.form['submit']:
        #         data={
        #         u"date":u"request.form['date']",
        #         u"time":u"request.form['time']",
        #         u"persons":u"request.form['persons']",
        #         u"name":u"request.form['name']",
        #         u"email":u"request.form['email']",
        #         u"phone":u"request.form['number']"
        #         }
        #         db.collection(u'reserve').document(u'1').set(data)

        #         return redirect(url_for('confirm'))

        #     # except:
        #     #     error='Please Enter all data'
        #     #     return render_template('reservation.html',error=error)

    return render_template('reservation.html',error=error)

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