# WebComponentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**html_content** | **str** |  | [optional] 
**css_content** | **str** |  | [optional] 
**js_content** | **str** |  | [optional] 
**code_type** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_component_update_dto import WebComponentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebComponentUpdateDto from a JSON string
web_component_update_dto_instance = WebComponentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(WebComponentUpdateDto.to_json())

# convert the object into a dict
web_component_update_dto_dict = web_component_update_dto_instance.to_dict()
# create an instance of WebComponentUpdateDto from a dict
web_component_update_dto_from_dict = WebComponentUpdateDto.from_dict(web_component_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


