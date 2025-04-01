from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Mathematical Operations Web App</h1>
    <form method="POST" action="/calculate">
        <label>Select Operation:</label><br>
        <select name="operation">
            <option value="arith">Arithmetic</option>
            <option value="trig">Trigonometry</option>
            <option value="log">Logarithm</option>
            <option value="exp">Exponentiation</option>
            <option value="atrig">Inverse Trigonometry</option>
        </select><br><br>
        <input type="submit" value="Next">
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form['operation']
    if operation == 'arith':
        return '''
        <h2>Arithmetic</h2>
        <form method="POST" action="/result_arith">
            <label>Enter First Number:</label><br>
            <input type="number" name="num1"><br>
            <label>Enter Operator (+, -, *, /):</label><br>
            <input type="text" name="operator"><br>
            <label>Enter Second Number:</label><br>
            <input type="number" name="num2"><br>
            <input type="submit" value="Calculate">
        </form>
        '''
    elif operation == 'trig':
        return '''
        <h2>Trigonometry</h2>
        <form method="POST" action="/result_trig">
            <label>Select Function:</label><br>
            <select name="function">
                <option value="sin">sin</option>
                <option value="cos">cos</option>
                <option value="tan">tan</option>
                <option value="cosec">cosec</option>
                <option value="sec">sec</option>
                <option value="cot">cot</option>
                
            </select><br>
            <label>Enter Angle (in degrees):</label><br>
            <input type="number" name="angle"><br>
            <input type="submit" value="Calculate">
        </form>
        '''
    elif operation == 'log':
        return '''
        <h2>Logarithm</h2>
        <form method="POST" action="/result_log">
            <label>Enter Number:</label><br>
            <input type="number" name="num"><br>
            <label>Enter Base:</label><br>
            <input type="number" name="base"><br>
            <input type="submit" value="Calculate">
        </form>
        '''
    elif operation == 'exp':
        return '''
        <h2>Exponentiation</h2>
        <form method="POST" action="/result_exp">
            <label>Enter Base:</label><br>
            <input type="number" name="base"><br>
            <label>Enter Exponent:</label><br>
            <input type="number" name="exponent"><br>
            <input type="submit" value="Calculate">
        </form>
        '''
    elif operation == 'atrig':
        return '''
        <h2>Inverse Trigonometry</h2>
        <form method="POST" action="/result_atrig">
            <label>Select Function:</label><br>
            <select name="function">
                <option value="asin">asin</option>
                <option value="acos">acos</option>
                <option value="atan">atan</option>
                <option value="acosec">acosec</option>
                <option value="asec">asec</option>
                <option value="acot">acot</option>
                
            </select><br>
            <label>Enter value (in decimals):</label><br>
            <input type="number" name="angle"><br>
            <input type="submit" value="Calculate">
        </form>
        '''

@app.route('/result_arith', methods=['POST'])
def result_arith():
    num1 = float(request.form['num1'])
    operator = request.form['operator']
    num2 = float(request.form['num2'])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operator"
    return f"<h3>Result: {result}</h3>"

@app.route('/result_trig', methods=['POST'])
def result_trig():
    func = request.form['function']
    angle = float(request.form['angle'])
    radians = math.radians(angle)
    if func == 'sin':
        result = math.sin(radians)
    elif func == 'cos':
        result = math.cos(radians)
    elif func == 'tan':
        result = math.tan(radians)
    elif func == 'cosec':
        result =1/ math.sin(radians)
    elif func == 'sec':
        result =1/ math.cos(radians)
    elif func == 'cot':
        result = 1/math.tan(radians)
    else:
        result = "Invalid function"
    return f"<h3>Result: {result}</h3>"

@app.route('/result_log', methods=['POST'])
def result_log():
    num = float(request.form['num'])
    base = float(request.form['base'])
    if num > 0 and base > 0 and base != 1:
        result = math.log(num, base)
    else:
        result = "Error: Invalid input for logarithm"
    return f"<h3>Result: {result}</h3>"

@app.route('/result_exp', methods=['POST'])
def result_exp():
    base = float(request.form['base'])
    exponent = float(request.form['exponent'])
    result = base ** exponent
    return f"<h3>Result: {result}</h3>"
@app.route('/result_atrig', methods=['POST'])
def result_atrig():
    func = request.form['function']
    angle = float(request.form['angle'])
   # radians = math.radians(angle)
    if func == 'asin':
        result = math.asin(angle)
    elif func == 'acos':
        result = math.acos(angle)
    elif func == 'atan':
        result = math.atan(angle)
    elif func == 'acosec':
        result =1/ math.asin(angle)
    elif func == 'asec':
        result =1/ math.acos(angle)
    elif func == 'acot':
        result = 1/math.atan(angle)
    else:
        result = "Invalid function"
    #radians = math.radians(result)
    return f"<h3>Result: {result} radian</h3>"

if __name__ == "__main__":
    app.run(debug=True)