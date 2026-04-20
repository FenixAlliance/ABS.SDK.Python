# WebPortalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**root** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**website_theme_id** | **str** |  | [optional] 
**business_domain_id** | **str** |  | [optional] 
**business_portal_application_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_portal_dto import WebPortalDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebPortalDto from a JSON string
web_portal_dto_instance = WebPortalDto.from_json(json)
# print the JSON string representation of the object
print(WebPortalDto.to_json())

# convert the object into a dict
web_portal_dto_dict = web_portal_dto_instance.to_dict()
# create an instance of WebPortalDto from a dict
web_portal_dto_from_dict = WebPortalDto.from_dict(web_portal_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


