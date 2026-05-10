# ItemShippingPolicyCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 
**code** | **str** |  | 
**is_express_shipment_policy** | **bool** |  | [optional] 
**is_free** | **bool** |  | [optional] 
**reduce** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**allow_international** | **bool** |  | [optional] 
**hours** | **int** |  | [optional] 
**days** | **int** |  | [optional] 
**weeks** | **int** |  | [optional] 
**months** | **int** |  | [optional] 
**years** | **int** |  | [optional] 
**value** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**currency_id** | **str** |  | 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**custom_state** | **str** |  | [optional] 
**custom_city** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**shipping_courier_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_shipping_policy_create_dto import ItemShippingPolicyCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemShippingPolicyCreateDto from a JSON string
item_shipping_policy_create_dto_instance = ItemShippingPolicyCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemShippingPolicyCreateDto.to_json())

# convert the object into a dict
item_shipping_policy_create_dto_dict = item_shipping_policy_create_dto_instance.to_dict()
# create an instance of ItemShippingPolicyCreateDto from a dict
item_shipping_policy_create_dto_from_dict = ItemShippingPolicyCreateDto.from_dict(item_shipping_policy_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


