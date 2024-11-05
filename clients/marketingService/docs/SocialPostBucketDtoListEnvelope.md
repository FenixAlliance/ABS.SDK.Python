# SocialPostBucketDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SocialPostBucketDto]**](SocialPostBucketDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_post_bucket_dto_list_envelope import SocialPostBucketDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostBucketDtoListEnvelope from a JSON string
social_post_bucket_dto_list_envelope_instance = SocialPostBucketDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialPostBucketDtoListEnvelope.to_json())

# convert the object into a dict
social_post_bucket_dto_list_envelope_dict = social_post_bucket_dto_list_envelope_instance.to_dict()
# create an instance of SocialPostBucketDtoListEnvelope from a dict
social_post_bucket_dto_list_envelope_from_dict = SocialPostBucketDtoListEnvelope.from_dict(social_post_bucket_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


