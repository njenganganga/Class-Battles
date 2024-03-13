class circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def area(self):
         Area = self.pi * self.radius * self.radius
         print(f"Area= {Area}")

circle = circle (7, 22/7)
print(circle.radius)
print(circle.pi)
circle.area()

