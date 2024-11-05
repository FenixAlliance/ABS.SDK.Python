# SupportRequestAttachmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**is_folder** | **bool** |  | [optional] 
**file_name** | **str** |  | [optional] 
**abstract** | **str** |  | [optional] 
**key_words** | **str** |  | [optional] 
**valid_response** | **bool** |  | [optional] 
**parent_file_upload_id** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**file** | **bytearray** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**support_request_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_request_attachment_create_dto import SupportRequestAttachmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRequestAttachmentCreateDto from a JSON string
support_request_attachment_create_dto_instance = SupportRequestAttachmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(SupportRequestAttachmentCreateDto.to_json())

# convert the object into a dict
support_request_attachment_create_dto_dict = support_request_attachment_create_dto_instance.to_dict()
# create an instance of SupportRequestAttachmentCreateDto from a dict
support_request_attachment_create_dto_from_dict = SupportRequestAttachmentCreateDto.from_dict(support_request_attachment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


