# SocialPostBucketDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_bucket_dto import SocialPostBucketDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostBucketDto from a JSON string
social_post_bucket_dto_instance = SocialPostBucketDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostBucketDto.to_json())

# convert the object into a dict
social_post_bucket_dto_dict = social_post_bucket_dto_instance.to_dict()
# create an instance of SocialPostBucketDto from a dict
social_post_bucket_dto_from_dict = SocialPostBucketDto.from_dict(social_post_bucket_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


