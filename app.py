from flask import Flask, render_template, request

app = Flask(__name__)

button_a_count = 0
button_b_count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global button_a_count, button_b_count
    if request.method == 'POST':
        if 'button_a' in request.form:
            button_a_count += 1
        elif 'button_b' in request.form:
            button_b_count += 1
    return render_template('index.html', button_a_count=button_a_count, button_b_count=button_b_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
