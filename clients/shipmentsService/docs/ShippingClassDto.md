# ShippingClassDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_class_dto import ShippingClassDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingClassDto from a JSON string
shipping_class_dto_instance = ShippingClassDto.from_json(json)
# print the JSON string representation of the object
print(ShippingClassDto.to_json())

# convert the object into a dict
shipping_class_dto_dict = shipping_class_dto_instance.to_dict()
# create an instance of ShippingClassDto from a dict
shipping_class_dto_from_dict = ShippingClassDto.from_dict(shipping_class_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


