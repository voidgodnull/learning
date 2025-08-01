class Workout:
    def __init__(self, start, end, calories):
        self.start = start
        self.end = end
        self.calories = calories
        self.kind = "workout"

    def get_calories(self):
        return self.calories

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_calories(self, calories):
        self.calories = calories

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def __str__(self):
        return f"{self.kind.capitalize()}({self.start} to {self.end}, {self.calories} calories burned)"


class Running(Workout):
    def __init__(self, start, end, calories, distance):
        super().__init__(start, end, calories)
        self.distance = distance  # in kilometers
        self.kind = "running"

    def get_distance(self):
        return self.distance

    def __str__(self):
        return f"Running({self.start} to {self.end}, {self.calories} calories, {self.distance} km)"


class Cycling(Workout):
    def __init__(self, start, end, calories, terrain):
        super().__init__(start, end, calories)
        self.terrain = terrain  # e.g., 'road', 'mountain'
        self.kind = "cycling"

    def get_terrain(self):
        return self.terrain

    def __str__(self):
        return f"Cycling({self.start} to {self.end}, {self.calories} calories, terrain: {self.terrain})"


class Yoga(Workout):
    def __init__(self, start, end, calories, level):
        super().__init__(start, end, calories)
        self.level = level  # e.g., 'beginner', 'intermediate', 'advanced'
        self.kind = "yoga"

    def get_level(self):
        return self.level

    def __str__(self):
        return f"Yoga({self.start} to {self.end}, {self.calories} calories, level: {self.level})"


# Example usage
run = Running("06:00 AM", "06:45 AM", 400, 5)
cycle = Cycling("07:00 AM", "08:00 AM", 500, "road")
yoga = Yoga("09:00 AM", "09:30 AM", 200, "beginner")

print(run)
print(cycle)
print(yoga)
