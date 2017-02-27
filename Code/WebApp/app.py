from flask import Flask
from flask import render_template
from ECC import Curve, Point
from aritmetica import add_cartesian

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = 'Flask app'
    return render_template('index.html', name=name)


@app.route('/add')
def add_assoc_hardcoded_wrapper():
    curve = Curve(97, 3, a=2)
    point1 = Point(curve, [17, 10])
    point2 = Point(curve, [95, 31])
    return str(add_cartesian(point1, point2, curve))


@app.context_processor
def utility_processor():
    return dict(
        add_points=add_assoc_hardcoded_wrapper,
    )
