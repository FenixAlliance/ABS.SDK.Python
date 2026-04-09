# WebTemplateCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**html_content** | **str** |  | [optional] 
**css_content** | **str** |  | [optional] 
**js_content** | **str** |  | [optional] 
**razor_content** | **str** |  | [optional] 
**highlight_image** | **str** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.web_template_create_dto import WebTemplateCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebTemplateCreateDto from a JSON string
web_template_create_dto_instance = WebTemplateCreateDto.from_json(json)
# print the JSON string representation of the object
print(WebTemplateCreateDto.to_json())

# convert the object into a dict
web_template_create_dto_dict = web_template_create_dto_instance.to_dict()
# create an instance of WebTemplateCreateDto from a dict
web_template_create_dto_from_dict = WebTemplateCreateDto.from_dict(web_template_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


