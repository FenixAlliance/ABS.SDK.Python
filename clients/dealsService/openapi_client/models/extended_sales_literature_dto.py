# coding: utf-8

"""
    DealsService

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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.sales_literature_type_dto import SalesLiteratureTypeDto
from openapi_client.models.tenant_dto import TenantDto
from typing import Optional, Set
from typing_extensions import Self

class ExtendedSalesLiteratureDto(BaseModel):
    """
    ExtendedSalesLiteratureDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    title: Optional[StrictStr] = None
    content: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    expiration_date: Optional[datetime] = Field(default=None, alias="expirationDate")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    enrolment_id: Optional[StrictStr] = Field(default=None, alias="enrolmentId")
    sales_literature_type_id: Optional[StrictStr] = Field(default=None, alias="salesLiteratureTypeId")
    sales_literature_type: Optional[SalesLiteratureTypeDto] = Field(default=None, alias="salesLiteratureType")
    tenant: Optional[TenantDto] = None
    __properties: ClassVar[List[str]] = ["id", "timestamp", "title", "content", "description", "modifiedDate", "expirationDate", "tenantId", "enrolmentId", "salesLiteratureTypeId", "salesLiteratureType", "tenant"]

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
        """Create an instance of ExtendedSalesLiteratureDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sales_literature_type
        if self.sales_literature_type:
            _dict['salesLiteratureType'] = self.sales_literature_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant
        if self.tenant:
            _dict['tenant'] = self.tenant.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if enrolment_id (nullable) is None
        # and model_fields_set contains the field
        if self.enrolment_id is None and "enrolment_id" in self.model_fields_set:
            _dict['enrolmentId'] = None

        # set to None if sales_literature_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.sales_literature_type_id is None and "sales_literature_type_id" in self.model_fields_set:
            _dict['salesLiteratureTypeId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExtendedSalesLiteratureDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "title": obj.get("title"),
            "content": obj.get("content"),
            "description": obj.get("description"),
            "modifiedDate": obj.get("modifiedDate"),
            "expirationDate": obj.get("expirationDate"),
            "tenantId": obj.get("tenantId"),
            "enrolmentId": obj.get("enrolmentId"),
            "salesLiteratureTypeId": obj.get("salesLiteratureTypeId"),
            "salesLiteratureType": SalesLiteratureTypeDto.from_dict(obj["salesLiteratureType"]) if obj.get("salesLiteratureType") is not None else None,
            "tenant": TenantDto.from_dict(obj["tenant"]) if obj.get("tenant") is not None else None
        })
        return _obj

