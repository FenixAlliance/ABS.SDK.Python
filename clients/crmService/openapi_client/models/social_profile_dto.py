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
from typing import Optional, Set
from typing_extensions import Self

class SocialProfileDto(BaseModel):
    """
    SocialProfileDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    name: Optional[StrictStr] = None
    about: Optional[StrictStr] = None
    cover: Optional[StrictStr] = None
    avatar: Optional[StrictStr] = None
    country_id: Optional[StrictStr] = Field(default=None, alias="countryId")
    country_name: Optional[StrictStr] = Field(default=None, alias="countryName")
    identity_id: Optional[StrictStr] = Field(default=None, alias="identityId")
    follows_count: Optional[StrictInt] = Field(default=None, alias="followsCount")
    messages_count: Optional[StrictInt] = Field(default=None, alias="messagesCount")
    followers_count: Optional[StrictInt] = Field(default=None, alias="followersCount")
    notifications_count: Optional[StrictInt] = Field(default=None, alias="notificationsCount")
    unread_notifications_count: Optional[StrictInt] = Field(default=None, alias="unreadNotificationsCount")
    unread_messages_count: Optional[StrictInt] = Field(default=None, alias="unreadMessagesCount")
    type: Optional[StrictInt] = None
    social_feed_id: Optional[StrictStr] = Field(default=None, alias="socialFeedId")
    twitter_url: Optional[StrictStr] = Field(default=None, alias="twitterUrl")
    facebook_url: Optional[StrictStr] = Field(default=None, alias="facebookURL")
    linked_in_url: Optional[StrictStr] = Field(default=None, alias="linkedInURL")
    youtube_url: Optional[StrictStr] = Field(default=None, alias="youtubeURL")
    github_url: Optional[StrictStr] = Field(default=None, alias="githubURL")
    pinterest_url: Optional[StrictStr] = Field(default=None, alias="pinterestURL")
    dribble_url: Optional[StrictStr] = Field(default=None, alias="dribbleURL")
    domain: Optional[StrictStr] = None
    notes: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "timestamp", "name", "about", "cover", "avatar", "countryId", "countryName", "identityId", "followsCount", "messagesCount", "followersCount", "notificationsCount", "unreadNotificationsCount", "unreadMessagesCount", "type", "socialFeedId", "twitterUrl", "facebookURL", "linkedInURL", "youtubeURL", "githubURL", "pinterestURL", "dribbleURL", "domain", "notes"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2]):
            raise ValueError("must be one of enum values (0, 1, 2)")
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
        """Create an instance of SocialProfileDto from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if about (nullable) is None
        # and model_fields_set contains the field
        if self.about is None and "about" in self.model_fields_set:
            _dict['about'] = None

        # set to None if cover (nullable) is None
        # and model_fields_set contains the field
        if self.cover is None and "cover" in self.model_fields_set:
            _dict['cover'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if country_id (nullable) is None
        # and model_fields_set contains the field
        if self.country_id is None and "country_id" in self.model_fields_set:
            _dict['countryId'] = None

        # set to None if country_name (nullable) is None
        # and model_fields_set contains the field
        if self.country_name is None and "country_name" in self.model_fields_set:
            _dict['countryName'] = None

        # set to None if identity_id (nullable) is None
        # and model_fields_set contains the field
        if self.identity_id is None and "identity_id" in self.model_fields_set:
            _dict['identityId'] = None

        # set to None if follows_count (nullable) is None
        # and model_fields_set contains the field
        if self.follows_count is None and "follows_count" in self.model_fields_set:
            _dict['followsCount'] = None

        # set to None if messages_count (nullable) is None
        # and model_fields_set contains the field
        if self.messages_count is None and "messages_count" in self.model_fields_set:
            _dict['messagesCount'] = None

        # set to None if followers_count (nullable) is None
        # and model_fields_set contains the field
        if self.followers_count is None and "followers_count" in self.model_fields_set:
            _dict['followersCount'] = None

        # set to None if notifications_count (nullable) is None
        # and model_fields_set contains the field
        if self.notifications_count is None and "notifications_count" in self.model_fields_set:
            _dict['notificationsCount'] = None

        # set to None if unread_notifications_count (nullable) is None
        # and model_fields_set contains the field
        if self.unread_notifications_count is None and "unread_notifications_count" in self.model_fields_set:
            _dict['unreadNotificationsCount'] = None

        # set to None if unread_messages_count (nullable) is None
        # and model_fields_set contains the field
        if self.unread_messages_count is None and "unread_messages_count" in self.model_fields_set:
            _dict['unreadMessagesCount'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if social_feed_id (nullable) is None
        # and model_fields_set contains the field
        if self.social_feed_id is None and "social_feed_id" in self.model_fields_set:
            _dict['socialFeedId'] = None

        # set to None if twitter_url (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_url is None and "twitter_url" in self.model_fields_set:
            _dict['twitterUrl'] = None

        # set to None if facebook_url (nullable) is None
        # and model_fields_set contains the field
        if self.facebook_url is None and "facebook_url" in self.model_fields_set:
            _dict['facebookURL'] = None

        # set to None if linked_in_url (nullable) is None
        # and model_fields_set contains the field
        if self.linked_in_url is None and "linked_in_url" in self.model_fields_set:
            _dict['linkedInURL'] = None

        # set to None if youtube_url (nullable) is None
        # and model_fields_set contains the field
        if self.youtube_url is None and "youtube_url" in self.model_fields_set:
            _dict['youtubeURL'] = None

        # set to None if github_url (nullable) is None
        # and model_fields_set contains the field
        if self.github_url is None and "github_url" in self.model_fields_set:
            _dict['githubURL'] = None

        # set to None if pinterest_url (nullable) is None
        # and model_fields_set contains the field
        if self.pinterest_url is None and "pinterest_url" in self.model_fields_set:
            _dict['pinterestURL'] = None

        # set to None if dribble_url (nullable) is None
        # and model_fields_set contains the field
        if self.dribble_url is None and "dribble_url" in self.model_fields_set:
            _dict['dribbleURL'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SocialProfileDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "name": obj.get("name"),
            "about": obj.get("about"),
            "cover": obj.get("cover"),
            "avatar": obj.get("avatar"),
            "countryId": obj.get("countryId"),
            "countryName": obj.get("countryName"),
            "identityId": obj.get("identityId"),
            "followsCount": obj.get("followsCount"),
            "messagesCount": obj.get("messagesCount"),
            "followersCount": obj.get("followersCount"),
            "notificationsCount": obj.get("notificationsCount"),
            "unreadNotificationsCount": obj.get("unreadNotificationsCount"),
            "unreadMessagesCount": obj.get("unreadMessagesCount"),
            "type": obj.get("type"),
            "socialFeedId": obj.get("socialFeedId"),
            "twitterUrl": obj.get("twitterUrl"),
            "facebookURL": obj.get("facebookURL"),
            "linkedInURL": obj.get("linkedInURL"),
            "youtubeURL": obj.get("youtubeURL"),
            "githubURL": obj.get("githubURL"),
            "pinterestURL": obj.get("pinterestURL"),
            "dribbleURL": obj.get("dribbleURL"),
            "domain": obj.get("domain"),
            "notes": obj.get("notes")
        })
        return _obj


