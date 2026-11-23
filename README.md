# CSC 20 Calculator Projects

This repository contains calculator projects written in Java and Python. The calculators can run in a terminal, in a desktop GUI, or as a Flask website with a JSON API.

## Project files

### Java

In `CSC-20 Addition of Two Numbers Java/`:

- `addition.java` is the terminal calculator.
- `additionGUI.java` is the Swing desktop calculator.

### Python

In `CSC-20 Addition of Two Numbers Python/`:

- `addition.py` contains the arithmetic functions and terminal calculator.
- `additionGUI.py` is the Tkinter desktop calculator.
- `app.py` runs the Flask website and JSON API.
- `requirements.txt` lists the Flask dependency.
- `templates/index.html` contains the Flask website form.

The calculators support addition, subtraction, multiplication, and whole-number division.

## Run the Java calculators

You need a Java Development Kit (JDK). In Terminal, go to the Java project folder:

```bash
cd "CSC-20 Addition of Two Numbers Java"
```

Run the terminal calculator:

```bash
javac addition.java
java addition
```

Compile and run the Swing desktop calculator:

```bash
javac addition.java additionGUI.java
java additionGUI
```

## Run the Python terminal calculator

From the repository root, run:

```bash
cd "CSC-20 Addition of Two Numbers Python"
python3 addition.py
```

## Run the Tkinter desktop calculator

Tkinter must be available in the Python interpreter you use. On the Mac used for this project, the system Python includes Tkinter:

```bash
cd "CSC-20 Addition of Two Numbers Python"
/usr/bin/python3 additionGUI.py
```

If your Python installation includes Tkinter, you can instead run `python3 additionGUI.py`.

## Run the Flask website

From the repository root, set up and start the Flask app:

```bash
cd "CSC-20 Addition of Two Numbers Python"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

The microservice status message is at [http://127.0.0.1:5000](http://127.0.0.1:5000), and the API test message is at [http://127.0.0.1:5000/test](http://127.0.0.1:5000/test). Open [http://127.0.0.1:5000/calculator](http://127.0.0.1:5000/calculator) to use the calculator webpage. Select an operation, enter two whole numbers, and click **Calculate**.

Press **Control + C** in the Terminal window running Flask to stop the server.

## Use the JSON API

With the Flask server running, the assignment's `/add` endpoint accepts either a GET request with `num1` and `num2` query parameters or a POST request with those fields in a JSON body. It returns both values and their sum as JSON:

```bash
curl "http://127.0.0.1:5000/add?num1=10&num2=20"
curl -X POST http://127.0.0.1:5000/add \
  -H "Content-Type: application/json" \
  -d '{"num1": 10, "num2": 20}'
```

Both requests return a JSON object with `num1`, `num2`, and `result`. This endpoint accepts decimal numbers and returns a JSON error with status 400 when either value is missing or invalid.

The calculator's `/api/add` endpoint supports all four operations. Include two whole numbers and an optional operation in the JSON body. The operation can be `add`, `subtract`, `multiply`, or `divide`.

For example, this subtracts 5 from 7:

```bash
curl -X POST http://127.0.0.1:5000/api/add \
  -H "Content-Type: application/json" \
  -d '{"number1": 7, "number2": 5, "operation": "subtract"}'
```

The response is:

```json
{"result":2}
```

If `operation` is omitted, the API defaults to addition. Missing or invalid values, unknown operations, and division by zero return a JSON error.

Division uses whole-number division and rounds toward zero for negative results.
