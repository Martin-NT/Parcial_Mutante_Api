from controllers.base_controller_impl import BaseControllerImpl
from schemas.adn_schema import DnaSchema
from services.adn_service import DnaService
from services.mutant_service import MutantService
from services.normal_service import NormalService
import logging


class DnaController(BaseControllerImpl):

    def __init__(self):
        super().__init__(DnaSchema, DnaService())
        self.mutant_service = MutantService()
        self.normal_service = NormalService()

    def save_dna(self, dna: list[str], dna_type: str) -> None:
        logger = logging.getLogger(__name__)
        logger.info(f"Dna recibido: {dna} y tipo recibido: {dna_type}")
        ##dna_str = "-".join(dna)
        dna_id = self.service.save_dna(dna)
        logger.info(f"Id conseguido: {dna_id}")
        if dna_type == "mutant":
            self.mutant_service.save_mutant(dna_id=dna_id)
        else:
            self.normal_service.save_normal(dna_id=dna_id)