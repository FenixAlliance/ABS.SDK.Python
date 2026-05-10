# ShippingRegionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**postal_codes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_region_update_dto import ShippingRegionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRegionUpdateDto from a JSON string
shipping_region_update_dto_instance = ShippingRegionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingRegionUpdateDto.to_json())

# convert the object into a dict
shipping_region_update_dto_dict = shipping_region_update_dto_instance.to_dict()
# create an instance of ShippingRegionUpdateDto from a dict
shipping_region_update_dto_from_dict = ShippingRegionUpdateDto.from_dict(shipping_region_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


