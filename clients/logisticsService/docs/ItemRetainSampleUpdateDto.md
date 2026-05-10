# ItemRetainSampleUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouse_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_retain_sample_update_dto import ItemRetainSampleUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRetainSampleUpdateDto from a JSON string
item_retain_sample_update_dto_instance = ItemRetainSampleUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemRetainSampleUpdateDto.to_json())

# convert the object into a dict
item_retain_sample_update_dto_dict = item_retain_sample_update_dto_instance.to_dict()
# create an instance of ItemRetainSampleUpdateDto from a dict
item_retain_sample_update_dto_from_dict = ItemRetainSampleUpdateDto.from_dict(item_retain_sample_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


