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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DealUnitFlowStageCreateDto(BaseModel):
    """
    DealUnitFlowStageCreateDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    order: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    deal_unit_flow_id: Optional[StrictStr] = Field(default=None, alias="dealUnitFlowId")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    description: Optional[StrictStr] = None
    enrolment_id: Optional[StrictStr] = Field(default=None, alias="enrolmentId")
    parent_business_process_stage_id: Optional[StrictStr] = Field(default=None, alias="parentBusinessProcessStageId")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "order", "name", "dealUnitFlowId", "tenantId", "description", "enrolmentId", "parentBusinessProcessStageId"]

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
        """Create an instance of DealUnitFlowStageCreateDto from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "timestamp",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if deal_unit_flow_id (nullable) is None
        # and model_fields_set contains the field
        if self.deal_unit_flow_id is None and "deal_unit_flow_id" in self.model_fields_set:
            _dict['dealUnitFlowId'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if enrolment_id (nullable) is None
        # and model_fields_set contains the field
        if self.enrolment_id is None and "enrolment_id" in self.model_fields_set:
            _dict['enrolmentId'] = None

        # set to None if parent_business_process_stage_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_business_process_stage_id is None and "parent_business_process_stage_id" in self.model_fields_set:
            _dict['parentBusinessProcessStageId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DealUnitFlowStageCreateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "order": obj.get("order"),
            "name": obj.get("name"),
            "dealUnitFlowId": obj.get("dealUnitFlowId"),
            "tenantId": obj.get("tenantId"),
            "description": obj.get("description"),
            "enrolmentId": obj.get("enrolmentId"),
            "parentBusinessProcessStageId": obj.get("parentBusinessProcessStageId")
        })
        return _obj

