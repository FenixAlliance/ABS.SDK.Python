# ShippingCourierUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_courier_update_dto import ShippingCourierUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCourierUpdateDto from a JSON string
shipping_courier_update_dto_instance = ShippingCourierUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingCourierUpdateDto.to_json())

# convert the object into a dict
shipping_courier_update_dto_dict = shipping_courier_update_dto_instance.to_dict()
# create an instance of ShippingCourierUpdateDto from a dict
shipping_courier_update_dto_from_dict = ShippingCourierUpdateDto.from_dict(shipping_courier_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


