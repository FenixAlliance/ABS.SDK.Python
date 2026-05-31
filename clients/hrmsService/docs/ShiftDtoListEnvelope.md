# ShiftDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ShiftDto]**](ShiftDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shift_dto_list_envelope import ShiftDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDtoListEnvelope from a JSON string
shift_dto_list_envelope_instance = ShiftDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShiftDtoListEnvelope.to_json())

# convert the object into a dict
shift_dto_list_envelope_dict = shift_dto_list_envelope_instance.to_dict()
# create an instance of ShiftDtoListEnvelope from a dict
shift_dto_list_envelope_from_dict = ShiftDtoListEnvelope.from_dict(shift_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


