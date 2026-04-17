# WebContentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**html_content** | **str** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 
**code_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_content_create_dto import WebContentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebContentCreateDto from a JSON string
web_content_create_dto_instance = WebContentCreateDto.from_json(json)
# print the JSON string representation of the object
print(WebContentCreateDto.to_json())

# convert the object into a dict
web_content_create_dto_dict = web_content_create_dto_instance.to_dict()
# create an instance of WebContentCreateDto from a dict
web_content_create_dto_from_dict = WebContentCreateDto.from_dict(web_content_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


