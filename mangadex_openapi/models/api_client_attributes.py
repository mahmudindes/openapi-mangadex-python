# coding: utf-8

"""
    MangaDex API

    MangaDex is an ad-free manga reader offering high-quality images!  This document details our API as it is right now. It is in no way a promise to never change it, although we will endeavour to publicly notify any major change.  # Acceptable use policy  Usage of our services implies acceptance of the following: - You **MUST** credit us - You **MUST** credit scanlation groups if you offer the ability to read chapters - You **CANNOT** run ads or paid services on your website and/or apps  These may change at any time for any and no reason and it is up to you check for updates from time to time.  # Security issues  If you believe you found a security issue in our API, please check our [security.txt](/security.txt) to get in touch privately. 

    The version of the OpenAPI document: 5.10.2
    Contact: support@mangadex.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ApiClientAttributes(BaseModel):
    """
    ApiClientAttributes
    """ # noqa: E501
    name: Optional[StrictStr] = None
    description: Optional[Annotated[str, Field(strict=True, max_length=256)]] = None
    profile: Optional[StrictStr] = None
    external_client_id: Optional[StrictStr] = Field(default=None, alias="externalClientId")
    is_active: Optional[StrictBool] = Field(default=None, alias="isActive")
    state: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    version: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    __properties: ClassVar[List[str]] = ["name", "description", "profile", "externalClientId", "isActive", "state", "createdAt", "updatedAt", "version"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['requested', 'approved', 'rejected', 'autoapproved']):
            raise ValueError("must be one of enum values ('requested', 'approved', 'rejected', 'autoapproved')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiClientAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if external_client_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_client_id is None and "external_client_id" in self.model_fields_set:
            _dict['externalClientId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiClientAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "profile": obj.get("profile"),
            "externalClientId": obj.get("externalClientId"),
            "isActive": obj.get("isActive"),
            "state": obj.get("state"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "version": obj.get("version")
        })
        return _obj


