from models.normal_model import NormalModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas.normal_schema import NormalSchema


class NormalRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(NormalModel, NormalSchema)