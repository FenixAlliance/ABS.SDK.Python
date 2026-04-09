# SocialPostDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**social_profile_name** | **str** |  | [optional] 
**social_profile_avatar_url** | **str** |  | [optional] 
**comments_count** | **int** |  | [optional] 
**reactions_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_dto import SocialPostDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostDto from a JSON string
social_post_dto_instance = SocialPostDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostDto.to_json())

# convert the object into a dict
social_post_dto_dict = social_post_dto_instance.to_dict()
# create an instance of SocialPostDto from a dict
social_post_dto_from_dict = SocialPostDto.from_dict(social_post_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


