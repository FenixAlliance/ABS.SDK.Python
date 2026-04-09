# SubscriptionCreateDto


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
from openapi_client.models.subscription_create_dto import SubscriptionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCreateDto from a JSON string
subscription_create_dto_instance = SubscriptionCreateDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCreateDto.to_json())

# convert the object into a dict
subscription_create_dto_dict = subscription_create_dto_instance.to_dict()
# create an instance of SubscriptionCreateDto from a dict
subscription_create_dto_from_dict = SubscriptionCreateDto.from_dict(subscription_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


