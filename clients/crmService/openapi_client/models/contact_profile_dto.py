# coding: utf-8

"""
    CrmService

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
from typing import Optional, Set
from typing_extensions import Self

class ContactProfileDto(BaseModel):
    """
    ContactProfileDto
    """ # noqa: E501
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    contact_id: Optional[StrictStr] = Field(default=None, alias="contactId")
    enrollment_id: Optional[StrictStr] = Field(default=None, alias="enrollmentId")
    about: Optional[StrictStr] = None
    verified: Optional[StrictBool] = None
    submitted: Optional[StrictBool] = None
    avatar_url: Optional[StrictStr] = Field(default=None, alias="avatarUrl")
    qualified_name: Optional[StrictStr] = Field(default=None, alias="qualifiedName")
    verification_timestamp: Optional[datetime] = Field(default=None, alias="verificationTimestamp")
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
    __properties: ClassVar[List[str]] = ["id", "timestamp", "tenantId", "contactId", "enrollmentId", "about", "verified", "submitted", "avatarUrl", "qualifiedName", "verificationTimestamp", "data", "dataLabel", "data1", "data1Label", "data2", "data2Label", "data3", "data3Label", "data4", "data4Label", "data5", "data5Label", "data6", "data6Label", "data7", "data7Label", "data8", "data8Label", "data9", "data9Label"]

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
        """Create an instance of ContactProfileDto from a JSON string"""
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

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.contact_id is None and "contact_id" in self.model_fields_set:
            _dict['contactId'] = None

        # set to None if enrollment_id (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_id is None and "enrollment_id" in self.model_fields_set:
            _dict['enrollmentId'] = None

        # set to None if about (nullable) is None
        # and model_fields_set contains the field
        if self.about is None and "about" in self.model_fields_set:
            _dict['about'] = None

        # set to None if avatar_url (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_url is None and "avatar_url" in self.model_fields_set:
            _dict['avatarUrl'] = None

        # set to None if qualified_name (nullable) is None
        # and model_fields_set contains the field
        if self.qualified_name is None and "qualified_name" in self.model_fields_set:
            _dict['qualifiedName'] = None

        # set to None if verification_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.verification_timestamp is None and "verification_timestamp" in self.model_fields_set:
            _dict['verificationTimestamp'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContactProfileDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "tenantId": obj.get("tenantId"),
            "contactId": obj.get("contactId"),
            "enrollmentId": obj.get("enrollmentId"),
            "about": obj.get("about"),
            "verified": obj.get("verified"),
            "submitted": obj.get("submitted"),
            "avatarUrl": obj.get("avatarUrl"),
            "qualifiedName": obj.get("qualifiedName"),
            "verificationTimestamp": obj.get("verificationTimestamp"),
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
            "data9Label": obj.get("data9Label")
        })
        return _obj

