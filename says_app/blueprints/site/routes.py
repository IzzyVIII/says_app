from flask import Blueprint, redirect, render_template, request
from says_app.models import Post, db
from says_app.service.quotes import QuotesService


#need to instantiate our Blueprint class
site = Blueprint('site', __name__, template_folder='site_templates' )


#use site object to create our routes

@site.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        post = Post(
                title=request.form["title"],
                description=request.form["description"]
            )
        db.session.add(post)
        db.session.commit()
                
    posts = Post.query.all()
    quote = QuotesService.get_quote()
    return render_template("app_home.html", posts=posts, quote=quote)

@site.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@site.route("/resources", methods=["GET", "POST"])
def resources():
    return render_template("resources.html")

@site.route("/events", methods=["GET", "POST"])
def events():
    return render_template("events.html")

@site.route("/post/delete/<id>")
def delete(id):
    post=Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return redirect("/")

# @site.route("/post", methods=["GET", "POST"]) #*******Put in BLUEPRINTS....... in routes???*******
# def post(id):
#     if request.method == "POST":
#         comment = Comment(
#             text=request.form["text"],
#             postId=request.form["postId"],
#             )
#         db.session.add(comment)
#         db.session.commit()
    
#         return render_template(.html) #******WHERE DO I PUT THIS*******