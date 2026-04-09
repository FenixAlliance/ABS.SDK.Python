# ItemImageUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | 
**is_item_mozaic_bg** | **bool** |  | [optional] 
**m_d5_hash** | **str** |  | 
**metadata** | **str** |  | [optional] 
**file_upload_url** | **str** |  | 
**file_name** | **str** |  | 
**title** | **str** |  | [optional] 
**abstract** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**key_words** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**content_type** | **str** |  | 
**file_length** | **int** |  | [optional] 
**valid_response** | **bool** |  | [optional] 
**parent_file_upload_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_image_update_dto import ItemImageUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemImageUpdateDto from a JSON string
item_image_update_dto_instance = ItemImageUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemImageUpdateDto.to_json())

# convert the object into a dict
item_image_update_dto_dict = item_image_update_dto_instance.to_dict()
# create an instance of ItemImageUpdateDto from a dict
item_image_update_dto_from_dict = ItemImageUpdateDto.from_dict(item_image_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


