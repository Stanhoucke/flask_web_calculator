from app import app
from modules.calculator import Calculator

calculator = Calculator()

@app.route("/")
def index():
    return "Use the URL to perform calculator functions"

@app.route("/add/<number_1>,<number_2>")
def add(number_1, number_2):
    return f"The answer is: {calculator.add(number_1, number_2)}"

@app.route("/subtract/<number_1>,<number_2>")
def subtract(number_1, number_2):
    return f"The answer is: {calculator.subtract(number_1, number_2)}"

@app.route("/multiply/<number_1>,<number_2>")
def multiply(number_1, number_2):
    return f"The answer is: {calculator.multiply(number_1, number_2)}"

@app.route("/divide/<number_1>,<number_2>")
def divide(number_1, number_2):
    return f"The answer is: {calculator.divide(number_1, number_2)}"
