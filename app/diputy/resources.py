from flask import request, Blueprint
from flask_restful import Api, Resource
from .schemas import DiputySchema
from .models import Diputy
from ..common.error_handling import ObjectNotFound

diputies_v1_bp = Blueprint('diputies_v1_bp', __name__)
diputy_schema = DiputySchema()

api = Api(diputies_v1_bp)

class DiputiesListResource(Resource):
    def get(self):
        diputies = Diputy.get_all()
        return diputy_schema.dump(diputies, many=True)

    def post(self):
        data = request.get_json()
        diputy_dict = diputy_schema.load(data)
        diputy = Diputy(name=diputy_dict['name'],
                    lastname=diputy_dict['lastname'],
                    birth_date=diputy_dict['birth_date'],
                    dni=diputy_dict['dni'],
                    sex=diputy_dict['sex']
        )
        diputy.save()
        return diputy_schema.dump(diputy), 201

class DiputyResource(Resource):
    def get(self, diputy_id):
        diputy = Diputy.get_by_id(diputy_id)
        if diputy is None:
            raise ObjectNotFound('Diputy dosnt exists')
        return diputy_schema.dump(diputy)

api.add_resource(DiputiesListResource, '/api/v1/diputies/', endpoint='diputies_list_resource')
api.add_resource(DiputyResource, '/api/v1/diputies/<int:diputy_id>', endpoint='diputy_resource')