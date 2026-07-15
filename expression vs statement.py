"""
Question 08: Expression vs Statement Identification - ADVANCED-INTERMEDIATE

Neeche diye gaye do code snippets ko dekhein:
Snippet A: x - 8
Snippet B: x = 10

In dono mein se kaunsa "Expression" hai aur kaunsa "Statement" hai?
Dono ke darmiyan operators aur operands ka farq samjhayein.
"""

x = 10

# --- Snippet A: an EXPRESSION ---
# "x - 8" is an EXPRESSION because it computes/produces a VALUE
# (10 - 8 = 2), but it does not, by itself, DO anything or store
# anything anywhere -- the result is just discarded here unless we
# use it (e.g. print it or assign it).
result_of_expression = x - 8   # here we capture the expression's value
print("Snippet A (expression) result:", result_of_expression)

# --- Snippet B: a STATEMENT ---
# "x = 10" is a STATEMENT (specifically, an assignment statement).
# It performs an ACTION: it binds the name 'x' to the value 10 in
# memory. A statement does not itself "return" a usable value the
# way an expression does -- its job is to carry out an instruction.
x = 10
print("Snippet B (statement) -> x is now:", x)

"""
EXPLANATION:
- EXPRESSION: any combination of values, variables, and OPERATORS
  (like -, +, *, /) that evaluates down to a single VALUE.
  Example: x - 8       -> operator: '-'   | operands: x, 8
  Expressions can be used inside other code, e.g. print(x - 8),
  or stored: y = x - 8.

- STATEMENT: a complete instruction/line of code that performs an
  action -- Python EXECUTES a statement, it doesn't just "evaluate"
  it to a value. Assignment (x = 10), if-statements, for-loops, and
  function definitions are all statements.

- Key difference: expressions produce values you can use elsewhere;
  statements perform actions/instructions and don't produce a reusable
  value themselves. Also, every expression CAN be part of a statement
  (e.g. "x = <expression>"), but not every statement is an expression
  (you can't do y = (x = 10) in Python -- that's a SyntaxError, because
  assignment is a statement, not an expression, in standard Python).
"""
