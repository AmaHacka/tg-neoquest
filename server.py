import json
import os
from flask import Flask, render_template

from database import select_all_names, Event

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello():
    return render_template("index.html", users=select_all_names())


@app.route("/api/<user_id>")
def get_user_events(user_id=None):
    events = [{"name": event.name, "time": event.time.strftime("%Y-%m-%d %H:%M:%S"), "status": event.status} for event
              in Event.select().where(Event.user_id == user_id)]
    return json.dumps(events)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
