# SocialPostBucketUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_bucket_update_dto import SocialPostBucketUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostBucketUpdateDto from a JSON string
social_post_bucket_update_dto_instance = SocialPostBucketUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostBucketUpdateDto.to_json())

# convert the object into a dict
social_post_bucket_update_dto_dict = social_post_bucket_update_dto_instance.to_dict()
# create an instance of SocialPostBucketUpdateDto from a dict
social_post_bucket_update_dto_from_dict = SocialPostBucketUpdateDto.from_dict(social_post_bucket_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


