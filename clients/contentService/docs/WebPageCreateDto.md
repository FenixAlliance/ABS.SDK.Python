# WebPageCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**html_content** | **str** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 
**code_type** | **str** |  | [optional] 
**web_template_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_page_create_dto import WebPageCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageCreateDto from a JSON string
web_page_create_dto_instance = WebPageCreateDto.from_json(json)
# print the JSON string representation of the object
print(WebPageCreateDto.to_json())

# convert the object into a dict
web_page_create_dto_dict = web_page_create_dto_instance.to_dict()
# create an instance of WebPageCreateDto from a dict
web_page_create_dto_from_dict = WebPageCreateDto.from_dict(web_page_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


