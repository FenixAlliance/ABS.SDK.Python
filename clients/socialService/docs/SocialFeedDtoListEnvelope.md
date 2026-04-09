# SocialFeedDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SocialFeedDto]**](SocialFeedDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_feed_dto_list_envelope import SocialFeedDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialFeedDtoListEnvelope from a JSON string
social_feed_dto_list_envelope_instance = SocialFeedDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialFeedDtoListEnvelope.to_json())

# convert the object into a dict
social_feed_dto_list_envelope_dict = social_feed_dto_list_envelope_instance.to_dict()
# create an instance of SocialFeedDtoListEnvelope from a dict
social_feed_dto_list_envelope_from_dict = SocialFeedDtoListEnvelope.from_dict(social_feed_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


