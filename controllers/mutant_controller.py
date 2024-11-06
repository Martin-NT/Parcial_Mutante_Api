from controllers.base_controller_impl import BaseControllerImpl
from schemas.mutant_schema import MutantSchema
from services.mutant_service import MutantService


class MutantController(BaseControllerImpl):

    def __init__(self):
        super().__init__(MutantSchema, MutantService())
