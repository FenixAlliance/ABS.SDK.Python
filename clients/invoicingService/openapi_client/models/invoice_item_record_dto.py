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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class InvoiceItemRecordDto(BaseModel):
    """
    InvoiceItemRecordDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    closed: Optional[StrictBool] = None
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    item_title: Optional[StrictStr] = Field(default=None, alias="itemTitle")
    item_short_description: Optional[StrictStr] = Field(default=None, alias="itemShortDescription")
    item_primary_image_url: Optional[StrictStr] = Field(default=None, alias="itemPrimaryImageUrl")
    shipping_policy_id: Optional[StrictStr] = Field(default=None, alias="shippingPolicyId")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    enrollment_id: Optional[StrictStr] = Field(default=None, alias="enrollmentId")
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    description: Optional[StrictStr] = None
    quantity: Optional[Union[StrictFloat, StrictInt]] = None
    free: Optional[StrictBool] = None
    free_reason: Optional[StrictStr] = Field(default=None, alias="freeReason")
    free_reason_code: Optional[StrictStr] = Field(default=None, alias="freeReasonCode")
    data: Optional[StrictStr] = None
    data_label: Optional[StrictStr] = Field(default=None, alias="dataLabel")
    data1: Optional[StrictStr] = None
    data1_label: Optional[StrictStr] = Field(default=None, alias="data1Label")
    data2: Optional[StrictStr] = None
    data2_label: Optional[StrictStr] = Field(default=None, alias="data2Label")
    data3: Optional[StrictStr] = None
    data3_label: Optional[StrictStr] = Field(default=None, alias="data3Label")
    data4: Optional[StrictStr] = None
    data4_label: Optional[StrictStr] = Field(default=None, alias="data4Label")
    data5: Optional[StrictStr] = None
    data5_label: Optional[StrictStr] = Field(default=None, alias="data5Label")
    data6: Optional[StrictStr] = None
    data6_label: Optional[StrictStr] = Field(default=None, alias="data6Label")
    data7: Optional[StrictStr] = None
    data7_label: Optional[StrictStr] = Field(default=None, alias="data7Label")
    data8: Optional[StrictStr] = None
    data8_label: Optional[StrictStr] = Field(default=None, alias="data8Label")
    data9: Optional[StrictStr] = None
    data9_label: Optional[StrictStr] = Field(default=None, alias="data9Label")
    item_price_id: Optional[StrictStr] = Field(default=None, alias="itemPriceId")
    price_list_item_id: Optional[StrictStr] = Field(default=None, alias="priceListItemId")
    unit_id: Optional[StrictStr] = Field(default=None, alias="unitId")
    unit_group_id: Optional[StrictStr] = Field(default=None, alias="unitGroupId")
    tax_calculation_method: Optional[StrictInt] = Field(default=None, alias="taxCalculationMethod")
    cost_calculation_method: Optional[StrictInt] = Field(default=None, alias="costCalculationMethod")
    forex_rates_snapshot: Optional[StrictStr] = Field(default=None, alias="forexRatesSnapshot")
    forex_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forexRate")
    total_base_amount_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalBaseAmountInUsd")
    total_profit_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalProfitInUsd")
    total_detail_amount_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalDetailAmountInUsd")
    total_tax_base_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalTaxBaseInUsd")
    total_discounts_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalDiscountsInUsd")
    total_taxes_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalTaxesInUsd")
    total_withholding_taxes_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalWithholdingTaxesInUsd")
    total_shipping_cost_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalShippingCostInUsd")
    total_shipping_taxes_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalShippingTaxesInUsd")
    total_warranty_cost_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalWarrantyCostInUsd")
    total_return_cost_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalReturnCostInUsd")
    total_refund_cost_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalRefundCostInUsd")
    total_surcharges_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalSurchargesInUsd")
    total_amount_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalAmountInUsd")
    total_global_discounts_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalGlobalDiscountsInUsd")
    total_global_surcharges_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalGlobalSurchargesInUsd")
    custom_global_surcharges_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customGlobalSurchargesAmount")
    custom_global_discounts_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customGlobalDiscountsAmount")
    custom_base_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customBaseAmount")
    custom_detail_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customDetailAmount")
    custom_discounts_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customDiscountsAmount")
    custom_tax_base: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customTaxBase")
    custom_surcharges_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customSurchargesAmount")
    custom_profit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customProfitAmount")
    custom_shipping_cost_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customShippingCostAmount")
    custom_shipping_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customShippingTaxAmount")
    custom_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customTaxAmount")
    custom_withholding_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customWithholdingTaxAmount")
    custom_total_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customTotalAmount")
    return_policy_id: Optional[StrictStr] = Field(default=None, alias="returnPolicyId")
    refund_policy_id: Optional[StrictStr] = Field(default=None, alias="refundPolicyId")
    warranty_policy_id: Optional[StrictStr] = Field(default=None, alias="warrantyPolicyId")
    shipment_policy_id: Optional[StrictStr] = Field(default=None, alias="shipmentPolicyId")
    shipping_location_id: Optional[StrictStr] = Field(default=None, alias="shippingLocationId")
    location_id: Optional[StrictStr] = Field(default=None, alias="locationId")
    quote_item_record_id: Optional[StrictStr] = Field(default=None, alias="quoteItemRecordId")
    business_profile_record_id: Optional[StrictStr] = Field(default=None, alias="businessProfileRecordId")
    parent_billing_item_record_id: Optional[StrictStr] = Field(default=None, alias="parentBillingItemRecordId")
    invoice_id: Optional[StrictStr] = Field(default=None, alias="invoiceId")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "closed", "itemId", "itemTitle", "itemShortDescription", "itemPrimaryImageUrl", "shippingPolicyId", "tenantId", "enrollmentId", "currencyId", "description", "quantity", "free", "freeReason", "freeReasonCode", "data", "dataLabel", "data1", "data1Label", "data2", "data2Label", "data3", "data3Label", "data4", "data4Label", "data5", "data5Label", "data6", "data6Label", "data7", "data7Label", "data8", "data8Label", "data9", "data9Label", "itemPriceId", "priceListItemId", "unitId", "unitGroupId", "taxCalculationMethod", "costCalculationMethod", "forexRatesSnapshot", "forexRate", "totalBaseAmountInUsd", "totalProfitInUsd", "totalDetailAmountInUsd", "totalTaxBaseInUsd", "totalDiscountsInUsd", "totalTaxesInUsd", "totalWithholdingTaxesInUsd", "totalShippingCostInUsd", "totalShippingTaxesInUsd", "totalWarrantyCostInUsd", "totalReturnCostInUsd", "totalRefundCostInUsd", "totalSurchargesInUsd", "totalAmountInUsd", "totalGlobalDiscountsInUsd", "totalGlobalSurchargesInUsd", "customGlobalSurchargesAmount", "customGlobalDiscountsAmount", "customBaseAmount", "customDetailAmount", "customDiscountsAmount", "customTaxBase", "customSurchargesAmount", "customProfitAmount", "customShippingCostAmount", "customShippingTaxAmount", "customTaxAmount", "customWithholdingTaxAmount", "customTotalAmount", "returnPolicyId", "refundPolicyId", "warrantyPolicyId", "shipmentPolicyId", "shippingLocationId", "locationId", "quoteItemRecordId", "businessProfileRecordId", "parentBillingItemRecordId", "invoiceId"]

    @field_validator('tax_calculation_method')
    def tax_calculation_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @field_validator('cost_calculation_method')
    def cost_calculation_method_validate_enum(cls, value):
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
        """Create an instance of InvoiceItemRecordDto from a JSON string"""
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

        # set to None if item_id (nullable) is None
        # and model_fields_set contains the field
        if self.item_id is None and "item_id" in self.model_fields_set:
            _dict['itemId'] = None

        # set to None if item_title (nullable) is None
        # and model_fields_set contains the field
        if self.item_title is None and "item_title" in self.model_fields_set:
            _dict['itemTitle'] = None

        # set to None if item_short_description (nullable) is None
        # and model_fields_set contains the field
        if self.item_short_description is None and "item_short_description" in self.model_fields_set:
            _dict['itemShortDescription'] = None

        # set to None if item_primary_image_url (nullable) is None
        # and model_fields_set contains the field
        if self.item_primary_image_url is None and "item_primary_image_url" in self.model_fields_set:
            _dict['itemPrimaryImageUrl'] = None

        # set to None if shipping_policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_policy_id is None and "shipping_policy_id" in self.model_fields_set:
            _dict['shippingPolicyId'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if enrollment_id (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_id is None and "enrollment_id" in self.model_fields_set:
            _dict['enrollmentId'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if free_reason (nullable) is None
        # and model_fields_set contains the field
        if self.free_reason is None and "free_reason" in self.model_fields_set:
            _dict['freeReason'] = None

        # set to None if free_reason_code (nullable) is None
        # and model_fields_set contains the field
        if self.free_reason_code is None and "free_reason_code" in self.model_fields_set:
            _dict['freeReasonCode'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if data_label (nullable) is None
        # and model_fields_set contains the field
        if self.data_label is None and "data_label" in self.model_fields_set:
            _dict['dataLabel'] = None

        # set to None if data1 (nullable) is None
        # and model_fields_set contains the field
        if self.data1 is None and "data1" in self.model_fields_set:
            _dict['data1'] = None

        # set to None if data1_label (nullable) is None
        # and model_fields_set contains the field
        if self.data1_label is None and "data1_label" in self.model_fields_set:
            _dict['data1Label'] = None

        # set to None if data2 (nullable) is None
        # and model_fields_set contains the field
        if self.data2 is None and "data2" in self.model_fields_set:
            _dict['data2'] = None

        # set to None if data2_label (nullable) is None
        # and model_fields_set contains the field
        if self.data2_label is None and "data2_label" in self.model_fields_set:
            _dict['data2Label'] = None

        # set to None if data3 (nullable) is None
        # and model_fields_set contains the field
        if self.data3 is None and "data3" in self.model_fields_set:
            _dict['data3'] = None

        # set to None if data3_label (nullable) is None
        # and model_fields_set contains the field
        if self.data3_label is None and "data3_label" in self.model_fields_set:
            _dict['data3Label'] = None

        # set to None if data4 (nullable) is None
        # and model_fields_set contains the field
        if self.data4 is None and "data4" in self.model_fields_set:
            _dict['data4'] = None

        # set to None if data4_label (nullable) is None
        # and model_fields_set contains the field
        if self.data4_label is None and "data4_label" in self.model_fields_set:
            _dict['data4Label'] = None

        # set to None if data5 (nullable) is None
        # and model_fields_set contains the field
        if self.data5 is None and "data5" in self.model_fields_set:
            _dict['data5'] = None

        # set to None if data5_label (nullable) is None
        # and model_fields_set contains the field
        if self.data5_label is None and "data5_label" in self.model_fields_set:
            _dict['data5Label'] = None

        # set to None if data6 (nullable) is None
        # and model_fields_set contains the field
        if self.data6 is None and "data6" in self.model_fields_set:
            _dict['data6'] = None

        # set to None if data6_label (nullable) is None
        # and model_fields_set contains the field
        if self.data6_label is None and "data6_label" in self.model_fields_set:
            _dict['data6Label'] = None

        # set to None if data7 (nullable) is None
        # and model_fields_set contains the field
        if self.data7 is None and "data7" in self.model_fields_set:
            _dict['data7'] = None

        # set to None if data7_label (nullable) is None
        # and model_fields_set contains the field
        if self.data7_label is None and "data7_label" in self.model_fields_set:
            _dict['data7Label'] = None

        # set to None if data8 (nullable) is None
        # and model_fields_set contains the field
        if self.data8 is None and "data8" in self.model_fields_set:
            _dict['data8'] = None

        # set to None if data8_label (nullable) is None
        # and model_fields_set contains the field
        if self.data8_label is None and "data8_label" in self.model_fields_set:
            _dict['data8Label'] = None

        # set to None if data9 (nullable) is None
        # and model_fields_set contains the field
        if self.data9 is None and "data9" in self.model_fields_set:
            _dict['data9'] = None

        # set to None if data9_label (nullable) is None
        # and model_fields_set contains the field
        if self.data9_label is None and "data9_label" in self.model_fields_set:
            _dict['data9Label'] = None

        # set to None if item_price_id (nullable) is None
        # and model_fields_set contains the field
        if self.item_price_id is None and "item_price_id" in self.model_fields_set:
            _dict['itemPriceId'] = None

        # set to None if price_list_item_id (nullable) is None
        # and model_fields_set contains the field
        if self.price_list_item_id is None and "price_list_item_id" in self.model_fields_set:
            _dict['priceListItemId'] = None

        # set to None if unit_id (nullable) is None
        # and model_fields_set contains the field
        if self.unit_id is None and "unit_id" in self.model_fields_set:
            _dict['unitId'] = None

        # set to None if unit_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.unit_group_id is None and "unit_group_id" in self.model_fields_set:
            _dict['unitGroupId'] = None

        # set to None if forex_rates_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.forex_rates_snapshot is None and "forex_rates_snapshot" in self.model_fields_set:
            _dict['forexRatesSnapshot'] = None

        # set to None if return_policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.return_policy_id is None and "return_policy_id" in self.model_fields_set:
            _dict['returnPolicyId'] = None

        # set to None if refund_policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.refund_policy_id is None and "refund_policy_id" in self.model_fields_set:
            _dict['refundPolicyId'] = None

        # set to None if warranty_policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.warranty_policy_id is None and "warranty_policy_id" in self.model_fields_set:
            _dict['warrantyPolicyId'] = None

        # set to None if shipment_policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.shipment_policy_id is None and "shipment_policy_id" in self.model_fields_set:
            _dict['shipmentPolicyId'] = None

        # set to None if shipping_location_id (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_location_id is None and "shipping_location_id" in self.model_fields_set:
            _dict['shippingLocationId'] = None

        # set to None if location_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_id is None and "location_id" in self.model_fields_set:
            _dict['locationId'] = None

        # set to None if quote_item_record_id (nullable) is None
        # and model_fields_set contains the field
        if self.quote_item_record_id is None and "quote_item_record_id" in self.model_fields_set:
            _dict['quoteItemRecordId'] = None

        # set to None if business_profile_record_id (nullable) is None
        # and model_fields_set contains the field
        if self.business_profile_record_id is None and "business_profile_record_id" in self.model_fields_set:
            _dict['businessProfileRecordId'] = None

        # set to None if parent_billing_item_record_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_billing_item_record_id is None and "parent_billing_item_record_id" in self.model_fields_set:
            _dict['parentBillingItemRecordId'] = None

        # set to None if invoice_id (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_id is None and "invoice_id" in self.model_fields_set:
            _dict['invoiceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceItemRecordDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "closed": obj.get("closed"),
            "itemId": obj.get("itemId"),
            "itemTitle": obj.get("itemTitle"),
            "itemShortDescription": obj.get("itemShortDescription"),
            "itemPrimaryImageUrl": obj.get("itemPrimaryImageUrl"),
            "shippingPolicyId": obj.get("shippingPolicyId"),
            "tenantId": obj.get("tenantId"),
            "enrollmentId": obj.get("enrollmentId"),
            "currencyId": obj.get("currencyId"),
            "description": obj.get("description"),
            "quantity": obj.get("quantity"),
            "free": obj.get("free"),
            "freeReason": obj.get("freeReason"),
            "freeReasonCode": obj.get("freeReasonCode"),
            "data": obj.get("data"),
            "dataLabel": obj.get("dataLabel"),
            "data1": obj.get("data1"),
            "data1Label": obj.get("data1Label"),
            "data2": obj.get("data2"),
            "data2Label": obj.get("data2Label"),
            "data3": obj.get("data3"),
            "data3Label": obj.get("data3Label"),
            "data4": obj.get("data4"),
            "data4Label": obj.get("data4Label"),
            "data5": obj.get("data5"),
            "data5Label": obj.get("data5Label"),
            "data6": obj.get("data6"),
            "data6Label": obj.get("data6Label"),
            "data7": obj.get("data7"),
            "data7Label": obj.get("data7Label"),
            "data8": obj.get("data8"),
            "data8Label": obj.get("data8Label"),
            "data9": obj.get("data9"),
            "data9Label": obj.get("data9Label"),
            "itemPriceId": obj.get("itemPriceId"),
            "priceListItemId": obj.get("priceListItemId"),
            "unitId": obj.get("unitId"),
            "unitGroupId": obj.get("unitGroupId"),
            "taxCalculationMethod": obj.get("taxCalculationMethod"),
            "costCalculationMethod": obj.get("costCalculationMethod"),
            "forexRatesSnapshot": obj.get("forexRatesSnapshot"),
            "forexRate": obj.get("forexRate"),
            "totalBaseAmountInUsd": obj.get("totalBaseAmountInUsd"),
            "totalProfitInUsd": obj.get("totalProfitInUsd"),
            "totalDetailAmountInUsd": obj.get("totalDetailAmountInUsd"),
            "totalTaxBaseInUsd": obj.get("totalTaxBaseInUsd"),
            "totalDiscountsInUsd": obj.get("totalDiscountsInUsd"),
            "totalTaxesInUsd": obj.get("totalTaxesInUsd"),
            "totalWithholdingTaxesInUsd": obj.get("totalWithholdingTaxesInUsd"),
            "totalShippingCostInUsd": obj.get("totalShippingCostInUsd"),
            "totalShippingTaxesInUsd": obj.get("totalShippingTaxesInUsd"),
            "totalWarrantyCostInUsd": obj.get("totalWarrantyCostInUsd"),
            "totalReturnCostInUsd": obj.get("totalReturnCostInUsd"),
            "totalRefundCostInUsd": obj.get("totalRefundCostInUsd"),
            "totalSurchargesInUsd": obj.get("totalSurchargesInUsd"),
            "totalAmountInUsd": obj.get("totalAmountInUsd"),
            "totalGlobalDiscountsInUsd": obj.get("totalGlobalDiscountsInUsd"),
            "totalGlobalSurchargesInUsd": obj.get("totalGlobalSurchargesInUsd"),
            "customGlobalSurchargesAmount": obj.get("customGlobalSurchargesAmount"),
            "customGlobalDiscountsAmount": obj.get("customGlobalDiscountsAmount"),
            "customBaseAmount": obj.get("customBaseAmount"),
            "customDetailAmount": obj.get("customDetailAmount"),
            "customDiscountsAmount": obj.get("customDiscountsAmount"),
            "customTaxBase": obj.get("customTaxBase"),
            "customSurchargesAmount": obj.get("customSurchargesAmount"),
            "customProfitAmount": obj.get("customProfitAmount"),
            "customShippingCostAmount": obj.get("customShippingCostAmount"),
            "customShippingTaxAmount": obj.get("customShippingTaxAmount"),
            "customTaxAmount": obj.get("customTaxAmount"),
            "customWithholdingTaxAmount": obj.get("customWithholdingTaxAmount"),
            "customTotalAmount": obj.get("customTotalAmount"),
            "returnPolicyId": obj.get("returnPolicyId"),
            "refundPolicyId": obj.get("refundPolicyId"),
            "warrantyPolicyId": obj.get("warrantyPolicyId"),
            "shipmentPolicyId": obj.get("shipmentPolicyId"),
            "shippingLocationId": obj.get("shippingLocationId"),
            "locationId": obj.get("locationId"),
            "quoteItemRecordId": obj.get("quoteItemRecordId"),
            "businessProfileRecordId": obj.get("businessProfileRecordId"),
            "parentBillingItemRecordId": obj.get("parentBillingItemRecordId"),
            "invoiceId": obj.get("invoiceId")
        })
        return _obj


