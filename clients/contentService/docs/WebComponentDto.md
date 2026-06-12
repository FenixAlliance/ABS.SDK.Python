# WebComponentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
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
**tenant_id** | **str** |  | [optional] 
**web_portal_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_component_dto import WebComponentDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebComponentDto from a JSON string
web_component_dto_instance = WebComponentDto.from_json(json)
# print the JSON string representation of the object
print(WebComponentDto.to_json())

# convert the object into a dict
web_component_dto_dict = web_component_dto_instance.to_dict()
# create an instance of WebComponentDto from a dict
web_component_dto_from_dict = WebComponentDto.from_dict(web_component_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


