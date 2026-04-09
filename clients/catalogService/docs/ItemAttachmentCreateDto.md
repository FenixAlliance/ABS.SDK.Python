# ItemAttachmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
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
**item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_attachment_create_dto import ItemAttachmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentCreateDto from a JSON string
item_attachment_create_dto_instance = ItemAttachmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentCreateDto.to_json())

# convert the object into a dict
item_attachment_create_dto_dict = item_attachment_create_dto_instance.to_dict()
# create an instance of ItemAttachmentCreateDto from a dict
item_attachment_create_dto_from_dict = ItemAttachmentCreateDto.from_dict(item_attachment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


