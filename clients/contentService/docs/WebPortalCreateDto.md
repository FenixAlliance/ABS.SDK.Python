# WebPortalCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**root** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**business_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**website_theme_id** | **str** |  | [optional] 
**business_domain_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**business_portal_application_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_portal_create_dto import WebPortalCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebPortalCreateDto from a JSON string
web_portal_create_dto_instance = WebPortalCreateDto.from_json(json)
# print the JSON string representation of the object
print(WebPortalCreateDto.to_json())

# convert the object into a dict
web_portal_create_dto_dict = web_portal_create_dto_instance.to_dict()
# create an instance of WebPortalCreateDto from a dict
web_portal_create_dto_from_dict = WebPortalCreateDto.from_dict(web_portal_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


