from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

astronauts = [
    "Ридли Скотт",
    "Энди Уир",
    "Марк Уотни",
    "Венката Капур",
    "Тедди Сандерс",
    "Шон Бин"
]


@app.route('/')
def index():
    return redirect(url_for('distribution'))


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)