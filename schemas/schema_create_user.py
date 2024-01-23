# generated by datamodel-codegen:
#   filename:  schema_create_user.json
#   timestamp: 2024-01-23T17:20:58+00:00

from __future__ import annotations

from pydantic import BaseModel, Field, StrictInt, StrictStr


class User(BaseModel):
    field_id: StrictStr = Field(..., alias='_id')
    firstName: StrictStr
    lastName: StrictStr
    email: StrictStr
    field__v: StrictInt = Field(..., alias='__v')


class CreateUser(BaseModel):
    user: User
    token: StrictStr