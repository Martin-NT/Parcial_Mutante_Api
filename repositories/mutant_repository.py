from models.mutant_model import MutantModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas.mutant_schema import MutantSchema


class MutantRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(MutantModel, MutantSchema)
