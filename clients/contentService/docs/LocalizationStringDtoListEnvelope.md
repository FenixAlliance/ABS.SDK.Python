# LocalizationStringDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LocalizationStringDto]**](LocalizationStringDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.localization_string_dto_list_envelope import LocalizationStringDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationStringDtoListEnvelope from a JSON string
localization_string_dto_list_envelope_instance = LocalizationStringDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LocalizationStringDtoListEnvelope.to_json())

# convert the object into a dict
localization_string_dto_list_envelope_dict = localization_string_dto_list_envelope_instance.to_dict()
# create an instance of LocalizationStringDtoListEnvelope from a dict
localization_string_dto_list_envelope_from_dict = LocalizationStringDtoListEnvelope.from_dict(localization_string_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


