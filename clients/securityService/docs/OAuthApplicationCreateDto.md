# OAuthApplicationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**display_name** | **str** |  | 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**consent_type** | **str** |  | [optional] 
**permissions** | **str** |  | [optional] 
**requirements** | **str** |  | [optional] 
**redirect_uris** | **str** |  | [optional] 
**post_logout_redirect_uris** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_application_create_dto import OAuthApplicationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplicationCreateDto from a JSON string
o_auth_application_create_dto_instance = OAuthApplicationCreateDto.from_json(json)
# print the JSON string representation of the object
print(OAuthApplicationCreateDto.to_json())

# convert the object into a dict
o_auth_application_create_dto_dict = o_auth_application_create_dto_instance.to_dict()
# create an instance of OAuthApplicationCreateDto from a dict
o_auth_application_create_dto_from_dict = OAuthApplicationCreateDto.from_dict(o_auth_application_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


