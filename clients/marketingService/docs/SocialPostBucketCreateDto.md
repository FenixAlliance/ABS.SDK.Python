# SocialPostBucketCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_bucket_create_dto import SocialPostBucketCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostBucketCreateDto from a JSON string
social_post_bucket_create_dto_instance = SocialPostBucketCreateDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostBucketCreateDto.to_json())

# convert the object into a dict
social_post_bucket_create_dto_dict = social_post_bucket_create_dto_instance.to_dict()
# create an instance of SocialPostBucketCreateDto from a dict
social_post_bucket_create_dto_from_dict = SocialPostBucketCreateDto.from_dict(social_post_bucket_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


