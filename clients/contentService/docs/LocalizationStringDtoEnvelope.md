# LocalizationStringDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**LocalizationStringDto**](LocalizationStringDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.localization_string_dto_envelope import LocalizationStringDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationStringDtoEnvelope from a JSON string
localization_string_dto_envelope_instance = LocalizationStringDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(LocalizationStringDtoEnvelope.to_json())

# convert the object into a dict
localization_string_dto_envelope_dict = localization_string_dto_envelope_instance.to_dict()
# create an instance of LocalizationStringDtoEnvelope from a dict
localization_string_dto_envelope_from_dict = LocalizationStringDtoEnvelope.from_dict(localization_string_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


