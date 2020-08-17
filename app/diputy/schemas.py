from marshmallow import fields
from app.extensions import ma

class DiputySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    lastname = fields.String()
    birth_date = fields.DateTime()
    dni = fields.String()
    sex = fields.Integer()
