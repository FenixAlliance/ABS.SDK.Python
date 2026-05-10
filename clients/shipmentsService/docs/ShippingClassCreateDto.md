# ShippingClassCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_class_create_dto import ShippingClassCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingClassCreateDto from a JSON string
shipping_class_create_dto_instance = ShippingClassCreateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingClassCreateDto.to_json())

# convert the object into a dict
shipping_class_create_dto_dict = shipping_class_create_dto_instance.to_dict()
# create an instance of ShippingClassCreateDto from a dict
shipping_class_create_dto_from_dict = ShippingClassCreateDto.from_dict(shipping_class_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


