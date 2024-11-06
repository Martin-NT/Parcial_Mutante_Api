from schemas.base_schema import BaseSchema
from typing import List


class DnaSchema(BaseSchema):
    dna: List[str]