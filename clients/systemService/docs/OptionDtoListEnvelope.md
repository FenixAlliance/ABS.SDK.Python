# OptionDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[OptionDto]**](OptionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.option_dto_list_envelope import OptionDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OptionDtoListEnvelope from a JSON string
option_dto_list_envelope_instance = OptionDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(OptionDtoListEnvelope.to_json())

# convert the object into a dict
option_dto_list_envelope_dict = option_dto_list_envelope_instance.to_dict()
# create an instance of OptionDtoListEnvelope from a dict
option_dto_list_envelope_from_dict = OptionDtoListEnvelope.from_dict(option_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


