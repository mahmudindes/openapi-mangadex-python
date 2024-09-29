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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ChapterAttributes(BaseModel):
    """
    ChapterAttributes
    """ # noqa: E501
    title: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    volume: Optional[StrictStr] = None
    chapter: Optional[Annotated[str, Field(strict=True, max_length=8)]] = None
    pages: Optional[StrictInt] = Field(default=None, description="Count of readable images for this chapter")
    translated_language: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="translatedLanguage")
    uploader: Optional[StrictStr] = None
    external_url: Optional[Annotated[str, Field(strict=True, max_length=512)]] = Field(default=None, description="Denotes a chapter that links to an external source.", alias="externalUrl")
    version: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    publish_at: Optional[StrictStr] = Field(default=None, alias="publishAt")
    readable_at: Optional[StrictStr] = Field(default=None, alias="readableAt")
    __properties: ClassVar[List[str]] = ["title", "volume", "chapter", "pages", "translatedLanguage", "uploader", "externalUrl", "version", "createdAt", "updatedAt", "publishAt", "readableAt"]

    @field_validator('translated_language')
    def translated_language_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-z]{2}(-[a-z]{2})?$", value):
            raise ValueError(r"must validate the regular expression /^[a-z]{2}(-[a-z]{2})?$/")
        return value

    @field_validator('external_url')
    def external_url_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^https?:\/\/", value):
            raise ValueError(r"must validate the regular expression /^https?:\/\//")
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
        """Create an instance of ChapterAttributes from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if volume (nullable) is None
        # and model_fields_set contains the field
        if self.volume is None and "volume" in self.model_fields_set:
            _dict['volume'] = None

        # set to None if chapter (nullable) is None
        # and model_fields_set contains the field
        if self.chapter is None and "chapter" in self.model_fields_set:
            _dict['chapter'] = None

        # set to None if external_url (nullable) is None
        # and model_fields_set contains the field
        if self.external_url is None and "external_url" in self.model_fields_set:
            _dict['externalUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChapterAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "volume": obj.get("volume"),
            "chapter": obj.get("chapter"),
            "pages": obj.get("pages"),
            "translatedLanguage": obj.get("translatedLanguage"),
            "uploader": obj.get("uploader"),
            "externalUrl": obj.get("externalUrl"),
            "version": obj.get("version"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "publishAt": obj.get("publishAt"),
            "readableAt": obj.get("readableAt")
        })
        return _obj


