from models.mutant_model import MutantModel
from repositories.mutant_repository import MutantRepository
from schemas.mutant_schema import MutantSchema
from services.base_service_impl import BaseServiceImpl
import logging


class MutantService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=MutantRepository(), model=MutantModel, schema=MutantSchema)

    def save_mutant(self, dna_id: int) -> None:
        logger = logging.getLogger(__name__)
        logger.info(f"Este es el supuesto id: {dna_id}")
        schema = self.schema(dna_id=dna_id)
        self.repository.save(self.to_model(schema))