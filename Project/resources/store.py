import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort


from schemas import StoreSchema

from db import db
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


blp = Blueprint("Stores", __name__, description="Operations on stores")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True)) 
    def get(self):
        return StoreModel.query.all()


    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            return {"message": "Store already exist"}, 400
        except SQLAlchemyError:
            return {"message": "Error ao criar a store"}, 500

        return store
    
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store
        
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)        #DELETAR
        db.session.commit()
        return {"message" : "Store deleted"}


