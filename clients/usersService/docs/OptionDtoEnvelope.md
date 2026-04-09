# OptionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**OptionDto**](OptionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.option_dto_envelope import OptionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OptionDtoEnvelope from a JSON string
option_dto_envelope_instance = OptionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(OptionDtoEnvelope.to_json())

# convert the object into a dict
option_dto_envelope_dict = option_dto_envelope_instance.to_dict()
# create an instance of OptionDtoEnvelope from a dict
option_dto_envelope_from_dict = OptionDtoEnvelope.from_dict(option_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


