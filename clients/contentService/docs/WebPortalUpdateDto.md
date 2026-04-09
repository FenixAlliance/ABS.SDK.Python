# WebPortalUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**website_theme_id** | **str** |  | [optional] 
**business_domain_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**business_portal_application_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.web_portal_update_dto import WebPortalUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebPortalUpdateDto from a JSON string
web_portal_update_dto_instance = WebPortalUpdateDto.from_json(json)
# print the JSON string representation of the object
print(WebPortalUpdateDto.to_json())

# convert the object into a dict
web_portal_update_dto_dict = web_portal_update_dto_instance.to_dict()
# create an instance of WebPortalUpdateDto from a dict
web_portal_update_dto_from_dict = WebPortalUpdateDto.from_dict(web_portal_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


