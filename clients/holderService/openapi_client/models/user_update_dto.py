# coding: utf-8

"""
    HolderService

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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserUpdateDto(BaseModel):
    """
    UserUpdateDto
    """ # noqa: E501
    birthday: Optional[datetime] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    public_name: Optional[StrictStr] = Field(default=None, alias="publicName")
    id_provider: Optional[StrictStr] = Field(default=None, alias="idProvider")
    language_id: Optional[StrictStr] = Field(default=None, alias="languageId")
    timezone_id: Optional[StrictStr] = Field(default=None, alias="timezoneId")
    gender: Optional[StrictStr] = None
    city_id: Optional[StrictStr] = Field(default=None, alias="cityId")
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    status: Optional[StrictStr] = None
    state_id: Optional[StrictStr] = Field(default=None, alias="stateId")
    about: Optional[StrictStr] = None
    web_url: Optional[StrictStr] = Field(default=None, alias="webUrl")
    job_title: Optional[StrictStr] = Field(default=None, alias="jobTitle")
    cover_url: Optional[StrictStr] = Field(default=None, alias="coverUrl")
    avatar_url: Optional[StrictStr] = Field(default=None, alias="avatarUrl")
    git_hub_url: Optional[StrictStr] = Field(default=None, alias="gitHubUrl")
    website_url: Optional[StrictStr] = Field(default=None, alias="websiteUrl")
    twitter_url: Optional[StrictStr] = Field(default=None, alias="twitterUrl")
    facebook_url: Optional[StrictStr] = Field(default=None, alias="facebookUrl")
    you_tube_url: Optional[StrictStr] = Field(default=None, alias="youTubeUrl")
    linked_in_url: Optional[StrictStr] = Field(default=None, alias="linkedInUrl")
    instagram_url: Optional[StrictStr] = Field(default=None, alias="instagramUrl")
    country_id: Optional[StrictStr] = Field(default=None, alias="countryId")
    github_username: Optional[StrictStr] = Field(default=None, alias="githubUsername")
    availability: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["birthday", "firstName", "lastName", "publicName", "idProvider", "languageId", "timezoneId", "gender", "cityId", "currencyId", "status", "stateId", "about", "webUrl", "jobTitle", "coverUrl", "avatarUrl", "gitHubUrl", "websiteUrl", "twitterUrl", "facebookUrl", "youTubeUrl", "linkedInUrl", "instagramUrl", "countryId", "githubUsername", "availability"]

    @field_validator('availability')
    def availability_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2, 3, 4]):
            raise ValueError("must be one of enum values (0, 1, 2, 3, 4)")
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
        """Create an instance of UserUpdateDto from a JSON string"""
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
        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if public_name (nullable) is None
        # and model_fields_set contains the field
        if self.public_name is None and "public_name" in self.model_fields_set:
            _dict['publicName'] = None

        # set to None if id_provider (nullable) is None
        # and model_fields_set contains the field
        if self.id_provider is None and "id_provider" in self.model_fields_set:
            _dict['idProvider'] = None

        # set to None if language_id (nullable) is None
        # and model_fields_set contains the field
        if self.language_id is None and "language_id" in self.model_fields_set:
            _dict['languageId'] = None

        # set to None if timezone_id (nullable) is None
        # and model_fields_set contains the field
        if self.timezone_id is None and "timezone_id" in self.model_fields_set:
            _dict['timezoneId'] = None

        # set to None if gender (nullable) is None
        # and model_fields_set contains the field
        if self.gender is None and "gender" in self.model_fields_set:
            _dict['gender'] = None

        # set to None if city_id (nullable) is None
        # and model_fields_set contains the field
        if self.city_id is None and "city_id" in self.model_fields_set:
            _dict['cityId'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if state_id (nullable) is None
        # and model_fields_set contains the field
        if self.state_id is None and "state_id" in self.model_fields_set:
            _dict['stateId'] = None

        # set to None if about (nullable) is None
        # and model_fields_set contains the field
        if self.about is None and "about" in self.model_fields_set:
            _dict['about'] = None

        # set to None if web_url (nullable) is None
        # and model_fields_set contains the field
        if self.web_url is None and "web_url" in self.model_fields_set:
            _dict['webUrl'] = None

        # set to None if job_title (nullable) is None
        # and model_fields_set contains the field
        if self.job_title is None and "job_title" in self.model_fields_set:
            _dict['jobTitle'] = None

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

        # set to None if website_url (nullable) is None
        # and model_fields_set contains the field
        if self.website_url is None and "website_url" in self.model_fields_set:
            _dict['websiteUrl'] = None

        # set to None if twitter_url (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_url is None and "twitter_url" in self.model_fields_set:
            _dict['twitterUrl'] = None

        # set to None if facebook_url (nullable) is None
        # and model_fields_set contains the field
        if self.facebook_url is None and "facebook_url" in self.model_fields_set:
            _dict['facebookUrl'] = None

        # set to None if you_tube_url (nullable) is None
        # and model_fields_set contains the field
        if self.you_tube_url is None and "you_tube_url" in self.model_fields_set:
            _dict['youTubeUrl'] = None

        # set to None if linked_in_url (nullable) is None
        # and model_fields_set contains the field
        if self.linked_in_url is None and "linked_in_url" in self.model_fields_set:
            _dict['linkedInUrl'] = None

        # set to None if instagram_url (nullable) is None
        # and model_fields_set contains the field
        if self.instagram_url is None and "instagram_url" in self.model_fields_set:
            _dict['instagramUrl'] = None

        # set to None if country_id (nullable) is None
        # and model_fields_set contains the field
        if self.country_id is None and "country_id" in self.model_fields_set:
            _dict['countryId'] = None

        # set to None if github_username (nullable) is None
        # and model_fields_set contains the field
        if self.github_username is None and "github_username" in self.model_fields_set:
            _dict['githubUsername'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserUpdateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "birthday": obj.get("birthday"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "publicName": obj.get("publicName"),
            "idProvider": obj.get("idProvider"),
            "languageId": obj.get("languageId"),
            "timezoneId": obj.get("timezoneId"),
            "gender": obj.get("gender"),
            "cityId": obj.get("cityId"),
            "currencyId": obj.get("currencyId"),
            "status": obj.get("status"),
            "stateId": obj.get("stateId"),
            "about": obj.get("about"),
            "webUrl": obj.get("webUrl"),
            "jobTitle": obj.get("jobTitle"),
            "coverUrl": obj.get("coverUrl"),
            "avatarUrl": obj.get("avatarUrl"),
            "gitHubUrl": obj.get("gitHubUrl"),
            "websiteUrl": obj.get("websiteUrl"),
            "twitterUrl": obj.get("twitterUrl"),
            "facebookUrl": obj.get("facebookUrl"),
            "youTubeUrl": obj.get("youTubeUrl"),
            "linkedInUrl": obj.get("linkedInUrl"),
            "instagramUrl": obj.get("instagramUrl"),
            "countryId": obj.get("countryId"),
            "githubUsername": obj.get("githubUsername"),
            "availability": obj.get("availability")
        })
        return _obj


