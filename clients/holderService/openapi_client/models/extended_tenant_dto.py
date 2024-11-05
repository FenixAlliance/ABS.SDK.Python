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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.cart_dto import CartDto
from openapi_client.models.social_profile_dto import SocialProfileDto
from openapi_client.models.wallet_dto import WalletDto
from typing import Optional, Set
from typing_extensions import Self

class ExtendedTenantDto(BaseModel):
    """
    ExtendedTenantDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    qualified_name: Optional[StrictStr] = Field(default=None, alias="qualifiedName")
    tax_id: Optional[StrictStr] = Field(default=None, alias="taxId")
    about: Optional[StrictStr] = None
    wallet_id: Optional[StrictStr] = Field(default=None, alias="walletId")
    social_feed_id: Optional[StrictStr] = Field(default=None, alias="socialFeedId")
    business_industry_id: Optional[StrictStr] = Field(default=None, alias="businessIndustryId")
    business_segment_id: Optional[StrictStr] = Field(default=None, alias="businessSegmentId")
    social_profile_id: Optional[StrictStr] = Field(default=None, alias="socialProfileId")
    language_id: Optional[StrictStr] = Field(default=None, alias="languageId")
    name: Optional[StrictStr] = None
    duns: Optional[StrictStr] = None
    slogan: Optional[StrictStr] = None
    legal_name: Optional[StrictStr] = Field(default=None, alias="legalName")
    cover_url: Optional[StrictStr] = Field(default=None, alias="coverUrl")
    avatar_url: Optional[StrictStr] = Field(default=None, alias="avatarUrl")
    cart_id: Optional[StrictStr] = Field(default=None, alias="cartId")
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    timezone_id: Optional[StrictStr] = Field(default=None, alias="timezoneId")
    country_id: Optional[StrictStr] = Field(default=None, alias="countryId")
    state_id: Optional[StrictStr] = Field(default=None, alias="stateId")
    city_id: Optional[StrictStr] = Field(default=None, alias="cityId")
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    web_url: Optional[StrictStr] = Field(default=None, alias="webUrl")
    facebook_url: Optional[StrictStr] = Field(default=None, alias="facebookUrl")
    twitter_url: Optional[StrictStr] = Field(default=None, alias="twitterUrl")
    git_hub_url: Optional[StrictStr] = Field(default=None, alias="gitHubUrl")
    linked_in_url: Optional[StrictStr] = Field(default=None, alias="linkedInUrl")
    instagram_url: Optional[StrictStr] = Field(default=None, alias="instagramUrl")
    you_tube_url: Optional[StrictStr] = Field(default=None, alias="youTubeUrl")
    whats_app_number: Optional[StrictStr] = Field(default=None, alias="whatsAppNumber")
    support_phone_number: Optional[StrictStr] = Field(default=None, alias="supportPhoneNumber")
    verified: Optional[StrictBool] = None
    business_name: Optional[StrictStr] = Field(default=None, alias="businessName")
    business_legal_name: Optional[StrictStr] = Field(default=None, alias="businessLegalName")
    twitter_username: Optional[StrictStr] = Field(default=None, alias="twitterUsername")
    cart: Optional[CartDto] = None
    wallet: Optional[WalletDto] = None
    social_profile: Optional[SocialProfileDto] = Field(default=None, alias="socialProfile")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "qualifiedName", "taxId", "about", "walletId", "socialFeedId", "businessIndustryId", "businessSegmentId", "socialProfileId", "languageId", "name", "duns", "slogan", "legalName", "coverUrl", "avatarUrl", "cartId", "currencyId", "timezoneId", "countryId", "stateId", "cityId", "email", "phone", "webUrl", "facebookUrl", "twitterUrl", "gitHubUrl", "linkedInUrl", "instagramUrl", "youTubeUrl", "whatsAppNumber", "supportPhoneNumber", "verified", "businessName", "businessLegalName", "twitterUsername", "cart", "wallet", "socialProfile"]

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
        """Create an instance of ExtendedTenantDto from a JSON string"""
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
            "qualified_name",
            "business_name",
            "business_legal_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cart
        if self.cart:
            _dict['cart'] = self.cart.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wallet
        if self.wallet:
            _dict['wallet'] = self.wallet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of social_profile
        if self.social_profile:
            _dict['socialProfile'] = self.social_profile.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if qualified_name (nullable) is None
        # and model_fields_set contains the field
        if self.qualified_name is None and "qualified_name" in self.model_fields_set:
            _dict['qualifiedName'] = None

        # set to None if tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id is None and "tax_id" in self.model_fields_set:
            _dict['taxId'] = None

        # set to None if about (nullable) is None
        # and model_fields_set contains the field
        if self.about is None and "about" in self.model_fields_set:
            _dict['about'] = None

        # set to None if wallet_id (nullable) is None
        # and model_fields_set contains the field
        if self.wallet_id is None and "wallet_id" in self.model_fields_set:
            _dict['walletId'] = None

        # set to None if social_feed_id (nullable) is None
        # and model_fields_set contains the field
        if self.social_feed_id is None and "social_feed_id" in self.model_fields_set:
            _dict['socialFeedId'] = None

        # set to None if business_industry_id (nullable) is None
        # and model_fields_set contains the field
        if self.business_industry_id is None and "business_industry_id" in self.model_fields_set:
            _dict['businessIndustryId'] = None

        # set to None if business_segment_id (nullable) is None
        # and model_fields_set contains the field
        if self.business_segment_id is None and "business_segment_id" in self.model_fields_set:
            _dict['businessSegmentId'] = None

        # set to None if social_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.social_profile_id is None and "social_profile_id" in self.model_fields_set:
            _dict['socialProfileId'] = None

        # set to None if language_id (nullable) is None
        # and model_fields_set contains the field
        if self.language_id is None and "language_id" in self.model_fields_set:
            _dict['languageId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if duns (nullable) is None
        # and model_fields_set contains the field
        if self.duns is None and "duns" in self.model_fields_set:
            _dict['duns'] = None

        # set to None if slogan (nullable) is None
        # and model_fields_set contains the field
        if self.slogan is None and "slogan" in self.model_fields_set:
            _dict['slogan'] = None

        # set to None if legal_name (nullable) is None
        # and model_fields_set contains the field
        if self.legal_name is None and "legal_name" in self.model_fields_set:
            _dict['legalName'] = None

        # set to None if cover_url (nullable) is None
        # and model_fields_set contains the field
        if self.cover_url is None and "cover_url" in self.model_fields_set:
            _dict['coverUrl'] = None

        # set to None if avatar_url (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_url is None and "avatar_url" in self.model_fields_set:
            _dict['avatarUrl'] = None

        # set to None if cart_id (nullable) is None
        # and model_fields_set contains the field
        if self.cart_id is None and "cart_id" in self.model_fields_set:
            _dict['cartId'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if timezone_id (nullable) is None
        # and model_fields_set contains the field
        if self.timezone_id is None and "timezone_id" in self.model_fields_set:
            _dict['timezoneId'] = None

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

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if web_url (nullable) is None
        # and model_fields_set contains the field
        if self.web_url is None and "web_url" in self.model_fields_set:
            _dict['webUrl'] = None

        # set to None if facebook_url (nullable) is None
        # and model_fields_set contains the field
        if self.facebook_url is None and "facebook_url" in self.model_fields_set:
            _dict['facebookUrl'] = None

        # set to None if twitter_url (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_url is None and "twitter_url" in self.model_fields_set:
            _dict['twitterUrl'] = None

        # set to None if git_hub_url (nullable) is None
        # and model_fields_set contains the field
        if self.git_hub_url is None and "git_hub_url" in self.model_fields_set:
            _dict['gitHubUrl'] = None

        # set to None if linked_in_url (nullable) is None
        # and model_fields_set contains the field
        if self.linked_in_url is None and "linked_in_url" in self.model_fields_set:
            _dict['linkedInUrl'] = None

        # set to None if instagram_url (nullable) is None
        # and model_fields_set contains the field
        if self.instagram_url is None and "instagram_url" in self.model_fields_set:
            _dict['instagramUrl'] = None

        # set to None if you_tube_url (nullable) is None
        # and model_fields_set contains the field
        if self.you_tube_url is None and "you_tube_url" in self.model_fields_set:
            _dict['youTubeUrl'] = None

        # set to None if whats_app_number (nullable) is None
        # and model_fields_set contains the field
        if self.whats_app_number is None and "whats_app_number" in self.model_fields_set:
            _dict['whatsAppNumber'] = None

        # set to None if support_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.support_phone_number is None and "support_phone_number" in self.model_fields_set:
            _dict['supportPhoneNumber'] = None

        # set to None if business_name (nullable) is None
        # and model_fields_set contains the field
        if self.business_name is None and "business_name" in self.model_fields_set:
            _dict['businessName'] = None

        # set to None if business_legal_name (nullable) is None
        # and model_fields_set contains the field
        if self.business_legal_name is None and "business_legal_name" in self.model_fields_set:
            _dict['businessLegalName'] = None

        # set to None if twitter_username (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_username is None and "twitter_username" in self.model_fields_set:
            _dict['twitterUsername'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExtendedTenantDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "qualifiedName": obj.get("qualifiedName"),
            "taxId": obj.get("taxId"),
            "about": obj.get("about"),
            "walletId": obj.get("walletId"),
            "socialFeedId": obj.get("socialFeedId"),
            "businessIndustryId": obj.get("businessIndustryId"),
            "businessSegmentId": obj.get("businessSegmentId"),
            "socialProfileId": obj.get("socialProfileId"),
            "languageId": obj.get("languageId"),
            "name": obj.get("name"),
            "duns": obj.get("duns"),
            "slogan": obj.get("slogan"),
            "legalName": obj.get("legalName"),
            "coverUrl": obj.get("coverUrl"),
            "avatarUrl": obj.get("avatarUrl"),
            "cartId": obj.get("cartId"),
            "currencyId": obj.get("currencyId"),
            "timezoneId": obj.get("timezoneId"),
            "countryId": obj.get("countryId"),
            "stateId": obj.get("stateId"),
            "cityId": obj.get("cityId"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "webUrl": obj.get("webUrl"),
            "facebookUrl": obj.get("facebookUrl"),
            "twitterUrl": obj.get("twitterUrl"),
            "gitHubUrl": obj.get("gitHubUrl"),
            "linkedInUrl": obj.get("linkedInUrl"),
            "instagramUrl": obj.get("instagramUrl"),
            "youTubeUrl": obj.get("youTubeUrl"),
            "whatsAppNumber": obj.get("whatsAppNumber"),
            "supportPhoneNumber": obj.get("supportPhoneNumber"),
            "verified": obj.get("verified"),
            "businessName": obj.get("businessName"),
            "businessLegalName": obj.get("businessLegalName"),
            "twitterUsername": obj.get("twitterUsername"),
            "cart": CartDto.from_dict(obj["cart"]) if obj.get("cart") is not None else None,
            "wallet": WalletDto.from_dict(obj["wallet"]) if obj.get("wallet") is not None else None,
            "socialProfile": SocialProfileDto.from_dict(obj["socialProfile"]) if obj.get("socialProfile") is not None else None
        })
        return _obj


