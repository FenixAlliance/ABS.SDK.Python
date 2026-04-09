# SubscriptionsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drip_downloadable_content** | **bool** |  | [optional] 
**retry_failed_payments** | **bool** |  | [optional] 
**allow0_initial_checkout** | **bool** |  | [optional] 
**allow_mixed_checkout** | **bool** |  | [optional] 
**synchronise_renewals** | **bool** |  | [optional] 
**add_to_cart_button_text** | **str** |  | [optional] 
**place_order_button_text** | **str** |  | [optional] 
**new_subscriber_role** | **str** |  | [optional] 
**inactive_subscriber_role** | **str** |  | [optional] 
**enable_automatic_payments** | **int** |  | [optional] 
**enable_manual_renewals** | **int** |  | [optional] 
**display_auto_renewal_toggle** | **int** |  | [optional] 
**accept_early_renewals** | **int** |  | [optional] 
**customer_suspensions** | **int** |  | [optional] 
**enable_subscription_switching_between_groups** | **int** |  | [optional] 
**enable_subscription_switching_between_variations** | **int** |  | [optional] 
**prorate_first_renewal** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.subscriptions_options import SubscriptionsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsOptions from a JSON string
subscriptions_options_instance = SubscriptionsOptions.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsOptions.to_json())

# convert the object into a dict
subscriptions_options_dict = subscriptions_options_instance.to_dict()
# create an instance of SubscriptionsOptions from a dict
subscriptions_options_from_dict = SubscriptionsOptions.from_dict(subscriptions_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


