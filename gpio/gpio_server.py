from flask import Flask, render_template, request
from gpiozero import LED

app = Flask(__name__)

# Set up GPIO pins using gpiozero
pins = {
    17: LED(17), 27: LED(27), 22: LED(22), 23: LED(23),
    24: LED(24), 25: LED(25), 5: LED(5), 6: LED(6)
}

# Initialize all pins to HIGH
for pin in pins.values():
    pin.on()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpio', methods=['POST'])
def control_gpio():
    state = request.form.get('state')
    pin = int(request.form.get('pin'))

    if state == 'off':
        pins[pin].on()
    elif state == 'on':
        pins[pin].off()

    return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

