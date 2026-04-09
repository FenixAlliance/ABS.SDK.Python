# SocialReactionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**reaction** | **str** |  | [optional] 
**reaction_value** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**social_profile_name** | **str** |  | [optional] 
**social_profile_avatar_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_reaction_dto import SocialReactionDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialReactionDto from a JSON string
social_reaction_dto_instance = SocialReactionDto.from_json(json)
# print the JSON string representation of the object
print(SocialReactionDto.to_json())

# convert the object into a dict
social_reaction_dto_dict = social_reaction_dto_instance.to_dict()
# create an instance of SocialReactionDto from a dict
social_reaction_dto_from_dict = SocialReactionDto.from_dict(social_reaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


