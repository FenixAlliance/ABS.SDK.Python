# SocialMediaPostCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**social_post_bucket_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_media_post_create_dto import SocialMediaPostCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialMediaPostCreateDto from a JSON string
social_media_post_create_dto_instance = SocialMediaPostCreateDto.from_json(json)
# print the JSON string representation of the object
print(SocialMediaPostCreateDto.to_json())

# convert the object into a dict
social_media_post_create_dto_dict = social_media_post_create_dto_instance.to_dict()
# create an instance of SocialMediaPostCreateDto from a dict
social_media_post_create_dto_from_dict = SocialMediaPostCreateDto.from_dict(social_media_post_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


