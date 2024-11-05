# SupportRequestAttachmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
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
**content_type** | **str** |  | [optional] 
**file_length** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.support_request_attachment_update_dto import SupportRequestAttachmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRequestAttachmentUpdateDto from a JSON string
support_request_attachment_update_dto_instance = SupportRequestAttachmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SupportRequestAttachmentUpdateDto.to_json())

# convert the object into a dict
support_request_attachment_update_dto_dict = support_request_attachment_update_dto_instance.to_dict()
# create an instance of SupportRequestAttachmentUpdateDto from a dict
support_request_attachment_update_dto_from_dict = SupportRequestAttachmentUpdateDto.from_dict(support_request_attachment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


