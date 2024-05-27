from flask import render_template,url_for, flash, redirect
from express import app
from express.forms import SignupForm,LoginForm
from express.models import User, Post


@app.route("/")
@app.route("/home")
def home():
    return render_template("welcome_page.html")

@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
    form = SignupForm()
    if(form.validate_on_submit()):
        flash(f"Welcome {form.first_name.data} {form.last_name.data} to Express!","success")
        return redirect(url_for('log_in'))
    return render_template("sign_up.html",form = form,title = "Sign Up")

@app.route("/log-in",methods=['GET','POST'])
def log_in():
    form = LoginForm()
    if(form.validate_on_submit()):
        if(form.email.data == "admin@gmail.com" and form.password.data=="admin"):
            flash(f"Welcome back to Express!","success")
            return redirect(url_for('log_in'))
        else:
            flash(f"Please check your email and password!","danger")

    return render_template("log_in.html",form = form,title = "Log In")
