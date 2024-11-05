# SocialPostBucketDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SocialPostBucketDto**](SocialPostBucketDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_post_bucket_dto_envelope import SocialPostBucketDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostBucketDtoEnvelope from a JSON string
social_post_bucket_dto_envelope_instance = SocialPostBucketDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialPostBucketDtoEnvelope.to_json())

# convert the object into a dict
social_post_bucket_dto_envelope_dict = social_post_bucket_dto_envelope_instance.to_dict()
# create an instance of SocialPostBucketDtoEnvelope from a dict
social_post_bucket_dto_envelope_from_dict = SocialPostBucketDtoEnvelope.from_dict(social_post_bucket_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


