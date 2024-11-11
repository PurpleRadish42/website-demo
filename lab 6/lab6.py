from flask import *

app = Flask(__name__)

@app.route('/input', methods=['GET'])
def input_number():
    return render_template('input.html')

@app.route('/result', methods=['GET'])
def result():
    number = request.args.get('number')
    if not number or not number.isdigit():
        return "Invalid input! Please enter a valid number."

    number = int(number)
    if number % 2 == 0:
        output = f"You entered an even number {number}."
    else:
        output = f"You entered an odd number {number}."
    return render_template('result.html', output=output)

@app.route('/readvalues', methods=['GET'])
def read_values():
    return render_template('readvalues.html')

@app.route('/calculator', methods=['POST'])
def calculator():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = f"{num1} + {num2} = {num1 + num2}"
        elif operation == 'subtract':
            result = f"{num1} - {num2} = {num1 - num2}"
        elif operation == 'multiply':
            result = f"{num1} * {num2} = {num1 * num2}"
        elif operation == 'divide':
            if num2 == 0:
                result = "Division by zero is not possible!"
            else:
                result = f"{num1} / {num2} = {num1 / num2}"
        else:
            result = "Invalid operation selected!"
            
    except ValueError:
        result = "Please enter valid numeric values!"
    
    return render_template('calculator.html', result=result)

app.run(debug=True)
