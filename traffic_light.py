#traffic_light.py
class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.timer = 30  # default timer in seconds
        self.state = "RED"

    def adjust_timer(self, traffic_density):
        if traffic_density > 75:
            self.timer += 10  # extend green light
        elif traffic_density < 25:
            self.timer -= 10  # reduce green light
        self.timer = max(10, min(60, self.timer))  # keep timer within bounds

    def update_state(self):
        # Simple state machine for traffic lights
        if self.state == "RED":
            self.state = "GREEN"
        elif self.state == "GREEN":
            self.state = "YELLOW"
        elif self.state == "YELLOW":
            self.state = "RED"
        return self.state


# app.py
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


# style.css
body {
    font-family: Arial, sans-serif;
    background: url('https://images.unsplash.com/photo-1526579533021-34c5f36c4c85?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MXwyMDg4NDV8MHwxfGFsbHwxfHx8fHx8fHwxNjEzMTczMjY2&ixlib=rb-1.2.1&q=80&w=1080') no-repeat center center fixed;
    background-size: cover;
    color: #333;
    text-align: center;
    margin: 0;
    padding: 0;
}

h1 {
    color: #fff;
    margin: 20px 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

#traffic-light {
    background-color: rgba(255, 255, 255, 0.8);
    border: 2px solid #4CAF50;
    border-radius: 10px;
    padding: 20px;
    margin: 40px auto;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    width: 300px;
}

h2 {
    margin-bottom: 15px;
    color: #4CAF50;
}

p {
    font-size: 1.2em;
    margin: 10px 0;
}

form {
    margin-top: 20px;
}

input[type="number"] {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 60%;
    margin-bottom: 10px;
}

button {
    padding: 10px 15px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
}

button:hover {
    background-color: #45a049;
}

.footer {
    position: fixed;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    color: white;
}


# index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>Smart Traffic Management System</title>
</head>
<body>
    <h1>Smart Traffic Management System</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Traffic_light_on_St._Paul%27s_Square%2C_Liverpool.jpg/800px-Traffic_light_on_St._Paul%27s_Square%2C_Liverpool.jpg" alt="Traffic Light" style="width:300px; border-radius:10px; margin-top: 20px;">
    <div id="traffic-light">
        <h2>Traffic Light Status</h2>
        <div>
            <p>Light ID: <strong>{{ light.id }}</strong></p>
            <p>Current State: <strong>{{ light.state }}</strong></p>
            <p>Timer: <strong>{{ light.timer }} seconds</strong></p>
        </div>
        <form action="/" method="post">
            <label for="traffic_density">Traffic Density (0-100): </label>
            <input type="number" id="traffic_density" name="traffic_density" min="0" max="100" required>
            <br>
            <button type="submit">Adjust Traffic Light</button>
        </form>
    </div>
    <div class="footer">
        &copy; 2024 Smart Traffic Management System
    </div>
</body>
</html>
