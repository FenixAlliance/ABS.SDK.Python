# ItemImageDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ItemImageDto]**](ItemImageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_image_dto_list_envelope import ItemImageDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemImageDtoListEnvelope from a JSON string
item_image_dto_list_envelope_instance = ItemImageDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemImageDtoListEnvelope.to_json())

# convert the object into a dict
item_image_dto_list_envelope_dict = item_image_dto_list_envelope_instance.to_dict()
# create an instance of ItemImageDtoListEnvelope from a dict
item_image_dto_list_envelope_from_dict = ItemImageDtoListEnvelope.from_dict(item_image_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


