# coding: utf-8

"""
    CrmService

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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ContactCreateDto(BaseModel):
    """
    ContactCreateDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    tenant_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="tenantId")
    type: StrictInt
    first_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(alias="firstName")
    last_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, alias="lastName")
    email: Annotated[str, Field(min_length=1, strict=True)]
    tax_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, alias="taxId")
    primary_contact_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=36)]] = Field(default=None, alias="primaryContactId")
    qualified_name: Optional[StrictStr] = Field(default=None, alias="qualifiedName")
    about: Optional[Annotated[str, Field(strict=True, max_length=500)]] = None
    country_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=3)]] = Field(default=None, alias="countryId")
    state_id: Optional[StrictStr] = Field(default=None, alias="stateId")
    city_id: Optional[StrictStr] = Field(default=None, alias="cityId")
    mobile_phone: Optional[StrictStr] = Field(default=None, alias="mobilePhone")
    business_phone: Optional[StrictStr] = Field(default=None, alias="businessPhone")
    postal_code: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="postalCode")
    duns: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=9)]] = None
    job_title: Optional[StrictStr] = Field(default=None, alias="jobTitle")
    web_url: Optional[StrictStr] = Field(default=None, alias="webUrl")
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    language_id: Optional[StrictStr] = Field(default=None, alias="languageId")
    timezone_id: Optional[StrictStr] = Field(default=None, alias="timezoneId")
    birthday: Optional[datetime] = None
    street_line1: Optional[StrictStr] = Field(default=None, alias="streetLine1")
    street_line2: Optional[StrictStr] = Field(default=None, alias="streetLine2")
    git_hub_url: Optional[StrictStr] = Field(default=None, alias="gitHubUrl")
    twitch_url: Optional[StrictStr] = Field(default=None, alias="twitchUrl")
    reddit_url: Optional[StrictStr] = Field(default=None, alias="redditUrl")
    tik_tok_url: Optional[StrictStr] = Field(default=None, alias="tikTokUrl")
    website_url: Optional[StrictStr] = Field(default=None, alias="websiteUrl")
    twitter_url: Optional[StrictStr] = Field(default=None, alias="twitterUrl")
    facebook_url: Optional[StrictStr] = Field(default=None, alias="facebookUrl")
    you_tube_url: Optional[StrictStr] = Field(default=None, alias="youTubeUrl")
    linked_in_url: Optional[StrictStr] = Field(default=None, alias="linkedInUrl")
    instagram_url: Optional[StrictStr] = Field(default=None, alias="instagramUrl")
    github_username: Optional[StrictStr] = Field(default=None, alias="githubUsername")
    instagram_username: Optional[Any] = Field(default=None, alias="instagramUsername")
    tik_tok_username: Optional[Any] = Field(default=None, alias="tikTokUsername")
    stack_exchange_url: Optional[Any] = Field(default=None, alias="stackExchangeUrl")
    stack_overflow_url: Optional[Any] = Field(default=None, alias="stackOverflowUrl")
    parent_contact_id: Optional[Any] = Field(default=None, alias="parentContactId")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "tenantId", "type", "firstName", "lastName", "email", "taxId", "primaryContactId", "qualifiedName", "about", "countryId", "stateId", "cityId", "mobilePhone", "businessPhone", "postalCode", "duns", "jobTitle", "webUrl", "currencyId", "languageId", "timezoneId", "birthday", "streetLine1", "streetLine2", "gitHubUrl", "twitchUrl", "redditUrl", "tikTokUrl", "websiteUrl", "twitterUrl", "facebookUrl", "youTubeUrl", "linkedInUrl", "instagramUrl", "githubUsername", "instagramUsername", "tikTokUsername", "stackExchangeUrl", "stackOverflowUrl", "parentContactId"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('postal_code')
    def postal_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\w\s-]{3,10}$", value):
            raise ValueError(r"must validate the regular expression /^[\w\s-]{3,10}$/")
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
        """Create an instance of ContactCreateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "timestamp",
            "qualified_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id is None and "tax_id" in self.model_fields_set:
            _dict['taxId'] = None

        # set to None if primary_contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.primary_contact_id is None and "primary_contact_id" in self.model_fields_set:
            _dict['primaryContactId'] = None

        # set to None if qualified_name (nullable) is None
        # and model_fields_set contains the field
        if self.qualified_name is None and "qualified_name" in self.model_fields_set:
            _dict['qualifiedName'] = None

        # set to None if about (nullable) is None
        # and model_fields_set contains the field
        if self.about is None and "about" in self.model_fields_set:
            _dict['about'] = None

        # set to None if country_id (nullable) is None
        # and model_fields_set contains the field
        if self.country_id is None and "country_id" in self.model_fields_set:
            _dict['countryId'] = None

        # set to None if state_id (nullable) is None
        # and model_fields_set contains the field
        if self.state_id is None and "state_id" in self.model_fields_set:
            _dict['stateId'] = None

        # set to None if city_id (nullable) is None
        # and model_fields_set contains the field
        if self.city_id is None and "city_id" in self.model_fields_set:
            _dict['cityId'] = None

        # set to None if mobile_phone (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone is None and "mobile_phone" in self.model_fields_set:
            _dict['mobilePhone'] = None

        # set to None if business_phone (nullable) is None
        # and model_fields_set contains the field
        if self.business_phone is None and "business_phone" in self.model_fields_set:
            _dict['businessPhone'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postalCode'] = None

        # set to None if duns (nullable) is None
        # and model_fields_set contains the field
        if self.duns is None and "duns" in self.model_fields_set:
            _dict['duns'] = None

        # set to None if job_title (nullable) is None
        # and model_fields_set contains the field
        if self.job_title is None and "job_title" in self.model_fields_set:
            _dict['jobTitle'] = None

        # set to None if web_url (nullable) is None
        # and model_fields_set contains the field
        if self.web_url is None and "web_url" in self.model_fields_set:
            _dict['webUrl'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if language_id (nullable) is None
        # and model_fields_set contains the field
        if self.language_id is None and "language_id" in self.model_fields_set:
            _dict['languageId'] = None

        # set to None if timezone_id (nullable) is None
        # and model_fields_set contains the field
        if self.timezone_id is None and "timezone_id" in self.model_fields_set:
            _dict['timezoneId'] = None

        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        # set to None if street_line1 (nullable) is None
        # and model_fields_set contains the field
        if self.street_line1 is None and "street_line1" in self.model_fields_set:
            _dict['streetLine1'] = None

        # set to None if street_line2 (nullable) is None
        # and model_fields_set contains the field
        if self.street_line2 is None and "street_line2" in self.model_fields_set:
            _dict['streetLine2'] = None

        # set to None if git_hub_url (nullable) is None
        # and model_fields_set contains the field
        if self.git_hub_url is None and "git_hub_url" in self.model_fields_set:
            _dict['gitHubUrl'] = None

        # set to None if twitch_url (nullable) is None
        # and model_fields_set contains the field
        if self.twitch_url is None and "twitch_url" in self.model_fields_set:
            _dict['twitchUrl'] = None

        # set to None if reddit_url (nullable) is None
        # and model_fields_set contains the field
        if self.reddit_url is None and "reddit_url" in self.model_fields_set:
            _dict['redditUrl'] = None

        # set to None if tik_tok_url (nullable) is None
        # and model_fields_set contains the field
        if self.tik_tok_url is None and "tik_tok_url" in self.model_fields_set:
            _dict['tikTokUrl'] = None

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

        # set to None if github_username (nullable) is None
        # and model_fields_set contains the field
        if self.github_username is None and "github_username" in self.model_fields_set:
            _dict['githubUsername'] = None

        # set to None if instagram_username (nullable) is None
        # and model_fields_set contains the field
        if self.instagram_username is None and "instagram_username" in self.model_fields_set:
            _dict['instagramUsername'] = None

        # set to None if tik_tok_username (nullable) is None
        # and model_fields_set contains the field
        if self.tik_tok_username is None and "tik_tok_username" in self.model_fields_set:
            _dict['tikTokUsername'] = None

        # set to None if stack_exchange_url (nullable) is None
        # and model_fields_set contains the field
        if self.stack_exchange_url is None and "stack_exchange_url" in self.model_fields_set:
            _dict['stackExchangeUrl'] = None

        # set to None if stack_overflow_url (nullable) is None
        # and model_fields_set contains the field
        if self.stack_overflow_url is None and "stack_overflow_url" in self.model_fields_set:
            _dict['stackOverflowUrl'] = None

        # set to None if parent_contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_contact_id is None and "parent_contact_id" in self.model_fields_set:
            _dict['parentContactId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContactCreateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "tenantId": obj.get("tenantId"),
            "type": obj.get("type"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "email": obj.get("email"),
            "taxId": obj.get("taxId"),
            "primaryContactId": obj.get("primaryContactId"),
            "qualifiedName": obj.get("qualifiedName"),
            "about": obj.get("about"),
            "countryId": obj.get("countryId"),
            "stateId": obj.get("stateId"),
            "cityId": obj.get("cityId"),
            "mobilePhone": obj.get("mobilePhone"),
            "businessPhone": obj.get("businessPhone"),
            "postalCode": obj.get("postalCode"),
            "duns": obj.get("duns"),
            "jobTitle": obj.get("jobTitle"),
            "webUrl": obj.get("webUrl"),
            "currencyId": obj.get("currencyId"),
            "languageId": obj.get("languageId"),
            "timezoneId": obj.get("timezoneId"),
            "birthday": obj.get("birthday"),
            "streetLine1": obj.get("streetLine1"),
            "streetLine2": obj.get("streetLine2"),
            "gitHubUrl": obj.get("gitHubUrl"),
            "twitchUrl": obj.get("twitchUrl"),
            "redditUrl": obj.get("redditUrl"),
            "tikTokUrl": obj.get("tikTokUrl"),
            "websiteUrl": obj.get("websiteUrl"),
            "twitterUrl": obj.get("twitterUrl"),
            "facebookUrl": obj.get("facebookUrl"),
            "youTubeUrl": obj.get("youTubeUrl"),
            "linkedInUrl": obj.get("linkedInUrl"),
            "instagramUrl": obj.get("instagramUrl"),
            "githubUsername": obj.get("githubUsername"),
            "instagramUsername": obj.get("instagramUsername"),
            "tikTokUsername": obj.get("tikTokUsername"),
            "stackExchangeUrl": obj.get("stackExchangeUrl"),
            "stackOverflowUrl": obj.get("stackOverflowUrl"),
            "parentContactId": obj.get("parentContactId")
        })
        return _obj


