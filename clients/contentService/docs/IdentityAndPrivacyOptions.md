# IdentityAndPrivacyOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_guest_orders** | **bool** |  | [optional] 
**allow_guest_cart_recognition** | **bool** |  | [optional] 
**allow_remove_download_access_on_request** | **bool** |  | [optional] 
**allow_remove_personal_data_from_orders_on_request** | **bool** |  | [optional] 
**allow_remove_personal_data_from_subscriptions_on_request** | **bool** |  | [optional] 
**store_checkout_privacy_policy_notice** | **str** |  | [optional] 
**store_registration_privacy_policy_notice** | **str** |  | [optional] 
**default_customer_location** | **str** |  | [optional] 
**inactive_carts_retention_policy** | [**StoreDataRetentionPolicy**](StoreDataRetentionPolicy.md) |  | [optional] 
**pending_orders_retention_policy** | [**StoreDataRetentionPolicy**](StoreDataRetentionPolicy.md) |  | [optional] 
**failed_orders_retention_policy** | [**StoreDataRetentionPolicy**](StoreDataRetentionPolicy.md) |  | [optional] 
**cancelled_orders_retention_policy** | [**StoreDataRetentionPolicy**](StoreDataRetentionPolicy.md) |  | [optional] 
**completed_orders_retention_policy** | [**StoreDataRetentionPolicy**](StoreDataRetentionPolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.identity_and_privacy_options import IdentityAndPrivacyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAndPrivacyOptions from a JSON string
identity_and_privacy_options_instance = IdentityAndPrivacyOptions.from_json(json)
# print the JSON string representation of the object
print(IdentityAndPrivacyOptions.to_json())

# convert the object into a dict
identity_and_privacy_options_dict = identity_and_privacy_options_instance.to_dict()
# create an instance of IdentityAndPrivacyOptions from a dict
identity_and_privacy_options_from_dict = IdentityAndPrivacyOptions.from_dict(identity_and_privacy_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


