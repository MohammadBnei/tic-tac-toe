from flask import Flask
from resources.movie import movies

app = Flask(__name__)

app.register_blueprint(movies)




app.run(host='0.0.0.0', port=3011)