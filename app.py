from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
def greet():
    return 'Hello'


@app.route('/f/<celsius_str>')
def convert_celsius_to_fahrenheit(celsius_str):
    try:
        celsius = float(celsius_str)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f'{fahrenheit:.2f}'
    except ValueError:
        return 'Invalid input. Please enter a valid Celsius temperature.'

if __name__ == '__main__':
    app.run()
