# coding: utf-8

"""
    HrmsService

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
from openapi_client.models.job_offer_dto import JobOfferDto
from typing import Optional, Set
from typing_extensions import Self

class JobOfferDtoListEnvelope(BaseModel):
    """
    JobOfferDtoListEnvelope
    """ # noqa: E501
    is_success: Optional[StrictBool] = Field(default=None, alias="isSuccess")
    error_message: Optional[StrictStr] = Field(default=None, alias="errorMessage")
    correlation_id: Optional[StrictStr] = Field(default=None, alias="correlationId")
    timestamp: Optional[datetime] = None
    activity_id: Optional[StrictStr] = Field(default=None, alias="activityId")
    result: Optional[List[JobOfferDto]] = None
    __properties: ClassVar[List[str]] = ["isSuccess", "errorMessage", "correlationId", "timestamp", "activityId", "result"]

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
        """Create an instance of JobOfferDtoListEnvelope from a JSON string"""
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
            "is_success",
            "timestamp",
            "activity_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in result (list)
        _items = []
        if self.result:
            for _item_result in self.result:
                if _item_result:
                    _items.append(_item_result.to_dict())
            _dict['result'] = _items
        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if correlation_id (nullable) is None
        # and model_fields_set contains the field
        if self.correlation_id is None and "correlation_id" in self.model_fields_set:
            _dict['correlationId'] = None

        # set to None if activity_id (nullable) is None
        # and model_fields_set contains the field
        if self.activity_id is None and "activity_id" in self.model_fields_set:
            _dict['activityId'] = None

        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobOfferDtoListEnvelope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isSuccess": obj.get("isSuccess"),
            "errorMessage": obj.get("errorMessage"),
            "correlationId": obj.get("correlationId"),
            "timestamp": obj.get("timestamp"),
            "activityId": obj.get("activityId"),
            "result": [JobOfferDto.from_dict(_item) for _item in obj["result"]] if obj.get("result") is not None else None
        })
        return _obj


