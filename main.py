import sympy as sp
import re

x = sp.Symbol('x')
C = sp.Symbol('C')

def preprocess_input(expr: str) -> str:
    expr = expr.replace('^', '**')
    expr = expr.replace('ln', 'log')
    expr = expr.replace('tg', 'tan')
    expr = expr.replace('ctg', '1/tan')
    expr = expr.replace('√', 'sqrt')

    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'(\))(\()', r'\1*\2', expr)
    expr = re.sub(r'(\))([a-zA-Z0-9])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z0-9])(\()', r'\1*\2', expr)

    return expr

user_input = input("Podaj funkcję do całkowania (względem x): ")

try:
    processed_input = preprocess_input(user_input)
    expression = sp.sympify(processed_input)

    integral = sp.integrate(expression, x)
    result = sp.Add(integral, C, evaluate=False)

    print(f"\nCałka nieoznaczona:")
    print(f"∫ {user_input} dx = ")
    sp.pprint(result, use_unicode=True)
    print("UWAGA")
    print("Stała C stoi za wyrażeniem, a nie przed")

except Exception as e:
    print("Wystąpił błąd podczas przetwarzania wzoru:", e)
