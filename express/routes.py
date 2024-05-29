from flask import render_template,url_for, flash, redirect , request
from express import app,bcrypt,db
from express.forms import SignupForm,LoginForm, UpdateAccountForm
from express.models import User, Post
from express.utils.profile_picture_utils import save_picture
from flask_login import login_user , current_user , logout_user , login_required

@app.route("/")
@app.route("/home")
def home():
    if(current_user.is_authenticated):
        return render_template('home.html' , title="Home")
    else : 
        return render_template("welcome_page.html")

@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
    form = SignupForm()
    if(form.validate_on_submit()):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(firstname = form.first_name.data , lastname = form.last_name.data,
                        email = form.email.data , password = hashed_password , 
                        birthday = form.birthday.data )
        new_user.add_user()
        flash(f"Welcome {form.first_name.data} {form.last_name.data} to Express!","success")
        return redirect(url_for('log_in'))
    return render_template("sign_up.html",form = form,title = "Sign Up")

@app.route("/log-in",methods=['GET','POST'])
def log_in():
    form = LoginForm()
    if(form.validate_on_submit()):
        user = User.query.filter_by(email=form.email.data).first()
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"Welcome back to Express!","success")
            return  redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f"Please check your email and password!","danger")

    return render_template("log_in.html",form = form,title = "Log In")
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    image = url_for('static',filename='images/profile_pictures/'+ current_user.image_file)
    form = UpdateAccountForm()
    if(form.validate_on_submit()):
        if(form.picture.data):
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.firstname = form.first_name.data
        current_user.lastname = form.last_name.data
        current_user.email = form.email.data
        current_user.birthday = form.birthday.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.firstname
        form.last_name.data = current_user.lastname
        form.email.data = current_user.email
        form.birthday.data = current_user.birthday


    return render_template("account.html",title = "Account",image = image,form = form)



# The 2023_c version is:
# from <app_name> import app, db
# app.app_context().push()
# from <app_name>.models import User
# user = User.query.first()