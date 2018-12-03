from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import json

db = SQLAlchemy()


class PDV(db.Model):

    __tablename__ = 'pdvs'

    id = db.Column(db.Integer, primary_key=True)
    tradingName = db.Column(db.String(128))
    ownerName = db.Column(db.String(128))
    document = db.Column(db.String(18), unique=True)
    coverageArea = db.Column(db.JSON)
    address = db.Column(db.JSON)

    def __init__(self, tradingName = None, ownerName = None, document = None, coverageArea = None, address = None):
        self.tradingName = tradingName
        self.ownerName = ownerName
        self.document = document
        self.coverageArea = coverageArea
        self.address = address

    def get_all(self):
        all_pdvs = PDV.query.all()
        return all_pdvs

    def get_one(self, id):
        specific_pdv = PDV.query.get(id)
        return specific_pdv

    def get_by_location(self, long, lat):
        SQL = text('SELECT * FROM pdvs WHERE JSON_CONTAINS(address, \'{"coordinates": ['+long+', '+lat+']}\')')
        result = db.engine.execute(SQL)

        located = []
        for row in result:
            item = {
                'id': row['id'],
                'tradingName': row['tradingName'],
                'ownerName': row['ownerName'],
                'document': row['document'],
                'coverageArea': row['coverageArea'],
                'address': row['address']
            }
            located.append(item)
        return located

    def insert(self, pdvs):
        inserted_ids = []
        for pdv in pdvs:
            pdv_item = PDV(pdv['tradingName'], pdv['ownerName'], pdv['document'], pdv['coverageArea'], pdv['address'])
            db.session.add(pdv_item)
            db.session.commit()

            inserted_ids.append(pdv_item.id)

        return inserted_ids
