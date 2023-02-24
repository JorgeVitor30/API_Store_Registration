from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"     #CRIAR A TABELA
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = True, nullable=True) #NULLABLE P TER OBRIGATORIO NAME
    items = db.relationship("ItemModel", back_populates ="store", lazy="dynamic", cascade ="all, delete")
    tags = db.relationship("TagModel", back_populates="store", lazy = "dynamic")


# COMENTÁRIO SOBRE 'CASCADE': BASICAMENTE É PRA APAGAR AS CÉLULAS FILHAS CASO A QUE FOR APAGAR SEJA A MÃE
# EXEMPLO: SE APAGAR LOJA, OS ITENS SERÃO APAGADOS JUNTOS
