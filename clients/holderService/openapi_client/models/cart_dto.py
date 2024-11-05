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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CartDto(BaseModel):
    """
    CartDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    ip: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    taxes: Optional[Union[StrictFloat, StrictInt]] = None
    freight: Optional[Union[StrictFloat, StrictInt]] = None
    sub_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="subTotal")
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    country_id: Optional[StrictStr] = Field(default=None, alias="countryId")
    item_cart_records_count: Optional[StrictInt] = Field(default=None, alias="itemCartRecordsCount")
    item_to_compare_records_count: Optional[StrictInt] = Field(default=None, alias="itemToCompareRecordsCount")
    __properties: ClassVar[List[str]] = ["id", "ip", "type", "total", "taxes", "freight", "subTotal", "currencyId", "countryId", "itemCartRecordsCount", "itemToCompareRecordsCount"]

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
        """Create an instance of CartDto from a JSON string"""
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

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if country_id (nullable) is None
        # and model_fields_set contains the field
        if self.country_id is None and "country_id" in self.model_fields_set:
            _dict['countryId'] = None

        # set to None if item_cart_records_count (nullable) is None
        # and model_fields_set contains the field
        if self.item_cart_records_count is None and "item_cart_records_count" in self.model_fields_set:
            _dict['itemCartRecordsCount'] = None

        # set to None if item_to_compare_records_count (nullable) is None
        # and model_fields_set contains the field
        if self.item_to_compare_records_count is None and "item_to_compare_records_count" in self.model_fields_set:
            _dict['itemToCompareRecordsCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CartDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "ip": obj.get("ip"),
            "type": obj.get("type"),
            "total": obj.get("total"),
            "taxes": obj.get("taxes"),
            "freight": obj.get("freight"),
            "subTotal": obj.get("subTotal"),
            "currencyId": obj.get("currencyId"),
            "countryId": obj.get("countryId"),
            "itemCartRecordsCount": obj.get("itemCartRecordsCount"),
            "itemToCompareRecordsCount": obj.get("itemToCompareRecordsCount")
        })
        return _obj


