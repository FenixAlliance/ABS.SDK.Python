# EmailOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_name** | **str** |  | [optional] 
**from_email_address** | **str** |  | [optional] 
**header_image** | **str** |  | [optional] 
**footer_text** | **str** |  | [optional] 
**base_color** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**body_background_color** | **str** |  | [optional] 
**body_text_color** | **str** |  | [optional] 
**new_order_email_id** | **str** |  | [optional] 
**cancelled_order_email_id** | **str** |  | [optional] 
**failed_order_email_id** | **str** |  | [optional] 
**on_hold_order_email_id** | **str** |  | [optional] 
**processing_order_email_id** | **str** |  | [optional] 
**completed_order_email_id** | **str** |  | [optional] 
**refunded_order_email_id** | **str** |  | [optional] 
**order_details_email_id** | **str** |  | [optional] 
**customer_invoice_email_id** | **str** |  | [optional] 
**customer_note_email_id** | **str** |  | [optional] 
**password_reset_email_id** | **str** |  | [optional] 
**new_renewal_order_email_id** | **str** |  | [optional] 
**new_subscription_email_id** | **str** |  | [optional] 
**subscription_welcome_email_id** | **str** |  | [optional] 
**suspended_subscription_email_id** | **str** |  | [optional] 
**overdue_subscription_email_id** | **str** |  | [optional] 
**expired_subscription_email_id** | **str** |  | [optional] 
**switched_subscription_email_id** | **str** |  | [optional] 
**new_account_email_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_options import EmailOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EmailOptions from a JSON string
email_options_instance = EmailOptions.from_json(json)
# print the JSON string representation of the object
print(EmailOptions.to_json())

# convert the object into a dict
email_options_dict = email_options_instance.to_dict()
# create an instance of EmailOptions from a dict
email_options_from_dict = EmailOptions.from_dict(email_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


