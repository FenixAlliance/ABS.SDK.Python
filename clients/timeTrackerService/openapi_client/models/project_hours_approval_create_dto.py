# coding: utf-8

"""
    TimeTrackerService

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
from typing import Optional, Set
from typing_extensions import Self

class ProjectHoursApprovalCreateDto(BaseModel):
    """
    ProjectHoursApprovalCreateDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    requester_contact_id: Optional[StrictStr] = Field(default=None, alias="requesterContactID")
    approver_contact_id: Optional[StrictStr] = Field(default=None, alias="approverContactID")
    project_period_id: Optional[StrictStr] = Field(default=None, alias="projectPeriodID")
    comments: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "timestamp", "requesterContactID", "approverContactID", "projectPeriodID", "comments"]

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
        """Create an instance of ProjectHoursApprovalCreateDto from a JSON string"""
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
        # set to None if requester_contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.requester_contact_id is None and "requester_contact_id" in self.model_fields_set:
            _dict['requesterContactID'] = None

        # set to None if approver_contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.approver_contact_id is None and "approver_contact_id" in self.model_fields_set:
            _dict['approverContactID'] = None

        # set to None if project_period_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_period_id is None and "project_period_id" in self.model_fields_set:
            _dict['projectPeriodID'] = None

        # set to None if comments (nullable) is None
        # and model_fields_set contains the field
        if self.comments is None and "comments" in self.model_fields_set:
            _dict['comments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectHoursApprovalCreateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "requesterContactID": obj.get("requesterContactID"),
            "approverContactID": obj.get("approverContactID"),
            "projectPeriodID": obj.get("projectPeriodID"),
            "comments": obj.get("comments")
        })
        return _obj

