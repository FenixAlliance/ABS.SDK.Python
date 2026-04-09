# SubscriptionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**subscription_plan_id** | **str** |  | [optional] 
**subscription_class** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.subscription_update_dto import SubscriptionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUpdateDto from a JSON string
subscription_update_dto_instance = SubscriptionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionUpdateDto.to_json())

# convert the object into a dict
subscription_update_dto_dict = subscription_update_dto_instance.to_dict()
# create an instance of SubscriptionUpdateDto from a dict
subscription_update_dto_from_dict = SubscriptionUpdateDto.from_dict(subscription_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


