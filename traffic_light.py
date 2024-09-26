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
