from express.models import Post

from flask import render_template,url_for, request, Blueprint
from flask_login import  current_user

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    if(current_user.is_authenticated):
        image = url_for('static',filename='images/profile_pictures/'+ current_user.image_file)
        page = request.args.get('page',default = 1,type = int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page = 5)
        return render_template('home.html' , title="Home", image = image, posts = posts, context="Home")
    else : 
        return render_template("welcome_page.html")