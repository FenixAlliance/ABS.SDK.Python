# ItemRetainSampleCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**warehouse_id** | **str** |  | 
**item_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_retain_sample_create_dto import ItemRetainSampleCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRetainSampleCreateDto from a JSON string
item_retain_sample_create_dto_instance = ItemRetainSampleCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemRetainSampleCreateDto.to_json())

# convert the object into a dict
item_retain_sample_create_dto_dict = item_retain_sample_create_dto_instance.to_dict()
# create an instance of ItemRetainSampleCreateDto from a dict
item_retain_sample_create_dto_from_dict = ItemRetainSampleCreateDto.from_dict(item_retain_sample_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


