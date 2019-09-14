from models import colors

from flask import Flask, request as req, jsonify, g
app = Flask(__name__)


@app.route('/', methods=['GET', 'PUT', 'DELETE'])
def index():
    try:
        if req.method == 'GET':
            result = colors.get_all()
            return jsonify(result), 200

        elif req.method == 'PUT':
            params = req.get_json()

            if params is None:
                return { "error": "empty parameters" }, 400

            if not all (i in params for i in ('name','hex')):
                return { "error": "must provide name and hex" }, 400

            if len(params['name']) > 32:
                return { "error": "name too long, max length 32 characters" }, 400

            if len(params['hex']) != 6:
                return { "error": "hex must 6 characters" }, 400

            last_row_id = colors.add(params['name'], params['hex'])
            return jsonify(color_id=last_row_id), 200

        elif req.method == 'DELETE':
            params = req.get_json()

            if params is None:
                return { "error": "empty parameters" }, 400

            if not 'color_id' in params:
                return { "error": "must provide color_id" }, 400

            colors.delete(params['color_id'])
            return {}, 200
    except Exception as err:
        print(err)
        return {}, 500



@app.route('/search', methods=['POST'])
def search():
    try:
        params = req.get_json()

        if params is None:
            return { "error": "empty parameters" }, 400

        if not 'query' in params:
            return { "error": "must provide query" }, 400

        result = colors.search(params['query'])
        return jsonify(result), 200
    except Exception as err:
        print(err)
        return {}, 500
