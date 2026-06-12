# WebComponentDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**WebComponentDto**](WebComponentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_component_dto_envelope import WebComponentDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WebComponentDtoEnvelope from a JSON string
web_component_dto_envelope_instance = WebComponentDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(WebComponentDtoEnvelope.to_json())

# convert the object into a dict
web_component_dto_envelope_dict = web_component_dto_envelope_instance.to_dict()
# create an instance of WebComponentDtoEnvelope from a dict
web_component_dto_envelope_from_dict = WebComponentDtoEnvelope.from_dict(web_component_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


