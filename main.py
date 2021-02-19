from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

db = [
    {
    "username":"John", "password":"1234", "role":"admin"
    },
    {
     "username":"Linus", "password":"tech", "role":"member"   
    },
    {
     "username":"Clark", "password":"007", "role":"member"   
    }
]

loggedIn = []

def check_credentials(username,password):
    valid = False
    for row in db:
        if row["username"]==username and row["password"]==password:
            valid = True
            break

    return valid


@app.route('/')
def index():
    return render_template('login_form.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if check_credentials(username,password):
        loggedIn.append(username)
        return redirect(url_for('dashboard',username=username))
    else:
        return redirect('/')
        
@app.route('/dashboard/<username>')
def dashboard(username):
    if username in loggedIn:
        data = {}
        for row in db:
            if row["username"]==username:
                data = row
                break
        return render_template('dashboard.html',username=data["username"],role=data["role"])
    
    else:
        redirect('/') 

if __name__ == "__main__":  
    app.run(host='0.0.0.0', port=5000)





    