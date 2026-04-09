# ItemAttachmentUpdateDto


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

## Example

```python
from openapi_client.models.item_attachment_update_dto import ItemAttachmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentUpdateDto from a JSON string
item_attachment_update_dto_instance = ItemAttachmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentUpdateDto.to_json())

# convert the object into a dict
item_attachment_update_dto_dict = item_attachment_update_dto_instance.to_dict()
# create an instance of ItemAttachmentUpdateDto from a dict
item_attachment_update_dto_from_dict = ItemAttachmentUpdateDto.from_dict(item_attachment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


