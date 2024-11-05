# SocialMediaPostUpdateDto


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
from openapi_client.models.social_media_post_update_dto import SocialMediaPostUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialMediaPostUpdateDto from a JSON string
social_media_post_update_dto_instance = SocialMediaPostUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SocialMediaPostUpdateDto.to_json())

# convert the object into a dict
social_media_post_update_dto_dict = social_media_post_update_dto_instance.to_dict()
# create an instance of SocialMediaPostUpdateDto from a dict
social_media_post_update_dto_from_dict = SocialMediaPostUpdateDto.from_dict(social_media_post_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


