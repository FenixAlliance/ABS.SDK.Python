# ItemImageCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**item_id** | **str** |  | [optional] 
**is_item_mozaic_bg** | **bool** |  | [optional] 
**m_d5_hash** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**file_upload_url** | **str** |  | [optional] 
**file_name** | **str** |  | 
**title** | **str** |  | [optional] 
**abstract** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**key_words** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**file_length** | **int** |  | [optional] 
**valid_response** | **bool** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**parent_file_upload_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_image_create_dto import ItemImageCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemImageCreateDto from a JSON string
item_image_create_dto_instance = ItemImageCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemImageCreateDto.to_json())

# convert the object into a dict
item_image_create_dto_dict = item_image_create_dto_instance.to_dict()
# create an instance of ItemImageCreateDto from a dict
item_image_create_dto_from_dict = ItemImageCreateDto.from_dict(item_image_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


