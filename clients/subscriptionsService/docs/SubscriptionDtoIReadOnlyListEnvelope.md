# SubscriptionDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SubscriptionDto]**](SubscriptionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscription_dto_i_read_only_list_envelope import SubscriptionDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDtoIReadOnlyListEnvelope from a JSON string
subscription_dto_i_read_only_list_envelope_instance = SubscriptionDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
subscription_dto_i_read_only_list_envelope_dict = subscription_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of SubscriptionDtoIReadOnlyListEnvelope from a dict
subscription_dto_i_read_only_list_envelope_from_dict = SubscriptionDtoIReadOnlyListEnvelope.from_dict(subscription_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


