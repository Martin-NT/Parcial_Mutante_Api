from models.normal_model import NormalModel
from repositories.normal_repository import NormalRepository
from schemas.normal_schema import NormalSchema
from services.base_service_impl import BaseServiceImpl


class NormalService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=NormalRepository(), model=NormalModel, schema=NormalSchema)

    def save_normal(self, dna_id: int):
        schema = self.schema(dna_id=dna_id)
        self.repository.save(self.to_model(schema))