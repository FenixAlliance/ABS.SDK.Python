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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class InvoiceAdjustmentUpdateDto(BaseModel):
    """
    InvoiceAdjustmentUpdateDto
    """ # noqa: E501
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    description: Optional[StrictStr] = None
    surcharge_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="surchargePercent")
    surcharge_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="surchargeAmount")
    discount_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="discountPercent")
    discount_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="discountAmount")
    total_surcharge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalSurcharge")
    total_discount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalDiscount")
    type: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["currencyId", "description", "surchargePercent", "surchargeAmount", "discountPercent", "discountAmount", "totalSurcharge", "totalDiscount", "type"]

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
        """Create an instance of InvoiceAdjustmentUpdateDto from a JSON string"""
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
        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceAdjustmentUpdateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currencyId": obj.get("currencyId"),
            "description": obj.get("description"),
            "surchargePercent": obj.get("surchargePercent"),
            "surchargeAmount": obj.get("surchargeAmount"),
            "discountPercent": obj.get("discountPercent"),
            "discountAmount": obj.get("discountAmount"),
            "totalSurcharge": obj.get("totalSurcharge"),
            "totalDiscount": obj.get("totalDiscount"),
            "type": obj.get("type")
        })
        return _obj


