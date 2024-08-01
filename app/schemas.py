import re

from pydantic import BaseModel, Field, validator

class CreateUser(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8, max_length=20)

    @validator('name')
    def validate_name(cls, value):
        if not re.match('^[a-zA-Z0-9@]{1,50}$', value):
            raise ValueError('Username format invalid!')
        return value
