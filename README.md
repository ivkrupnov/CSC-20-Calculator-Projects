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
python -m pip install Flask
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser. Select an operation, enter two whole numbers, and click **Calculate**.

Press **Control + C** in the Terminal window running Flask to stop the server.

## Use the JSON API

With the Flask server running, send a `POST` request to `/api/add`. Include two whole numbers and an operation in the JSON body. The operation can be `add`, `subtract`, `multiply`, or `divide`.

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
