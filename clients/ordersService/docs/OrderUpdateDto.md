# OrderUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**billing_location_id** | **str** |  | [optional] 
**shipping_location_id** | **str** |  | [optional] 
**shipping_method_id** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**total_amount_in_usd** | **float** |  | [optional] 
**total_taxes_in_usd** | **float** |  | [optional] 
**receiver_tenant_id** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**payment_term_id** | **str** |  | [optional] 
**quote_status** | **str** |  | [optional] 
**effective_to** | **datetime** |  | [optional] 
**effective_from** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.order_update_dto import OrderUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdateDto from a JSON string
order_update_dto_instance = OrderUpdateDto.from_json(json)
# print the JSON string representation of the object
print(OrderUpdateDto.to_json())

# convert the object into a dict
order_update_dto_dict = order_update_dto_instance.to_dict()
# create an instance of OrderUpdateDto from a dict
order_update_dto_from_dict = OrderUpdateDto.from_dict(order_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


