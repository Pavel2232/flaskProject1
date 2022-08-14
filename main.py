import json

from flask import Flask
import json
from flask_set import app
from models import User,Offer,Order
from utils import init_db, get_all


@app.route("/")
def user_page():
    return app.response_class(
        response= json.dumps(get_all(User),indent=4),
        status= 200,
        mimetype="application/json")

print(user_page)

if __name__ == "main":
    init_db()
    app.run()

