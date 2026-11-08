import os
import redis
from flask import Flask, render_template

app = Flask(__name__)
db = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)


@app.route("/")
def dashboard():
    total_messages = db.llen("messages")  # size of the list
    total_visits = int(db.get("visits") or 0)  # counter, 0 if App 1 never ran
    return render_template("index.html", total_messages=total_messages, total_visits=total_visits)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
