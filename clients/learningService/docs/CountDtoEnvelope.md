# CountDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**CountDto**](CountDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.count_dto_envelope import CountDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CountDtoEnvelope from a JSON string
count_dto_envelope_instance = CountDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(CountDtoEnvelope.to_json())

# convert the object into a dict
count_dto_envelope_dict = count_dto_envelope_instance.to_dict()
# create an instance of CountDtoEnvelope from a dict
count_dto_envelope_from_dict = CountDtoEnvelope.from_dict(count_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


