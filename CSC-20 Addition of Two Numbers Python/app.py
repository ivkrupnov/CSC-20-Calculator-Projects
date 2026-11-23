# Run these commands in Terminal to set up and start the Flask app:
# cd "/Users/ivankrupnov/Documents/CSC-20 All Projects for the Final Exam/CSC-20 Addition of Two Numbers Python"
# python3 -m venv .venv
# source .venv/bin/activate
# python -m pip install Flask
# python app.py
#
# Open the webpage in a browser:
# open http://127.0.0.1:5000
#
# Test the JSON API in a second Terminal window (operation can be add, subtract, multiply, or divide):
# curl -X POST http://127.0.0.1:5000/api/add -H "Content-Type: application/json" -d '{"number1": 7, "number2": 5, "operation": "subtract"}'
#
# Stop the server with Control+C in the Terminal window running Flask.

# This Flask app serves the calculator webpage and its JSON web service.
from flask import Flask, jsonify, render_template, request

# Share the same arithmetic functions with the other calculator programs.
from addition import add, divide, multiply, substract as subtract


# Create the Flask application.
app = Flask(__name__)


# Perform the requested operation using the shared calculator functions.
def calculate(number1, number2, operation):
    if operation == "add":
        return add(number1, number2)
    if operation == "subtract":
        return subtract(number1, number2)
    if operation == "multiply":
        return multiply(number1, number2)
    if operation == "divide":
        if number2 == 0:
            raise ZeroDivisionError
        return divide(number1, number2)
    raise ValueError("Choose add, subtract, multiply, or divide.")


@app.route("/", methods=["GET", "POST"])
def index():
    # Start with no result; a submitted form will set a result or an error message.
    result = ""

    if request.method == "POST":
        # Read the values submitted by the HTML form.
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        operation = request.form.get("operation", "add")

        if number1 is None or number1.strip() == "":
            result = "Please enter two numbers."
        elif number2 is None or number2.strip() == "":
            result = "Please enter two numbers."
        else:
            # Form values arrive as text, so convert them to integers first.
            try:
                number1 = int(number1)
                number2 = int(number2)
            except ValueError:
                result = "Please enter valid whole numbers."
            else:
                # Calculate only after both values have been validated.
                try:
                    result = str(calculate(number1, number2, operation))
                except ZeroDivisionError:
                    result = "Cannot divide by zero."
                except ValueError:
                    result = "Please choose a valid operation."

    # Render the HTML template and pass it the result to display.
    return render_template("index.html", result=result)


# Accept JSON requests at /api/add and return a JSON result or error.
@app.route("/api/add", methods=["POST"])
def api_add():
    # Parse the request body as JSON; invalid or missing JSON becomes None.
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(error="Send a JSON object with number1 and number2."), 400

    number1 = data.get("number1")
    number2 = data.get("number2")

    # Reject missing values, non-integers, and booleans.
    if (
        not isinstance(number1, int)
        or isinstance(number1, bool)
        or not isinstance(number2, int)
        or isinstance(number2, bool)
    ):
        return jsonify(error="number1 and number2 must be whole numbers."), 400

    # Keep older requests working by using addition when no operation is given.
    operation = data.get("operation", "add")
    if not isinstance(operation, str):
        return jsonify(error="operation must be add, subtract, multiply, or divide."), 400

    # Convert division-by-zero and unknown-operation cases into HTTP 400 errors.
    try:
        result = calculate(number1, number2, operation.lower())
    except ZeroDivisionError:
        return jsonify(error="Cannot divide by zero."), 400
    except ValueError:
        return jsonify(error="operation must be add, subtract, multiply, or divide."), 400

    return jsonify(result=result)


# Start the local development server when this file is run directly.
if __name__ == "__main__":
    app.run()
