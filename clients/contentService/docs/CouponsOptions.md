# CouponsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_coupons** | **bool** |  | [optional] 
**calculate_coupons_secuentially** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.coupons_options import CouponsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CouponsOptions from a JSON string
coupons_options_instance = CouponsOptions.from_json(json)
# print the JSON string representation of the object
print(CouponsOptions.to_json())

# convert the object into a dict
coupons_options_dict = coupons_options_instance.to_dict()
# create an instance of CouponsOptions from a dict
coupons_options_from_dict = CouponsOptions.from_dict(coupons_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


