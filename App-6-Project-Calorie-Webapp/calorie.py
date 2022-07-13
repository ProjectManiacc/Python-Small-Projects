from wtforms import SubmitField, StringField

from temperature import Temperature


class Calorie:

    def __init__(self, weight, height, age,temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        return 10 * self.weight + 6.5 * self.height + 5 -self.temperature * 10


