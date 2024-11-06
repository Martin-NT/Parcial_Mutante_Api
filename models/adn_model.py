from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.ext.declarative import declared_attr

from models.base_model import BaseModel

class DnaModel(BaseModel):
    __tablename__ = 'dna'

    dna = Column(ARRAY(String))