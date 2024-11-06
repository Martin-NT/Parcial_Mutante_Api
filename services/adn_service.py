from models.adn_model import DnaModel
from repositories.adn_repository import DnaRepository
from schemas.adn_schema import DnaSchema
from services.base_service_impl import BaseServiceImpl
from schemas.base_schema import BaseSchema
from services.adn_validator_service import DnaTester
import logging


class DnaService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=DnaRepository(), model=DnaModel, schema=DnaSchema)

    def save_dna(self, dna: list[str]) -> int:
        logger = logging.getLogger(__name__)
        logger.info(f"dna recibido para la creacion: {dna}")
        schema = self.schema(dna=dna)
        logger.info(f"esquema creado: {schema}")
        logger.info(f"to model: {self.to_model(schema)}")
        dna_model = self.repository.save(self.to_model(schema))
        logger.info(f"modelo: {dna_model}")
        return dna_model.id_key