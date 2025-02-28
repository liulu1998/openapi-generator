# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class User(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    User - a model defined in OpenAPI

        id: The id of this User [Optional].
        username: The username of this User [Optional].
        first_name: The first_name of this User [Optional].
        last_name: The last_name of this User [Optional].
        email: The email of this User [Optional].
        password: The password of this User [Optional].
        phone: The phone of this User [Optional].
        user_status: The user_status of this User [Optional].
    """

    id: Optional[int] = Field(alias="id", default=None)
    username: Optional[str] = Field(alias="username", default=None)
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    email: Optional[str] = Field(alias="email", default=None)
    password: Optional[str] = Field(alias="password", default=None)
    phone: Optional[str] = Field(alias="phone", default=None)
    user_status: Optional[int] = Field(alias="userStatus", default=None)


User.update_forward_refs()
