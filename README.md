# 2nd Degree Equation Solver

## Description
This Python script, **2nd degree equation solver.py**, is a robust tool designed to solve quadratic equations of the form $ax^2 + bx + c = 0$. It handles real-world mathematical edge cases, such as ensuring the leading coefficient $a$ is non-zero, and provides clean output for both real and complex roots.

## Features
* **Zero-Coefficient Validation**: Automatically prompts the user to re-enter `a` if it is set to 0 (which would make the equation linear rather than quadratic).
* **Discriminant Logic**: Uses the discriminant $\Delta = b^2 - 4ac$ to determine the nature of the roots.
* **Complex Number Support**: When $\Delta < 0$, the script calculates and formats complex solutions using the real and imaginary components.
* **Clean Formatting**: Uses the `:g` format specifier for floating-point numbers to remove unnecessary trailing zeros.

## Requirements
* **Python 3.x**
* **math module** (Standard library)

## How to Use
1. Run the script in your terminal or IDE:
   `python "2nd degree equation solver.py"`
2. Enter the three coefficients ($a$, $b$, and $c$) when prompted, separated by a space.
   *Example:* `2 -3 9`

## Mathematical Cases Handled
1. **$\Delta > 0$**: Two distinct real roots.
2. **$\Delta = 0$**: A single repeated real root ($x = -b / 2a$).
3. **$\Delta < 0$**: Two complex conjugate roots in the form $a \pm bi$.
