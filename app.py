from flask import Flask, render_template, request
from traffic_light import TrafficLight

app = Flask(__name__)
light = TrafficLight(1)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        traffic_density = int(request.form["traffic_density"])
        light.adjust_timer(traffic_density)
        light.update_state()
    return render_template("index.html", light=light)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
