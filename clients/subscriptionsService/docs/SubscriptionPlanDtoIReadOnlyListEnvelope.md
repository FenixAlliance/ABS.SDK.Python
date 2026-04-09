# SubscriptionPlanDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SubscriptionPlanDto]**](SubscriptionPlanDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscription_plan_dto_i_read_only_list_envelope import SubscriptionPlanDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlanDtoIReadOnlyListEnvelope from a JSON string
subscription_plan_dto_i_read_only_list_envelope_instance = SubscriptionPlanDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPlanDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
subscription_plan_dto_i_read_only_list_envelope_dict = subscription_plan_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of SubscriptionPlanDtoIReadOnlyListEnvelope from a dict
subscription_plan_dto_i_read_only_list_envelope_from_dict = SubscriptionPlanDtoIReadOnlyListEnvelope.from_dict(subscription_plan_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


