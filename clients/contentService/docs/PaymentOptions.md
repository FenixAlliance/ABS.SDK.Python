# PaymentOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_methods** | [**List[PaymentMethod]**](PaymentMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_options import PaymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOptions from a JSON string
payment_options_instance = PaymentOptions.from_json(json)
# print the JSON string representation of the object
print(PaymentOptions.to_json())

# convert the object into a dict
payment_options_dict = payment_options_instance.to_dict()
# create an instance of PaymentOptions from a dict
payment_options_from_dict = PaymentOptions.from_dict(payment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


