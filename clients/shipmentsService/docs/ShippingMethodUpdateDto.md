# ShippingMethodUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**taxable** | **bool** |  | [optional] 
**tax_included** | **bool** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**shipping_class_calculation_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_method_update_dto import ShippingMethodUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMethodUpdateDto from a JSON string
shipping_method_update_dto_instance = ShippingMethodUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingMethodUpdateDto.to_json())

# convert the object into a dict
shipping_method_update_dto_dict = shipping_method_update_dto_instance.to_dict()
# create an instance of ShippingMethodUpdateDto from a dict
shipping_method_update_dto_from_dict = ShippingMethodUpdateDto.from_dict(shipping_method_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


