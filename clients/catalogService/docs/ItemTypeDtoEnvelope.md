# ItemTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemTypeDto**](ItemTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_type_dto_envelope import ItemTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTypeDtoEnvelope from a JSON string
item_type_dto_envelope_instance = ItemTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemTypeDtoEnvelope.to_json())

# convert the object into a dict
item_type_dto_envelope_dict = item_type_dto_envelope_instance.to_dict()
# create an instance of ItemTypeDtoEnvelope from a dict
item_type_dto_envelope_from_dict = ItemTypeDtoEnvelope.from_dict(item_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


