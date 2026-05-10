# ShippingLabelCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tracking_code** | **str** |  | 
**expected_delivery** | **datetime** |  | [optional] 
**location_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**shipping_courier_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_label_create_dto import ShippingLabelCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingLabelCreateDto from a JSON string
shipping_label_create_dto_instance = ShippingLabelCreateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingLabelCreateDto.to_json())

# convert the object into a dict
shipping_label_create_dto_dict = shipping_label_create_dto_instance.to_dict()
# create an instance of ShippingLabelCreateDto from a dict
shipping_label_create_dto_from_dict = ShippingLabelCreateDto.from_dict(shipping_label_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


