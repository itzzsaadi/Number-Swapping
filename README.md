**Single-Line Number Swap in Python**
A clean Python demonstration of swapping two variables using a single line of code. This program leverages Python's walrus operator (:=) combined with arithmetic operations to exchange values between two variables without requiring a temporary variable.
Features:

Demonstrates the walrus operator (:=) introduced in Python 3.8
Performs variable swapping in one elegant line
Educational example of Python's assignment expressions

**How it works:**
The expression a = (a + b) - (b := a) simultaneously updates both variables by using the walrus operator to assign a's original value to b while calculating the new value for a.
