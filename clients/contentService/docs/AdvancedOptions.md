# AdvancedOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_page_id** | **str** |  | [optional] 
**cart_page_id** | **str** |  | [optional] 
**checkout_page_id** | **str** |  | [optional] 
**privacy_policy_page_id** | **str** |  | [optional] 
**customer_account_page_id** | **str** |  | [optional] 
**terms_and_conditions_page_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.advanced_options import AdvancedOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedOptions from a JSON string
advanced_options_instance = AdvancedOptions.from_json(json)
# print the JSON string representation of the object
print(AdvancedOptions.to_json())

# convert the object into a dict
advanced_options_dict = advanced_options_instance.to_dict()
# create an instance of AdvancedOptions from a dict
advanced_options_from_dict = AdvancedOptions.from_dict(advanced_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


