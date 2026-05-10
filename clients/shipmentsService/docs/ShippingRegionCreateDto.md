# ShippingRegionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**postal_codes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_region_create_dto import ShippingRegionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRegionCreateDto from a JSON string
shipping_region_create_dto_instance = ShippingRegionCreateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingRegionCreateDto.to_json())

# convert the object into a dict
shipping_region_create_dto_dict = shipping_region_create_dto_instance.to_dict()
# create an instance of ShippingRegionCreateDto from a dict
shipping_region_create_dto_from_dict = ShippingRegionCreateDto.from_dict(shipping_region_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


