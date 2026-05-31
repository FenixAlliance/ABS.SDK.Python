# ItemFamilyDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemFamilyDto**](ItemFamilyDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_family_dto_envelope import ItemFamilyDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFamilyDtoEnvelope from a JSON string
item_family_dto_envelope_instance = ItemFamilyDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemFamilyDtoEnvelope.to_json())

# convert the object into a dict
item_family_dto_envelope_dict = item_family_dto_envelope_instance.to_dict()
# create an instance of ItemFamilyDtoEnvelope from a dict
item_family_dto_envelope_from_dict = ItemFamilyDtoEnvelope.from_dict(item_family_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


