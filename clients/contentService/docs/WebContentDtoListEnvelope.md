# WebContentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[WebContentDto]**](WebContentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_content_dto_list_envelope import WebContentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WebContentDtoListEnvelope from a JSON string
web_content_dto_list_envelope_instance = WebContentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(WebContentDtoListEnvelope.to_json())

# convert the object into a dict
web_content_dto_list_envelope_dict = web_content_dto_list_envelope_instance.to_dict()
# create an instance of WebContentDtoListEnvelope from a dict
web_content_dto_list_envelope_from_dict = WebContentDtoListEnvelope.from_dict(web_content_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


