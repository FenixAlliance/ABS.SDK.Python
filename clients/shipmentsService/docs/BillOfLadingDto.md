# BillOfLadingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**bill_of_lading_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**bill_of_lading_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**is_negotiable** | **bool** |  | [optional] 
**is_clean** | **bool** |  | [optional] 
**number_of_originals** | **int** |  | [optional] 
**freight_payment_type** | **str** |  | [optional] 
**shipping_terms** | **str** |  | [optional] 
**freight_charges_description** | **str** |  | [optional] 
**declared_value_amount** | **float** |  | [optional] 
**declared_value_currency_id** | **str** |  | [optional] 
**issued_date** | **datetime** |  | [optional] 
**on_board_date** | **datetime** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**vessel_name** | **str** |  | [optional] 
**voyage_number** | **str** |  | [optional] 
**shipper_contact_id** | **str** |  | [optional] 
**consignee_contact_id** | **str** |  | [optional] 
**notify_party_contact_id** | **str** |  | [optional] 
**shipping_courier_id** | **str** |  | [optional] 
**port_of_loading_id** | **str** |  | [optional] 
**port_of_discharge_id** | **str** |  | [optional] 
**place_of_receipt_id** | **str** |  | [optional] 
**place_of_delivery_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**voyage_id** | **str** |  | [optional] 
**marks_and_numbers** | **str** |  | [optional] 
**total_packages** | **int** |  | [optional] 
**total_gross_weight_kg** | **float** |  | [optional] 
**total_volume_m3** | **float** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bill_of_lading_dto import BillOfLadingDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillOfLadingDto from a JSON string
bill_of_lading_dto_instance = BillOfLadingDto.from_json(json)
# print the JSON string representation of the object
print(BillOfLadingDto.to_json())

# convert the object into a dict
bill_of_lading_dto_dict = bill_of_lading_dto_instance.to_dict()
# create an instance of BillOfLadingDto from a dict
bill_of_lading_dto_from_dict = BillOfLadingDto.from_dict(bill_of_lading_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


