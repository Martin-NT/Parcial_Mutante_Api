from controllers.base_controller_impl import BaseControllerImpl
from schemas.normal_schema import NormalSchema
from services.normal_service import NormalService


class NormalController(BaseControllerImpl):

    def __init__(self):
        super().__init__(NormalSchema, NormalService())
