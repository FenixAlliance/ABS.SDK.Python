# BillOfLadingUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_of_lading_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**bill_of_lading_type** | **str** |  | [optional] 
**is_negotiable** | **bool** |  | [optional] 
**is_clean** | **bool** |  | [optional] 
**number_of_originals** | **int** |  | [optional] 
**freight_payment_type** | **str** |  | [optional] 
**shipping_terms** | **str** |  | [optional] 
**freight_charges_description** | **str** |  | [optional] 
**declared_value_amount** | **float** |  | [optional] 
**declared_value_currency_id** | **str** |  | [optional] 
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

## Example

```python
from openapi_client.models.bill_of_lading_update_dto import BillOfLadingUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillOfLadingUpdateDto from a JSON string
bill_of_lading_update_dto_instance = BillOfLadingUpdateDto.from_json(json)
# print the JSON string representation of the object
print(BillOfLadingUpdateDto.to_json())

# convert the object into a dict
bill_of_lading_update_dto_dict = bill_of_lading_update_dto_instance.to_dict()
# create an instance of BillOfLadingUpdateDto from a dict
bill_of_lading_update_dto_from_dict = BillOfLadingUpdateDto.from_dict(bill_of_lading_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


