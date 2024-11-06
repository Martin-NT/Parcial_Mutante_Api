from models.adn_model import DnaModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas.adn_schema import DnaSchema


class DnaRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(DnaModel, DnaSchema)