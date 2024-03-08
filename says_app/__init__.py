from flask import Flask, render_template
from flask_migrate import Migrate


from config import Config
from .blueprints.site.routes import site
from .models import login_manager, db
from .blueprints.auth.routes import auth
#from .blueprints.api.routes import api 

app=Flask(__name__)
app.config.from_object(Config)

login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in' 
login_manager.login_message = "You must first sign in!"
login_manager.login_message_category = 'warning'

#@app.route("/")
#def base():
#   return render_template('base.html')

app.register_blueprint(site)
app.register_blueprint(auth)
#app.register_blueprint(api)


db.init_app(app)
migrate = Migrate(app, db)