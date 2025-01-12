from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()

tutorials = [
    {
        'tittle': 'Video1 ',
        'description': 'Get, post routes'
    },
    {
        'tiitle': 'Video2',
        'description': 'Put, Delete  routes'
    }
]

@app.route('/tutorials', methods = ['GET'])
def get_list():
    return jsonify(tutorials)

@app.route('/tutorials', methods = ['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)


if __name__ == '__name__':
    app.run()