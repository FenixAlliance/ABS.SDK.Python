# ShippingLabelUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_code** | **str** |  | [optional] 
**expected_delivery** | **datetime** |  | [optional] 
**location_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**shipping_courier_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_label_update_dto import ShippingLabelUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingLabelUpdateDto from a JSON string
shipping_label_update_dto_instance = ShippingLabelUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingLabelUpdateDto.to_json())

# convert the object into a dict
shipping_label_update_dto_dict = shipping_label_update_dto_instance.to_dict()
# create an instance of ShippingLabelUpdateDto from a dict
shipping_label_update_dto_from_dict = ShippingLabelUpdateDto.from_dict(shipping_label_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


