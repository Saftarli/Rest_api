from flask import Flask, jsonify, request
from run import app







tutorials = [
    {
        'id': 1,
        'tittle': 'Video1 ',
        'description': 'Get, post routes'
    },
    {
        'id': 2,
        'tiitle': 'Video2',
        'description': 'Put, Delete  routes'
    }
]

@app.route('/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)

@app.route('/tutorials', methods=['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials), 201

@app.route('/tutorials/<int:tutorial_id>', methods=['PUT'])
def update_tutorial(tutorial_id):
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    if not item:
        return {'message': 'No tutorials with this ID'}, 404
    params = request.json
    item.update(params)
    return jsonify(item)

@app.route('/tutorials/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    idx, item = next((i, x) for i, x in enumerate(tutorials) if x[1]['id'] == tutorial_id), (None, None)
    if idx is None:
        return {'message': 'No tutorials with this ID'}, 404
    tutorials.pop(idx)
    return '', 204




