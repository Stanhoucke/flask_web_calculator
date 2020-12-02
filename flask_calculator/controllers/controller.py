from app import app
from modules.calculator import Calculator

calculator = Calculator()

@app.route("/")
def index():
    return "Use the URL to perform calculator functions"

@app.route("/add/<number_1>,<number_2>")
def add(number_1, number_2):
    integer_1 = int(number_1)
    integer_2 = int(number_2)
    return f"The answer is: {calculator.add(integer_1, integer_2)}"