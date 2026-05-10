# ShippingClassUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_class_update_dto import ShippingClassUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingClassUpdateDto from a JSON string
shipping_class_update_dto_instance = ShippingClassUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingClassUpdateDto.to_json())

# convert the object into a dict
shipping_class_update_dto_dict = shipping_class_update_dto_instance.to_dict()
# create an instance of ShippingClassUpdateDto from a dict
shipping_class_update_dto_from_dict = ShippingClassUpdateDto.from_dict(shipping_class_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


