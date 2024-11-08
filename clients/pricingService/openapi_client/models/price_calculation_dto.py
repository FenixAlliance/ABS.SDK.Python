# coding: utf-8

"""
    PricingService

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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class PriceCalculationDto(BaseModel):
    """
    PriceCalculationDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    unit_id: Optional[StrictStr] = Field(default=None, alias="unitId")
    unit_group_id: Optional[StrictStr] = Field(default=None, alias="unitGroupId")
    price_id: Optional[StrictStr] = Field(default=None, alias="priceId")
    price_list_id: Optional[StrictStr] = Field(default=None, alias="priceListId")
    discount_id: Optional[StrictStr] = Field(default=None, alias="discountId")
    discount_list_id: Optional[StrictStr] = Field(default=None, alias="discountListId")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    enrollment_id: Optional[StrictStr] = Field(default=None, alias="enrollmentId")
    rounding_policy_id: Optional[StrictStr] = Field(default=None, alias="roundingPolicyId")
    effective_discount_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="effectiveDiscountPercent")
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    total_base_amount: Optional[Money] = Field(default=None, alias="totalBaseAmount")
    total_discounts_amount: Optional[Money] = Field(default=None, alias="totalDiscountsAmount")
    total_surcharges_amount: Optional[Money] = Field(default=None, alias="totalSurchargesAmount")
    total_shipping_amount: Optional[Money] = Field(default=None, alias="totalShippingAmount")
    total_shipping_tax_amount: Optional[Money] = Field(default=None, alias="totalShippingTaxAmount")
    total_tax_amount: Optional[Money] = Field(default=None, alias="totalTaxAmount")
    total_amount: Optional[Money] = Field(default=None, alias="totalAmount")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "itemId", "unitId", "unitGroupId", "priceId", "priceListId", "discountId", "discountListId", "tenantId", "enrollmentId", "roundingPolicyId", "effectiveDiscountPercent", "currencyId", "totalBaseAmount", "totalDiscountsAmount", "totalSurchargesAmount", "totalShippingAmount", "totalShippingTaxAmount", "totalTaxAmount", "totalAmount"]

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
        """Create an instance of PriceCalculationDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of total_base_amount
        if self.total_base_amount:
            _dict['totalBaseAmount'] = self.total_base_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_discounts_amount
        if self.total_discounts_amount:
            _dict['totalDiscountsAmount'] = self.total_discounts_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_surcharges_amount
        if self.total_surcharges_amount:
            _dict['totalSurchargesAmount'] = self.total_surcharges_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_shipping_amount
        if self.total_shipping_amount:
            _dict['totalShippingAmount'] = self.total_shipping_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_shipping_tax_amount
        if self.total_shipping_tax_amount:
            _dict['totalShippingTaxAmount'] = self.total_shipping_tax_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_tax_amount
        if self.total_tax_amount:
            _dict['totalTaxAmount'] = self.total_tax_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_amount
        if self.total_amount:
            _dict['totalAmount'] = self.total_amount.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if item_id (nullable) is None
        # and model_fields_set contains the field
        if self.item_id is None and "item_id" in self.model_fields_set:
            _dict['itemId'] = None

        # set to None if unit_id (nullable) is None
        # and model_fields_set contains the field
        if self.unit_id is None and "unit_id" in self.model_fields_set:
            _dict['unitId'] = None

        # set to None if unit_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.unit_group_id is None and "unit_group_id" in self.model_fields_set:
            _dict['unitGroupId'] = None

        # set to None if price_id (nullable) is None
        # and model_fields_set contains the field
        if self.price_id is None and "price_id" in self.model_fields_set:
            _dict['priceId'] = None

        # set to None if price_list_id (nullable) is None
        # and model_fields_set contains the field
        if self.price_list_id is None and "price_list_id" in self.model_fields_set:
            _dict['priceListId'] = None

        # set to None if discount_id (nullable) is None
        # and model_fields_set contains the field
        if self.discount_id is None and "discount_id" in self.model_fields_set:
            _dict['discountId'] = None

        # set to None if discount_list_id (nullable) is None
        # and model_fields_set contains the field
        if self.discount_list_id is None and "discount_list_id" in self.model_fields_set:
            _dict['discountListId'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if enrollment_id (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_id is None and "enrollment_id" in self.model_fields_set:
            _dict['enrollmentId'] = None

        # set to None if rounding_policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.rounding_policy_id is None and "rounding_policy_id" in self.model_fields_set:
            _dict['roundingPolicyId'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceCalculationDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "itemId": obj.get("itemId"),
            "unitId": obj.get("unitId"),
            "unitGroupId": obj.get("unitGroupId"),
            "priceId": obj.get("priceId"),
            "priceListId": obj.get("priceListId"),
            "discountId": obj.get("discountId"),
            "discountListId": obj.get("discountListId"),
            "tenantId": obj.get("tenantId"),
            "enrollmentId": obj.get("enrollmentId"),
            "roundingPolicyId": obj.get("roundingPolicyId"),
            "effectiveDiscountPercent": obj.get("effectiveDiscountPercent"),
            "currencyId": obj.get("currencyId"),
            "totalBaseAmount": Money.from_dict(obj["totalBaseAmount"]) if obj.get("totalBaseAmount") is not None else None,
            "totalDiscountsAmount": Money.from_dict(obj["totalDiscountsAmount"]) if obj.get("totalDiscountsAmount") is not None else None,
            "totalSurchargesAmount": Money.from_dict(obj["totalSurchargesAmount"]) if obj.get("totalSurchargesAmount") is not None else None,
            "totalShippingAmount": Money.from_dict(obj["totalShippingAmount"]) if obj.get("totalShippingAmount") is not None else None,
            "totalShippingTaxAmount": Money.from_dict(obj["totalShippingTaxAmount"]) if obj.get("totalShippingTaxAmount") is not None else None,
            "totalTaxAmount": Money.from_dict(obj["totalTaxAmount"]) if obj.get("totalTaxAmount") is not None else None,
            "totalAmount": Money.from_dict(obj["totalAmount"]) if obj.get("totalAmount") is not None else None
        })
        return _obj


