from models import colors

from flask import Flask, request as req, jsonify, g
from flask_cors import CORS

import errors

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def index():
    try:
        if req.method == 'GET':
            result = colors.get_all()
            return jsonify(result), 200

        elif req.method == 'PUT':
            params = req.get_json()

            if params is None:
                return errors.result(1, 400)

            if not all (i in params for i in ('name','hex')):
                return errors.result(2, 400)

            if len(params['name']) > 32:
                return errors.result(3, 400)

            if len(params['hex']) != 6:
                return errors.result(4, 400)

            last_row_id = colors.add(params['name'], params['hex'])
            if last_row_id is not None:
                return jsonify(color_id=last_row_id), 200
            else:
                raise Exception()

        elif req.method == 'PATCH':
            params = req.get_json()

            if params is None:
                return errors.result(1, 400)

            if not all (i in params for i in ('color_id', 'name','hex')):
                return errors.result(2, 400)

            if len(params['name']) > 32:
                return errors.result(3, 400)

            if len(params['hex']) != 6:
                return errors.result(14, 400)

            if colors.update(params['color_id'], params['name'], params['hex']) is 1:
                return {}, 200
            else:
                raise Exception()

        elif req.method == 'DELETE':
            params = req.get_json()

            if params is None:
                return errors.result(1, 400)

            if not 'color_id' in params:
                return errors.result(2, 400)

            if colors.delete(params['color_id']) is not None:
                return {}, 200
            else:
                raise Exception()
    except Exception as err:
        print(err)
        return {}, 500



@app.route('/search', methods=['POST'])
def search():
    try:
        params = req.get_json()

        if params is None:
            return errors.result(1, 400)

        if not 'query' in params:
            return errors.result(2, 400)

        result = colors.search(params['query'])
        if result is not None:
            return jsonify(result), 200
        else:
            raise Exception()
    except Exception as err:
        print(err)
        return {}, 500


@app.route('/ping', methods=['GET'])
def ping():
    return {}, 200
