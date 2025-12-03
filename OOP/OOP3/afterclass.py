class Vehicle:
    def __init__(self, name, max_speed, mileage, seating_capacity=0):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity
class Bus(Vehicle):
    def fare(self):
        base_fare = self.seating_capacity * 100
        return base_fare * 1.10
bus = Bus("School Volvo", 180, 12, seating_capacity=50)
print("Vehicle Name:", bus.name)
print("Total Fare:", bus.fare())
australia_distances = {
    ('Sydney', 'Melbourne'): 878,
    ('Sydney', 'Brisbane'): 920,
    ('Sydney', 'Canberra'): 286,
    ('Canberra', 'Melbourne'): 662,
    ('Melbourne', 'Adelaide'): 726,
    ('Adelaide', 'Perth'): 2726,
    ('Perth', 'Darwin'): 4123,
    ('Adelaide', 'Darwin'): 3044,
    ('Hobart', 'Melbourne'): 652,
    ('Brisbane', 'Gold Coast'): 78,
    ('Cairns', 'Townsville'): 347,
    ('Townsville', 'Brisbane'): 1376,
    ('Cairns', 'Brisbane'): 1685,
}

def distance_between(a, b):
    if (a, b) in australia_distances:
        return australia_distances[(a, b)]
    if (b, a) in australia_distances:
        return australia_distances[(b, a)]
    return None
def route_distance(stops):
    total = 0
    missing = []
    for i in range(len(stops) - 1):
        d = distance_between(stops[i], stops[i + 1])
        if d is None:
            missing.append((stops[i], stops[i + 1]))
        else:
            total += d
    return total, missing
routes = {
    "Interstate run": ['Sydney', 'Canberra', 'Melbourne', 'Adelaide'],
    "Coastal run": ['Cairns', 'Townsville', 'Brisbane', 'Gold Coast'],
    "West-East crossing": ['Perth', 'Adelaide', 'Melbourne', 'Sydney'],
}
for name, stops in routes.items():
    total_km, missing_pairs = route_distance(stops)
    if missing_pairs:
        print(f"{name}: missing distances for {missing_pairs}")
    print(f"{name}: stops={stops} total_distance_km={total_km}")
a, b = "Sydney", "Melbourne"
print(f"Distance {a} <-> {b}:", distance_between(a, b), "km")