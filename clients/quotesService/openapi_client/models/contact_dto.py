# coding: utf-8

"""
    QuotesService

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

class ContactDto(BaseModel):
    """
    ContactDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    qualified_name: Optional[StrictStr] = Field(default=None, alias="qualifiedName")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    type: Optional[StrictInt] = None
    public_name: Optional[StrictStr] = Field(default=None, alias="publicName")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    job_title: Optional[StrictStr] = Field(default=None, alias="jobTitle")
    cover_url: Optional[StrictStr] = Field(default=None, alias="coverUrl")
    avatar_url: Optional[StrictStr] = Field(default=None, alias="avatarUrl")
    country_id: Optional[StrictStr] = Field(default=None, alias="countryId")
    timezone_id: Optional[StrictStr] = Field(default=None, alias="timezoneId")
    language_id: Optional[StrictStr] = Field(default=None, alias="languageId")
    social_profile_id: Optional[StrictStr] = Field(default=None, alias="socialProfileId")
    web_url: Optional[StrictStr] = Field(default=None, alias="webUrl")
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
    duns: Optional[StrictStr] = None
    tax_id: Optional[StrictStr] = Field(default=None, alias="taxId")
    email: Optional[StrictStr] = None
    about: Optional[StrictStr] = None
    street: Optional[StrictStr] = None
    cart_id: Optional[StrictStr] = Field(default=None, alias="cartId")
    city_id: Optional[StrictStr] = Field(default=None, alias="cityId")
    zip_code: Optional[StrictStr] = Field(default=None, alias="zipCode")
    state_id: Optional[StrictStr] = Field(default=None, alias="stateId")
    wallet_id: Optional[StrictStr] = Field(default=None, alias="walletId")
    fax_number: Optional[StrictStr] = Field(default=None, alias="faxNumber")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    street_line1: Optional[StrictStr] = Field(default=None, alias="streetLine1")
    street_line2: Optional[StrictStr] = Field(default=None, alias="streetLine2")
    territory_id: Optional[StrictStr] = Field(default=None, alias="territoryId")
    mobile_phone: Optional[StrictStr] = Field(default=None, alias="mobilePhone")
    enrollment_id: Optional[StrictStr] = Field(default=None, alias="enrollmentId")
    annual_revenue: Optional[StrictStr] = Field(default=None, alias="annualRevenue")
    related_user_id: Optional[StrictStr] = Field(default=None, alias="relatedUserId")
    business_phone: Optional[StrictStr] = Field(default=None, alias="businessPhone")
    owner_contact_id: Optional[StrictStr] = Field(default=None, alias="ownerContactId")
    related_tenant_id: Optional[StrictStr] = Field(default=None, alias="relatedTenantId")
    activity_feed_id: Optional[StrictStr] = Field(default=None, alias="activityFeedId")
    parent_contact_id: Optional[StrictStr] = Field(default=None, alias="parentContactId")
    identity_provider: Optional[StrictStr] = Field(default=None, alias="identityProvider")
    partner_profile_id: Optional[StrictStr] = Field(default=None, alias="partnerProfileId")
    primary_contact_id: Optional[StrictStr] = Field(default=None, alias="primaryContactId")
    active_directory_id: Optional[StrictStr] = Field(default=None, alias="activeDirectoryId")
    identity_provider_access_token: Optional[StrictStr] = Field(default=None, alias="identityProviderAccessToken")
    birthday: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "timestamp", "qualifiedName", "tenantId", "type", "publicName", "firstName", "lastName", "jobTitle", "coverUrl", "avatarUrl", "countryId", "timezoneId", "languageId", "socialProfileId", "webUrl", "gitHubUrl", "twitchUrl", "redditUrl", "tikTokUrl", "websiteUrl", "twitterUrl", "facebookUrl", "youTubeUrl", "linkedInUrl", "instagramUrl", "githubUsername", "duns", "taxId", "email", "about", "street", "cartId", "cityId", "zipCode", "stateId", "walletId", "faxNumber", "postalCode", "currencyId", "streetLine1", "streetLine2", "territoryId", "mobilePhone", "enrollmentId", "annualRevenue", "relatedUserId", "businessPhone", "ownerContactId", "relatedTenantId", "activityFeedId", "parentContactId", "identityProvider", "partnerProfileId", "primaryContactId", "activeDirectoryId", "identityProviderAccessToken", "birthday"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
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
        """Create an instance of ContactDto from a JSON string"""
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
            "qualified_name",
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

        # set to None if qualified_name (nullable) is None
        # and model_fields_set contains the field
        if self.qualified_name is None and "qualified_name" in self.model_fields_set:
            _dict['qualifiedName'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if public_name (nullable) is None
        # and model_fields_set contains the field
        if self.public_name is None and "public_name" in self.model_fields_set:
            _dict['publicName'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

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

        # set to None if country_id (nullable) is None
        # and model_fields_set contains the field
        if self.country_id is None and "country_id" in self.model_fields_set:
            _dict['countryId'] = None

        # set to None if timezone_id (nullable) is None
        # and model_fields_set contains the field
        if self.timezone_id is None and "timezone_id" in self.model_fields_set:
            _dict['timezoneId'] = None

        # set to None if language_id (nullable) is None
        # and model_fields_set contains the field
        if self.language_id is None and "language_id" in self.model_fields_set:
            _dict['languageId'] = None

        # set to None if social_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.social_profile_id is None and "social_profile_id" in self.model_fields_set:
            _dict['socialProfileId'] = None

        # set to None if web_url (nullable) is None
        # and model_fields_set contains the field
        if self.web_url is None and "web_url" in self.model_fields_set:
            _dict['webUrl'] = None

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

        # set to None if duns (nullable) is None
        # and model_fields_set contains the field
        if self.duns is None and "duns" in self.model_fields_set:
            _dict['duns'] = None

        # set to None if tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id is None and "tax_id" in self.model_fields_set:
            _dict['taxId'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if about (nullable) is None
        # and model_fields_set contains the field
        if self.about is None and "about" in self.model_fields_set:
            _dict['about'] = None

        # set to None if street (nullable) is None
        # and model_fields_set contains the field
        if self.street is None and "street" in self.model_fields_set:
            _dict['street'] = None

        # set to None if cart_id (nullable) is None
        # and model_fields_set contains the field
        if self.cart_id is None and "cart_id" in self.model_fields_set:
            _dict['cartId'] = None

        # set to None if city_id (nullable) is None
        # and model_fields_set contains the field
        if self.city_id is None and "city_id" in self.model_fields_set:
            _dict['cityId'] = None

        # set to None if zip_code (nullable) is None
        # and model_fields_set contains the field
        if self.zip_code is None and "zip_code" in self.model_fields_set:
            _dict['zipCode'] = None

        # set to None if state_id (nullable) is None
        # and model_fields_set contains the field
        if self.state_id is None and "state_id" in self.model_fields_set:
            _dict['stateId'] = None

        # set to None if wallet_id (nullable) is None
        # and model_fields_set contains the field
        if self.wallet_id is None and "wallet_id" in self.model_fields_set:
            _dict['walletId'] = None

        # set to None if fax_number (nullable) is None
        # and model_fields_set contains the field
        if self.fax_number is None and "fax_number" in self.model_fields_set:
            _dict['faxNumber'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postalCode'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if street_line1 (nullable) is None
        # and model_fields_set contains the field
        if self.street_line1 is None and "street_line1" in self.model_fields_set:
            _dict['streetLine1'] = None

        # set to None if street_line2 (nullable) is None
        # and model_fields_set contains the field
        if self.street_line2 is None and "street_line2" in self.model_fields_set:
            _dict['streetLine2'] = None

        # set to None if territory_id (nullable) is None
        # and model_fields_set contains the field
        if self.territory_id is None and "territory_id" in self.model_fields_set:
            _dict['territoryId'] = None

        # set to None if mobile_phone (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone is None and "mobile_phone" in self.model_fields_set:
            _dict['mobilePhone'] = None

        # set to None if enrollment_id (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_id is None and "enrollment_id" in self.model_fields_set:
            _dict['enrollmentId'] = None

        # set to None if annual_revenue (nullable) is None
        # and model_fields_set contains the field
        if self.annual_revenue is None and "annual_revenue" in self.model_fields_set:
            _dict['annualRevenue'] = None

        # set to None if related_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_user_id is None and "related_user_id" in self.model_fields_set:
            _dict['relatedUserId'] = None

        # set to None if business_phone (nullable) is None
        # and model_fields_set contains the field
        if self.business_phone is None and "business_phone" in self.model_fields_set:
            _dict['businessPhone'] = None

        # set to None if owner_contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.owner_contact_id is None and "owner_contact_id" in self.model_fields_set:
            _dict['ownerContactId'] = None

        # set to None if related_tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_tenant_id is None and "related_tenant_id" in self.model_fields_set:
            _dict['relatedTenantId'] = None

        # set to None if activity_feed_id (nullable) is None
        # and model_fields_set contains the field
        if self.activity_feed_id is None and "activity_feed_id" in self.model_fields_set:
            _dict['activityFeedId'] = None

        # set to None if parent_contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_contact_id is None and "parent_contact_id" in self.model_fields_set:
            _dict['parentContactId'] = None

        # set to None if identity_provider (nullable) is None
        # and model_fields_set contains the field
        if self.identity_provider is None and "identity_provider" in self.model_fields_set:
            _dict['identityProvider'] = None

        # set to None if partner_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.partner_profile_id is None and "partner_profile_id" in self.model_fields_set:
            _dict['partnerProfileId'] = None

        # set to None if primary_contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.primary_contact_id is None and "primary_contact_id" in self.model_fields_set:
            _dict['primaryContactId'] = None

        # set to None if active_directory_id (nullable) is None
        # and model_fields_set contains the field
        if self.active_directory_id is None and "active_directory_id" in self.model_fields_set:
            _dict['activeDirectoryId'] = None

        # set to None if identity_provider_access_token (nullable) is None
        # and model_fields_set contains the field
        if self.identity_provider_access_token is None and "identity_provider_access_token" in self.model_fields_set:
            _dict['identityProviderAccessToken'] = None

        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContactDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "qualifiedName": obj.get("qualifiedName"),
            "tenantId": obj.get("tenantId"),
            "type": obj.get("type"),
            "publicName": obj.get("publicName"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "jobTitle": obj.get("jobTitle"),
            "coverUrl": obj.get("coverUrl"),
            "avatarUrl": obj.get("avatarUrl"),
            "countryId": obj.get("countryId"),
            "timezoneId": obj.get("timezoneId"),
            "languageId": obj.get("languageId"),
            "socialProfileId": obj.get("socialProfileId"),
            "webUrl": obj.get("webUrl"),
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
            "duns": obj.get("duns"),
            "taxId": obj.get("taxId"),
            "email": obj.get("email"),
            "about": obj.get("about"),
            "street": obj.get("street"),
            "cartId": obj.get("cartId"),
            "cityId": obj.get("cityId"),
            "zipCode": obj.get("zipCode"),
            "stateId": obj.get("stateId"),
            "walletId": obj.get("walletId"),
            "faxNumber": obj.get("faxNumber"),
            "postalCode": obj.get("postalCode"),
            "currencyId": obj.get("currencyId"),
            "streetLine1": obj.get("streetLine1"),
            "streetLine2": obj.get("streetLine2"),
            "territoryId": obj.get("territoryId"),
            "mobilePhone": obj.get("mobilePhone"),
            "enrollmentId": obj.get("enrollmentId"),
            "annualRevenue": obj.get("annualRevenue"),
            "relatedUserId": obj.get("relatedUserId"),
            "businessPhone": obj.get("businessPhone"),
            "ownerContactId": obj.get("ownerContactId"),
            "relatedTenantId": obj.get("relatedTenantId"),
            "activityFeedId": obj.get("activityFeedId"),
            "parentContactId": obj.get("parentContactId"),
            "identityProvider": obj.get("identityProvider"),
            "partnerProfileId": obj.get("partnerProfileId"),
            "primaryContactId": obj.get("primaryContactId"),
            "activeDirectoryId": obj.get("activeDirectoryId"),
            "identityProviderAccessToken": obj.get("identityProviderAccessToken"),
            "birthday": obj.get("birthday")
        })
        return _obj


