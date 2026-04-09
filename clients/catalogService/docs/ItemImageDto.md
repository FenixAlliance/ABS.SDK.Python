# ItemImageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**is_item_mozaic_bg** | **bool** |  | [optional] 
**m_d5_hash** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**file_upload_url** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
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
**account_holder_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_image_dto import ItemImageDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemImageDto from a JSON string
item_image_dto_instance = ItemImageDto.from_json(json)
# print the JSON string representation of the object
print(ItemImageDto.to_json())

# convert the object into a dict
item_image_dto_dict = item_image_dto_instance.to_dict()
# create an instance of ItemImageDto from a dict
item_image_dto_from_dict = ItemImageDto.from_dict(item_image_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


