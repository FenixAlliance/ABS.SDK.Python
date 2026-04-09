# SocialGroupCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_group_create_dto import SocialGroupCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialGroupCreateDto from a JSON string
social_group_create_dto_instance = SocialGroupCreateDto.from_json(json)
# print the JSON string representation of the object
print(SocialGroupCreateDto.to_json())

# convert the object into a dict
social_group_create_dto_dict = social_group_create_dto_instance.to_dict()
# create an instance of SocialGroupCreateDto from a dict
social_group_create_dto_from_dict = SocialGroupCreateDto.from_dict(social_group_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


