# OrderCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**closed** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**payment_term_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
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
**cart_id** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**parent_order_id** | **str** |  | [optional] 
**shipping_method_id** | **str** |  | [optional] 
**billing_location_id** | **str** |  | [optional] 
**customer_notes** | **str** |  | [optional] 
**order_status** | **int** |  | [optional] 
**quote_status** | **int** |  | [optional] 
**freight_terms** | **int** |  | [optional] 
**receiver_tenant_id** | **str** |  | [optional] 
**shipping_location_id** | **str** |  | [optional] 
**qualified_identifier** | **str** |  | [optional] 
**total_taxes_in_usd** | **float** |  | [optional] 
**total_amount_in_usd** | **float** |  | [optional] 
**effective_to** | **datetime** |  | [optional] 
**effective_from** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.order_create_dto import OrderCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateDto from a JSON string
order_create_dto_instance = OrderCreateDto.from_json(json)
# print the JSON string representation of the object
print(OrderCreateDto.to_json())

# convert the object into a dict
order_create_dto_dict = order_create_dto_instance.to_dict()
# create an instance of OrderCreateDto from a dict
order_create_dto_from_dict = OrderCreateDto.from_dict(order_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


