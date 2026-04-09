# WebContentDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**WebContentDto**](WebContentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_content_dto_envelope import WebContentDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WebContentDtoEnvelope from a JSON string
web_content_dto_envelope_instance = WebContentDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(WebContentDtoEnvelope.to_json())

# convert the object into a dict
web_content_dto_envelope_dict = web_content_dto_envelope_instance.to_dict()
# create an instance of WebContentDtoEnvelope from a dict
web_content_dto_envelope_from_dict = WebContentDtoEnvelope.from_dict(web_content_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


