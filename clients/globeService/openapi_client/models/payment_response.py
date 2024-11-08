# coding: utf-8

"""
    GlobeService

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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PaymentResponse(BaseModel):
    """
    PaymentResponse
    """ # noqa: E501
    test: Optional[StrictBool] = None
    ip: Optional[StrictStr] = None
    bank: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    errors: Optional[Any] = None
    response: Optional[StrictStr] = None
    auth_code: Optional[StrictStr] = Field(default=None, alias="authCode")
    payment_id: Optional[StrictStr] = Field(default=None, alias="paymentID")
    franchise: Optional[StrictStr] = None
    signature: Optional[StrictStr] = None
    payment_status: Optional[StrictInt] = Field(default=None, alias="paymentStatus")
    __properties: ClassVar[List[str]] = ["test", "ip", "bank", "status", "errors", "response", "authCode", "paymentID", "franchise", "signature", "paymentStatus"]

    @field_validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]):
            raise ValueError("must be one of enum values (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)")
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
        """Create an instance of PaymentResponse from a JSON string"""
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
        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if bank (nullable) is None
        # and model_fields_set contains the field
        if self.bank is None and "bank" in self.model_fields_set:
            _dict['bank'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if response (nullable) is None
        # and model_fields_set contains the field
        if self.response is None and "response" in self.model_fields_set:
            _dict['response'] = None

        # set to None if auth_code (nullable) is None
        # and model_fields_set contains the field
        if self.auth_code is None and "auth_code" in self.model_fields_set:
            _dict['authCode'] = None

        # set to None if payment_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_id is None and "payment_id" in self.model_fields_set:
            _dict['paymentID'] = None

        # set to None if franchise (nullable) is None
        # and model_fields_set contains the field
        if self.franchise is None and "franchise" in self.model_fields_set:
            _dict['franchise'] = None

        # set to None if signature (nullable) is None
        # and model_fields_set contains the field
        if self.signature is None and "signature" in self.model_fields_set:
            _dict['signature'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "test": obj.get("test"),
            "ip": obj.get("ip"),
            "bank": obj.get("bank"),
            "status": obj.get("status"),
            "errors": obj.get("errors"),
            "response": obj.get("response"),
            "authCode": obj.get("authCode"),
            "paymentID": obj.get("paymentID"),
            "franchise": obj.get("franchise"),
            "signature": obj.get("signature"),
            "paymentStatus": obj.get("paymentStatus")
        })
        return _obj


