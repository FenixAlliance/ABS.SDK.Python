# OAuthApplicationUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**consent_type** | **str** |  | [optional] 
**permissions** | **str** |  | [optional] 
**requirements** | **str** |  | [optional] 
**redirect_uris** | **str** |  | [optional] 
**post_logout_redirect_uris** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_application_update_dto import OAuthApplicationUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplicationUpdateDto from a JSON string
o_auth_application_update_dto_instance = OAuthApplicationUpdateDto.from_json(json)
# print the JSON string representation of the object
print(OAuthApplicationUpdateDto.to_json())

# convert the object into a dict
o_auth_application_update_dto_dict = o_auth_application_update_dto_instance.to_dict()
# create an instance of OAuthApplicationUpdateDto from a dict
o_auth_application_update_dto_from_dict = OAuthApplicationUpdateDto.from_dict(o_auth_application_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


