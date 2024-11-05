# coding: utf-8

"""
    SupportService

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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Tuple, Union
from typing import Optional, Set
from typing_extensions import Self

class SupportRequestAttachmentUpdateDto(BaseModel):
    """
    SupportRequestAttachmentUpdateDto
    """ # noqa: E501
    notes: Optional[StrictStr] = None
    metadata: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    author: Optional[StrictStr] = None
    is_folder: Optional[StrictBool] = Field(default=None, alias="isFolder")
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    abstract: Optional[StrictStr] = None
    key_words: Optional[StrictStr] = Field(default=None, alias="keyWords")
    valid_response: Optional[StrictBool] = Field(default=None, alias="validResponse")
    parent_file_upload_id: Optional[StrictStr] = Field(default=None, alias="parentFileUploadID")
    file_path: Optional[StrictStr] = Field(default=None, alias="filePath")
    file: Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]] = None
    content_type: Optional[StrictStr] = Field(default=None, alias="contentType")
    file_length: Optional[StrictInt] = Field(default=None, alias="fileLength")
    __properties: ClassVar[List[str]] = ["notes", "metadata", "title", "author", "isFolder", "fileName", "abstract", "keyWords", "validResponse", "parentFileUploadID", "filePath", "file", "contentType", "fileLength"]

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
        """Create an instance of SupportRequestAttachmentUpdateDto from a JSON string"""
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
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if author (nullable) is None
        # and model_fields_set contains the field
        if self.author is None and "author" in self.model_fields_set:
            _dict['author'] = None

        # set to None if file_name (nullable) is None
        # and model_fields_set contains the field
        if self.file_name is None and "file_name" in self.model_fields_set:
            _dict['fileName'] = None

        # set to None if abstract (nullable) is None
        # and model_fields_set contains the field
        if self.abstract is None and "abstract" in self.model_fields_set:
            _dict['abstract'] = None

        # set to None if key_words (nullable) is None
        # and model_fields_set contains the field
        if self.key_words is None and "key_words" in self.model_fields_set:
            _dict['keyWords'] = None

        # set to None if parent_file_upload_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_file_upload_id is None and "parent_file_upload_id" in self.model_fields_set:
            _dict['parentFileUploadID'] = None

        # set to None if file_path (nullable) is None
        # and model_fields_set contains the field
        if self.file_path is None and "file_path" in self.model_fields_set:
            _dict['filePath'] = None

        # set to None if file (nullable) is None
        # and model_fields_set contains the field
        if self.file is None and "file" in self.model_fields_set:
            _dict['file'] = None

        # set to None if content_type (nullable) is None
        # and model_fields_set contains the field
        if self.content_type is None and "content_type" in self.model_fields_set:
            _dict['contentType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupportRequestAttachmentUpdateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "notes": obj.get("notes"),
            "metadata": obj.get("metadata"),
            "title": obj.get("title"),
            "author": obj.get("author"),
            "isFolder": obj.get("isFolder"),
            "fileName": obj.get("fileName"),
            "abstract": obj.get("abstract"),
            "keyWords": obj.get("keyWords"),
            "validResponse": obj.get("validResponse"),
            "parentFileUploadID": obj.get("parentFileUploadID"),
            "filePath": obj.get("filePath"),
            "file": obj.get("file"),
            "contentType": obj.get("contentType"),
            "fileLength": obj.get("fileLength")
        })
        return _obj

