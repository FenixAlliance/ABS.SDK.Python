# WebComponentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[WebComponentDto]**](WebComponentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_component_dto_list_envelope import WebComponentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WebComponentDtoListEnvelope from a JSON string
web_component_dto_list_envelope_instance = WebComponentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(WebComponentDtoListEnvelope.to_json())

# convert the object into a dict
web_component_dto_list_envelope_dict = web_component_dto_list_envelope_instance.to_dict()
# create an instance of WebComponentDtoListEnvelope from a dict
web_component_dto_list_envelope_from_dict = WebComponentDtoListEnvelope.from_dict(web_component_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


