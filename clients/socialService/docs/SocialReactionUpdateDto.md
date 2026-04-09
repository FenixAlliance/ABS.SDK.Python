# SocialReactionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**reaction** | **str** |  | [optional] 
**reaction_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_reaction_update_dto import SocialReactionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialReactionUpdateDto from a JSON string
social_reaction_update_dto_instance = SocialReactionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SocialReactionUpdateDto.to_json())

# convert the object into a dict
social_reaction_update_dto_dict = social_reaction_update_dto_instance.to_dict()
# create an instance of SocialReactionUpdateDto from a dict
social_reaction_update_dto_from_dict = SocialReactionUpdateDto.from_dict(social_reaction_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


