from flask import render_template,url_for, flash, redirect , request, abort, Blueprint
from flask_login import  current_user , login_required

from express import db
from express.posts.forms import CreatePostForm 
from express.models import Post

posts = Blueprint('posts',__name__)

@posts.route("/post/create",methods=['GET','POST'])
@login_required
def create_post():
    image = url_for('static',filename='images/profile_pictures/'+ current_user.image_file)
    form = CreatePostForm()
    if(form.validate_on_submit()):
        newPost = Post(title = form.title.data,content = form.content.data, author = current_user)
        newPost.create_post()
        flash('Your post has been published!', 'success')
        return redirect(url_for('main.home'))

    return render_template("create_post.html",title = "New Post", form = form , image=image , context="create")

@posts.route("/post/edit/<int:post_id>",methods=['GET','POST'])
@login_required
def edit_post(post_id):
    image = url_for('static',filename='images/profile_pictures/'+ current_user.image_file)
    post = Post.query.get_or_404(post_id)
    if(current_user != post.author):
        abort(403)
    form = CreatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == "GET" :
        form.title.data = post.title
        form.content.data = post.content
    return render_template("create_post.html",title = "Edit Post", form = form , context="edit", image = image)

@posts.route("/post/delete/<int:post_id>",methods=['GET','POST'])
@login_required
def delete_post(post_id):
    image = url_for('static',filename='images/profile_pictures/'+ current_user.image_file)
    post = Post.query.get_or_404(post_id)
    if(current_user != post.author):
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

