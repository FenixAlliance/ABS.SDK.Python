# DealUnitUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**payment_term_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**receiver_tenant_id** | **str** |  | [optional] 
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
**ordered** | **bool** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**deal_unit_feed_id** | **str** |  | [optional] 
**deal_unit_flow_id** | **str** |  | [optional] 
**deal_unit_flow_stage_id** | **str** |  | [optional] 
**partner_created** | **bool** |  | [optional] 
**partner_collaboration** | **bool** |  | [optional] 
**proposed_solution** | **str** |  | [optional] 
**current_situation** | **str** |  | [optional] 
**customer_need** | **str** |  | [optional] 
**won_date** | **datetime** |  | [optional] 
**lost_date** | **datetime** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**delivered_date** | **datetime** |  | [optional] 
**closed_timestamp** | **datetime** |  | [optional] 
**expected_close_date** | **datetime** |  | [optional] 
**deal_unit_status** | **int** |  | [optional] 
**deal_unit_purchase_process** | **int** |  | [optional] 
**deal_unit_forecast_category** | **int** |  | [optional] 
**deal_unit_amounts_calculation** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_update_dto import DealUnitUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitUpdateDto from a JSON string
deal_unit_update_dto_instance = DealUnitUpdateDto.from_json(json)
# print the JSON string representation of the object
print(DealUnitUpdateDto.to_json())

# convert the object into a dict
deal_unit_update_dto_dict = deal_unit_update_dto_instance.to_dict()
# create an instance of DealUnitUpdateDto from a dict
deal_unit_update_dto_from_dict = DealUnitUpdateDto.from_dict(deal_unit_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


