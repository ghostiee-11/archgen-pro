from typing import List, Optional
from pydantic import BaseModel, Field

class TableSchema(BaseModel):
    table_name: str
    columns: List[str]
    description: Optional[str] = None

class APIEndpoint(BaseModel):
    method: str
    endpoint: str
    description: str
    request_body: Optional[dict] = None

class SystemSpec(BaseModel):
    modules: List[str]
    database_schema: List[TableSchema]
    apis: List[APIEndpoint]
    tech_stack: List[str]