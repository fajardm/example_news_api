from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ping')
def get_hello():
    res = jsonify(status='success', data={'message': 'pong'})
    return res


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
