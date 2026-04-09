# SocialReactionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**reaction** | **str** |  | [optional] 
**reaction_value** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_reaction_create_dto import SocialReactionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialReactionCreateDto from a JSON string
social_reaction_create_dto_instance = SocialReactionCreateDto.from_json(json)
# print the JSON string representation of the object
print(SocialReactionCreateDto.to_json())

# convert the object into a dict
social_reaction_create_dto_dict = social_reaction_create_dto_instance.to_dict()
# create an instance of SocialReactionCreateDto from a dict
social_reaction_create_dto_from_dict = SocialReactionCreateDto.from_dict(social_reaction_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


