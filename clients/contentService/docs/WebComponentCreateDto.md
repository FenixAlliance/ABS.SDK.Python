# WebComponentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
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
from openapi_client.models.web_component_create_dto import WebComponentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebComponentCreateDto from a JSON string
web_component_create_dto_instance = WebComponentCreateDto.from_json(json)
# print the JSON string representation of the object
print(WebComponentCreateDto.to_json())

# convert the object into a dict
web_component_create_dto_dict = web_component_create_dto_instance.to_dict()
# create an instance of WebComponentCreateDto from a dict
web_component_create_dto_from_dict = WebComponentCreateDto.from_dict(web_component_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


