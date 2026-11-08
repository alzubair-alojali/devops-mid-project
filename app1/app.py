import os

import redis
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# The Redis host is the Compose service name ("redis"), set through an env variable.
db = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)


@app.route("/")
def index():
    db.incr("visits")  # count every page load
    sent = request.args.get("sent") == "1"
    return render_template("index.html", sent=sent)


@app.route("/submit", methods=["POST"])
def submit():
    message = request.form.get("message", "").strip()
    if message:
        db.rpush("messages", message)  # append the message to the Redis list (the log)
    return redirect(url_for("index", sent=1))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
