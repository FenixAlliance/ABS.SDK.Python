# SocialPostCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**social_feed_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_create_dto import SocialPostCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostCreateDto from a JSON string
social_post_create_dto_instance = SocialPostCreateDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostCreateDto.to_json())

# convert the object into a dict
social_post_create_dto_dict = social_post_create_dto_instance.to_dict()
# create an instance of SocialPostCreateDto from a dict
social_post_create_dto_from_dict = SocialPostCreateDto.from_dict(social_post_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


