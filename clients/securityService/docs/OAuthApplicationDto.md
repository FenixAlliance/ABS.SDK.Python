# OAuthApplicationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**application_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**concurrency_token** | **str** |  | [optional] 
**consent_type** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**display_names** | **str** |  | [optional] 
**permissions** | **str** |  | [optional] 
**post_logout_redirect_uris** | **str** |  | [optional] 
**properties** | **str** |  | [optional] 
**redirect_uris** | **str** |  | [optional] 
**requirements** | **str** |  | [optional] 
**settings** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**business_application_id** | **str** |  | [optional] 
**authorizations_count** | **int** |  | [optional] 
**tokens_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_application_dto import OAuthApplicationDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplicationDto from a JSON string
o_auth_application_dto_instance = OAuthApplicationDto.from_json(json)
# print the JSON string representation of the object
print(OAuthApplicationDto.to_json())

# convert the object into a dict
o_auth_application_dto_dict = o_auth_application_dto_instance.to_dict()
# create an instance of OAuthApplicationDto from a dict
o_auth_application_dto_from_dict = OAuthApplicationDto.from_dict(o_auth_application_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


