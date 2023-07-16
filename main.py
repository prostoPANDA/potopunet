from flask import Flask, render_template, url_for, request, redirect
from bot import send_msg


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        send_msg(str(name))
        send_msg(str(phone))
        return redirect('/success')
    else:
        return render_template('form.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=False)
