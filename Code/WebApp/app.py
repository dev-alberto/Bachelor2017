from flask import Flask
from flask import render_template, request

from WebApp.Wrappers.addition import AddWrapeer, DoubleWrapper, ScalarMulWrapper, JointMulWrapper

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = 'Flask app'
    return render_template('index.html', name=name)


@app.route('/arithmetic/add', methods=['POST'])
def add_wrapper():
    x1, y1, x2, y2, a, b, p, nist, bits = request.get_json()
    wrapper = AddWrapeer(int(x1), int(y1), int(x2), int(y2), a, b, p, nist=nist, bits=bits)
    return str(wrapper.add_wrapper())


@app.route('/arithmetic/double', methods=['POST'])
def double_wrapper():
    x, y, a, b, p, nist, bits = request.get_json()
    wrapper = DoubleWrapper(int(x), int(y), int(a), int(b), int(p), nist=nist, bits=int(bits))
    return str(wrapper.double_wrapper())


@app.route('/arithmetic/affine', methods=['POST'])
def affine_wrapper():
    x, y, a, b, p, nist, bits = request.get_json()
    wrapper = DoubleWrapper(int(x), int(y), int(a), int(b), int(p), nist=nist, bits=int(bits))
    return str(wrapper.transform_affine_wrapper())


@app.route('/arithmetic/mul', methods=['POST'])
def scalar_mul_wrapper():
    x, y, a, b, p, scalar, w, nist, bits = request.get_json()
    wrapper = ScalarMulWrapper(int(x), int(y), int(a), int(b), int(p), int(scalar), int(w), nist=nist, bits=int(bits))
    return str(wrapper.mul_wrapper())


@app.route('/arithmetic/joint', methods=['POST'])
def scalar_mul_wrapper():
    x1, y1, x2, y2, a, b, p, scalar1, scalar2, w1, w2, nist, bits = request.get_json()
    wrapper = JointMulWrapper(int(x1), int(y1), int(x2), int(y2), int(a), int(b),
                              int(p), int(scalar1), int(scalar2), int(w1), int(w2),
                              nist=nist, bits=int(bits))
    return str(wrapper.joint_mul_wrapper())
