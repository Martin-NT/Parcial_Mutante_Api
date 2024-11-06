from models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class NormalModel(BaseModel):
    __tablename__ = 'normal'

    dna_id = Column(Integer, ForeignKey('dna.id_key'))
    dna = relationship("DnaModel", uselist=False)