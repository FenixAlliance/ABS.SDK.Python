# ShippingRegionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**postal_codes** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_region_dto import ShippingRegionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRegionDto from a JSON string
shipping_region_dto_instance = ShippingRegionDto.from_json(json)
# print the JSON string representation of the object
print(ShippingRegionDto.to_json())

# convert the object into a dict
shipping_region_dto_dict = shipping_region_dto_instance.to_dict()
# create an instance of ShippingRegionDto from a dict
shipping_region_dto_from_dict = ShippingRegionDto.from_dict(shipping_region_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


