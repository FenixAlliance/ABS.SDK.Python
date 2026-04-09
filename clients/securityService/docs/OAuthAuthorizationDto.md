# OAuthAuthorizationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**concurrency_token** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**properties** | **str** |  | [optional] 
**scopes** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**tokens_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_authorization_dto import OAuthAuthorizationDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAuthorizationDto from a JSON string
o_auth_authorization_dto_instance = OAuthAuthorizationDto.from_json(json)
# print the JSON string representation of the object
print(OAuthAuthorizationDto.to_json())

# convert the object into a dict
o_auth_authorization_dto_dict = o_auth_authorization_dto_instance.to_dict()
# create an instance of OAuthAuthorizationDto from a dict
o_auth_authorization_dto_from_dict = OAuthAuthorizationDto.from_dict(o_auth_authorization_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


