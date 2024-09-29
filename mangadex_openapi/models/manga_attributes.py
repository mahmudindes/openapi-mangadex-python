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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mangadex_openapi.models.tag import Tag
from typing import Optional, Set
from typing_extensions import Self

class MangaAttributes(BaseModel):
    """
    MangaAttributes
    """ # noqa: E501
    title: Optional[Dict[str, Annotated[str, Field(strict=True)]]] = None
    alt_titles: Optional[List[Dict[str, Annotated[str, Field(strict=True)]]]] = Field(default=None, alias="altTitles")
    description: Optional[Dict[str, Annotated[str, Field(strict=True)]]] = None
    is_locked: Optional[StrictBool] = Field(default=None, alias="isLocked")
    links: Optional[Dict[str, StrictStr]] = None
    original_language: Optional[StrictStr] = Field(default=None, alias="originalLanguage")
    last_volume: Optional[StrictStr] = Field(default=None, alias="lastVolume")
    last_chapter: Optional[StrictStr] = Field(default=None, alias="lastChapter")
    publication_demographic: Optional[StrictStr] = Field(default=None, alias="publicationDemographic")
    status: Optional[StrictStr] = None
    year: Optional[StrictInt] = Field(default=None, description="Year of release")
    content_rating: Optional[StrictStr] = Field(default=None, alias="contentRating")
    chapter_numbers_reset_on_new_volume: Optional[StrictBool] = Field(default=None, alias="chapterNumbersResetOnNewVolume")
    available_translated_languages: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, alias="availableTranslatedLanguages")
    latest_uploaded_chapter: Optional[StrictStr] = Field(default=None, alias="latestUploadedChapter")
    tags: Optional[List[Tag]] = None
    state: Optional[StrictStr] = None
    version: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["title", "altTitles", "description", "isLocked", "links", "originalLanguage", "lastVolume", "lastChapter", "publicationDemographic", "status", "year", "contentRating", "chapterNumbersResetOnNewVolume", "availableTranslatedLanguages", "latestUploadedChapter", "tags", "state", "version", "createdAt", "updatedAt"]

    @field_validator('publication_demographic')
    def publication_demographic_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['shounen', 'shoujo', 'josei', 'seinen']):
            raise ValueError("must be one of enum values ('shounen', 'shoujo', 'josei', 'seinen')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['completed', 'ongoing', 'cancelled', 'hiatus']):
            raise ValueError("must be one of enum values ('completed', 'ongoing', 'cancelled', 'hiatus')")
        return value

    @field_validator('content_rating')
    def content_rating_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['safe', 'suggestive', 'erotica', 'pornographic']):
            raise ValueError("must be one of enum values ('safe', 'suggestive', 'erotica', 'pornographic')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'submitted', 'published', 'rejected']):
            raise ValueError("must be one of enum values ('draft', 'submitted', 'published', 'rejected')")
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
        """Create an instance of MangaAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # set to None if last_volume (nullable) is None
        # and model_fields_set contains the field
        if self.last_volume is None and "last_volume" in self.model_fields_set:
            _dict['lastVolume'] = None

        # set to None if last_chapter (nullable) is None
        # and model_fields_set contains the field
        if self.last_chapter is None and "last_chapter" in self.model_fields_set:
            _dict['lastChapter'] = None

        # set to None if publication_demographic (nullable) is None
        # and model_fields_set contains the field
        if self.publication_demographic is None and "publication_demographic" in self.model_fields_set:
            _dict['publicationDemographic'] = None

        # set to None if year (nullable) is None
        # and model_fields_set contains the field
        if self.year is None and "year" in self.model_fields_set:
            _dict['year'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MangaAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "altTitles": obj.get("altTitles"),
            "description": obj.get("description"),
            "isLocked": obj.get("isLocked"),
            "links": obj.get("links"),
            "originalLanguage": obj.get("originalLanguage"),
            "lastVolume": obj.get("lastVolume"),
            "lastChapter": obj.get("lastChapter"),
            "publicationDemographic": obj.get("publicationDemographic"),
            "status": obj.get("status"),
            "year": obj.get("year"),
            "contentRating": obj.get("contentRating"),
            "chapterNumbersResetOnNewVolume": obj.get("chapterNumbersResetOnNewVolume"),
            "availableTranslatedLanguages": obj.get("availableTranslatedLanguages"),
            "latestUploadedChapter": obj.get("latestUploadedChapter"),
            "tags": [Tag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "state": obj.get("state"),
            "version": obj.get("version"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


