from flask import Blueprint
from flask import jsonify
from flask import request
from app.models import PDV

pdvs = Blueprint('pdvs', __name__)
PDV_obj = PDV()


@pdvs.route('/', methods=['GET'])
def index():
    pdvs = PDV_obj.get_all()

    data = []
    for pdv in pdvs:
        item = {
            'id': pdv.id,
            'tradingName': pdv.tradingName,
            'ownerName': pdv.ownerName,
            'document': pdv.document,
            'coverageArea': pdv.coverageArea,
            'address': pdv.address
        }
        data.append(item)

    return jsonify({'pdvs': [data]})


@pdvs.route('/<id_pdv>', methods=['GET'])
def one(id_pdv):
    pdv = PDV_obj.get_one(id_pdv)

    data = []
    if pdv:
        item = {
            'id': pdv.id,
            'tradingName': pdv.tradingName,
            'ownerName': pdv.ownerName,
            'document': pdv.document,
            'coverageArea': pdv.coverageArea,
            'address': pdv.address
        }
        data.append(item)

    return jsonify({'pdvs': [data]})


@pdvs.route('/location/<long>/<lat>', methods=['GET'])
def by_location(long, lat):
    located = PDV_obj.get_by_location(long, lat)
    return jsonify({'pdvs': [located]})


@pdvs.route('/new', methods=['POST'])
def save():
    json = request.get_json()
    inserted_pdv = PDV_obj.insert(json)
    return jsonify({'pdvs': [inserted_pdv]})