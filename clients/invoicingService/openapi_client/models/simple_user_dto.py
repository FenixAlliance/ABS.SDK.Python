# coding: utf-8

"""
    InvoicingService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.1.4089
    Contact: support@fenix-alliance.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SimpleUserDto(BaseModel):
    """
    SimpleUserDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    qualified_name: Optional[StrictStr] = Field(default=None, alias="qualifiedName")
    public_name: Optional[StrictStr] = Field(default=None, alias="publicName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    cover_url: Optional[StrictStr] = Field(default=None, alias="coverUrl")
    avatar_url: Optional[StrictStr] = Field(default=None, alias="avatarUrl")
    git_hub_url: Optional[StrictStr] = Field(default=None, alias="gitHubUrl")
    country_id: Optional[StrictStr] = Field(default=None, alias="countryId")
    timezone_id: Optional[StrictStr] = Field(default=None, alias="timezoneId")
    website_url: Optional[StrictStr] = Field(default=None, alias="websiteUrl")
    twitter_url: Optional[StrictStr] = Field(default=None, alias="twitterUrl")
    you_tube_url: Optional[StrictStr] = Field(default=None, alias="youTubeUrl")
    linked_in_url: Optional[StrictStr] = Field(default=None, alias="linkedInUrl")
    facebook_url: Optional[StrictStr] = Field(default=None, alias="facebookUrl")
    instagram_url: Optional[StrictStr] = Field(default=None, alias="instagramUrl")
    social_profile_id: Optional[StrictStr] = Field(default=None, alias="socialProfileId")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "fullName", "qualifiedName", "publicName", "lastName", "firstName", "coverUrl", "avatarUrl", "gitHubUrl", "countryId", "timezoneId", "websiteUrl", "twitterUrl", "youTubeUrl", "linkedInUrl", "facebookUrl", "instagramUrl", "socialProfileId"]

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
        """Create an instance of SimpleUserDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "full_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if full_name (nullable) is None
        # and model_fields_set contains the field
        if self.full_name is None and "full_name" in self.model_fields_set:
            _dict['fullName'] = None

        # set to None if qualified_name (nullable) is None
        # and model_fields_set contains the field
        if self.qualified_name is None and "qualified_name" in self.model_fields_set:
            _dict['qualifiedName'] = None

        # set to None if public_name (nullable) is None
        # and model_fields_set contains the field
        if self.public_name is None and "public_name" in self.model_fields_set:
            _dict['publicName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if cover_url (nullable) is None
        # and model_fields_set contains the field
        if self.cover_url is None and "cover_url" in self.model_fields_set:
            _dict['coverUrl'] = None

        # set to None if avatar_url (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_url is None and "avatar_url" in self.model_fields_set:
            _dict['avatarUrl'] = None

        # set to None if git_hub_url (nullable) is None
        # and model_fields_set contains the field
        if self.git_hub_url is None and "git_hub_url" in self.model_fields_set:
            _dict['gitHubUrl'] = None

        # set to None if country_id (nullable) is None
        # and model_fields_set contains the field
        if self.country_id is None and "country_id" in self.model_fields_set:
            _dict['countryId'] = None

        # set to None if timezone_id (nullable) is None
        # and model_fields_set contains the field
        if self.timezone_id is None and "timezone_id" in self.model_fields_set:
            _dict['timezoneId'] = None

        # set to None if website_url (nullable) is None
        # and model_fields_set contains the field
        if self.website_url is None and "website_url" in self.model_fields_set:
            _dict['websiteUrl'] = None

        # set to None if twitter_url (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_url is None and "twitter_url" in self.model_fields_set:
            _dict['twitterUrl'] = None

        # set to None if you_tube_url (nullable) is None
        # and model_fields_set contains the field
        if self.you_tube_url is None and "you_tube_url" in self.model_fields_set:
            _dict['youTubeUrl'] = None

        # set to None if linked_in_url (nullable) is None
        # and model_fields_set contains the field
        if self.linked_in_url is None and "linked_in_url" in self.model_fields_set:
            _dict['linkedInUrl'] = None

        # set to None if facebook_url (nullable) is None
        # and model_fields_set contains the field
        if self.facebook_url is None and "facebook_url" in self.model_fields_set:
            _dict['facebookUrl'] = None

        # set to None if instagram_url (nullable) is None
        # and model_fields_set contains the field
        if self.instagram_url is None and "instagram_url" in self.model_fields_set:
            _dict['instagramUrl'] = None

        # set to None if social_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.social_profile_id is None and "social_profile_id" in self.model_fields_set:
            _dict['socialProfileId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SimpleUserDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "fullName": obj.get("fullName"),
            "qualifiedName": obj.get("qualifiedName"),
            "publicName": obj.get("publicName"),
            "lastName": obj.get("lastName"),
            "firstName": obj.get("firstName"),
            "coverUrl": obj.get("coverUrl"),
            "avatarUrl": obj.get("avatarUrl"),
            "gitHubUrl": obj.get("gitHubUrl"),
            "countryId": obj.get("countryId"),
            "timezoneId": obj.get("timezoneId"),
            "websiteUrl": obj.get("websiteUrl"),
            "twitterUrl": obj.get("twitterUrl"),
            "youTubeUrl": obj.get("youTubeUrl"),
            "linkedInUrl": obj.get("linkedInUrl"),
            "facebookUrl": obj.get("facebookUrl"),
            "instagramUrl": obj.get("instagramUrl"),
            "socialProfileId": obj.get("socialProfileId")
        })
        return _obj


