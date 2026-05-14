from pydantic import BaseModel
from datetime import datetime

class SuccessResponse(BaseModel):
    success: bool
    message: str

class ErrorResponse(BaseModel):
    detail: str
