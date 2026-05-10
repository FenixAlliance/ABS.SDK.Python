# ShippingMethodDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**taxable** | **bool** |  | [optional] 
**tax_included** | **bool** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**shipping_class_calculation_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_method_dto import ShippingMethodDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMethodDto from a JSON string
shipping_method_dto_instance = ShippingMethodDto.from_json(json)
# print the JSON string representation of the object
print(ShippingMethodDto.to_json())

# convert the object into a dict
shipping_method_dto_dict = shipping_method_dto_instance.to_dict()
# create an instance of ShippingMethodDto from a dict
shipping_method_dto_from_dict = ShippingMethodDto.from_dict(shipping_method_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


