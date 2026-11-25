# CSC 20 Calculator Assignments

This repository contains the two iterations of a calculator assignment for CSC 20.

## Iteration 1: Java calculator

The Java version is in the folder `CSC-20 Addition of Two Numbers Java/`. This was the first version of the assignment.

Although the original assignment was to add two numbers, this iteration was expanded into a basic calculator that can:

- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers

The Java project includes both a console version and a graphical version:

- `addition.java` — runs in the terminal
- `additionGUI.java` — runs as a Swing desktop application

### Run the Java terminal version

```bash
cd "CSC-20 Addition of Two Numbers Java"
javac addition.java
java addition
```

Enter two integers and then enter `add`, `subtract`, `multiply`, or `divide`.

### Run the Java GUI

```bash
cd "CSC-20 Addition of Two Numbers Java"
javac addition.java additionGUI.java
java additionGUI
```

## Iteration 2: Python calculator

The Python version is in the folder `CSC-20 Addition of Two Numbers Python/`. This iteration writes the calculator in Python and provides both a terminal program and a GUI.

The two files for this iteration are:

- `addition.py` — console calculator and reusable arithmetic functions
- `additionGUI.py` — Tkinter desktop calculator

Both Python files support addition, subtraction, multiplication, and division.

### Run the Python terminal version

```bash
cd "CSC-20 Addition of Two Numbers Python"
python3 addition.py
```

Enter two integers and choose `add`, `subtract`, `multiply`, or `divide`.

### Run the Python GUI

Tkinter must be available in the Python installation:

```bash
cd "CSC-20 Addition of Two Numbers Python"
python3 additionGUI.py
```

On macOS systems where `python3` does not include Tkinter, try:

```bash
/usr/bin/python3 additionGUI.py
```

Enter two integers, select an operation from the dropdown, and click **Calculate**.
