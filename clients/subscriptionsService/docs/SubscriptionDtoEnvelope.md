# SubscriptionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SubscriptionDto**](SubscriptionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscription_dto_envelope import SubscriptionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDtoEnvelope from a JSON string
subscription_dto_envelope_instance = SubscriptionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDtoEnvelope.to_json())

# convert the object into a dict
subscription_dto_envelope_dict = subscription_dto_envelope_instance.to_dict()
# create an instance of SubscriptionDtoEnvelope from a dict
subscription_dto_envelope_from_dict = SubscriptionDtoEnvelope.from_dict(subscription_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


