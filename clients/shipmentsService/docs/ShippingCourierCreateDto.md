# ShippingCourierCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_courier_create_dto import ShippingCourierCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCourierCreateDto from a JSON string
shipping_courier_create_dto_instance = ShippingCourierCreateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingCourierCreateDto.to_json())

# convert the object into a dict
shipping_courier_create_dto_dict = shipping_courier_create_dto_instance.to_dict()
# create an instance of ShippingCourierCreateDto from a dict
shipping_courier_create_dto_from_dict = ShippingCourierCreateDto.from_dict(shipping_courier_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


