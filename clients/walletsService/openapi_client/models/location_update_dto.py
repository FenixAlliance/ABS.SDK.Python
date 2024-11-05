# coding: utf-8

"""
    WalletsService

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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class LocationUpdateDto(BaseModel):
    """
    LocationUpdateDto
    """ # noqa: E501
    title: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    fax: Optional[StrictStr] = None
    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    address3: Optional[StrictStr] = None
    unit: Optional[StrictStr] = None
    city_id: Optional[StrictStr] = Field(default=None, alias="cityId")
    state_id: Optional[StrictStr] = Field(default=None, alias="stateId")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    country_id: Optional[StrictStr] = Field(default=None, alias="countryId")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    is_routable: Optional[StrictBool] = Field(default=None, alias="isRoutable")
    is_global_primary: Optional[StrictBool] = Field(default=None, alias="isGlobalPrimary")
    is_country_primary: Optional[StrictBool] = Field(default=None, alias="isCountryPrimary")
    can_generate_labels: Optional[StrictBool] = Field(default=None, alias="canGenerateLabels")
    is_default_sender_address: Optional[StrictBool] = Field(default=None, alias="isDefaultSenderAddress")
    is_default_return_address: Optional[StrictBool] = Field(default=None, alias="isDefaultReturnAddress")
    is_default_supping_location: Optional[StrictBool] = Field(default=None, alias="isDefaultSuppingLocation")
    __properties: ClassVar[List[str]] = ["title", "email", "phone", "fax", "address1", "address2", "address3", "unit", "cityId", "stateId", "postalCode", "countryId", "tenantId", "longitude", "latitude", "isRoutable", "isGlobalPrimary", "isCountryPrimary", "canGenerateLabels", "isDefaultSenderAddress", "isDefaultReturnAddress", "isDefaultSuppingLocation"]

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
        """Create an instance of LocationUpdateDto from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if fax (nullable) is None
        # and model_fields_set contains the field
        if self.fax is None and "fax" in self.model_fields_set:
            _dict['fax'] = None

        # set to None if address1 (nullable) is None
        # and model_fields_set contains the field
        if self.address1 is None and "address1" in self.model_fields_set:
            _dict['address1'] = None

        # set to None if address2 (nullable) is None
        # and model_fields_set contains the field
        if self.address2 is None and "address2" in self.model_fields_set:
            _dict['address2'] = None

        # set to None if address3 (nullable) is None
        # and model_fields_set contains the field
        if self.address3 is None and "address3" in self.model_fields_set:
            _dict['address3'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if city_id (nullable) is None
        # and model_fields_set contains the field
        if self.city_id is None and "city_id" in self.model_fields_set:
            _dict['cityId'] = None

        # set to None if state_id (nullable) is None
        # and model_fields_set contains the field
        if self.state_id is None and "state_id" in self.model_fields_set:
            _dict['stateId'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postalCode'] = None

        # set to None if country_id (nullable) is None
        # and model_fields_set contains the field
        if self.country_id is None and "country_id" in self.model_fields_set:
            _dict['countryId'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LocationUpdateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "fax": obj.get("fax"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "address3": obj.get("address3"),
            "unit": obj.get("unit"),
            "cityId": obj.get("cityId"),
            "stateId": obj.get("stateId"),
            "postalCode": obj.get("postalCode"),
            "countryId": obj.get("countryId"),
            "tenantId": obj.get("tenantId"),
            "longitude": obj.get("longitude"),
            "latitude": obj.get("latitude"),
            "isRoutable": obj.get("isRoutable"),
            "isGlobalPrimary": obj.get("isGlobalPrimary"),
            "isCountryPrimary": obj.get("isCountryPrimary"),
            "canGenerateLabels": obj.get("canGenerateLabels"),
            "isDefaultSenderAddress": obj.get("isDefaultSenderAddress"),
            "isDefaultReturnAddress": obj.get("isDefaultReturnAddress"),
            "isDefaultSuppingLocation": obj.get("isDefaultSuppingLocation")
        })
        return _obj


