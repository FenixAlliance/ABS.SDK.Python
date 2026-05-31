# AirwayBillCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**document_number** | **str** |  | [optional] 
**airway_bill_type** | **str** |  | [optional] 
**master_awb_number** | **str** |  | [optional] 
**shipper_contact_id** | **str** |  | [optional] 
**consignee_contact_id** | **str** |  | [optional] 
**notify_party_contact_id** | **str** |  | [optional] 
**carrier_id** | **str** |  | [optional] 
**airline_code** | **str** |  | [optional] 
**flight_number** | **str** |  | [optional] 
**airport_of_departure_code** | **str** |  | [optional] 
**airport_of_destination_code** | **str** |  | [optional] 
**departure_date** | **datetime** |  | [optional] 
**arrival_date** | **datetime** |  | [optional] 
**date_issued** | **datetime** |  | [optional] 
**freight_terms** | **str** |  | [optional] 
**freight_amount** | **float** |  | [optional] 
**freight_currency_id** | **str** |  | [optional] 
**chargeable_weight_kg** | **float** |  | [optional] 
**total_gross_weight_kg** | **float** |  | [optional] 
**total_packages** | **int** |  | [optional] 
**total_volume_m3** | **float** |  | [optional] 
**declared_value_for_carriage** | **float** |  | [optional] 
**declared_value_for_customs** | **float** |  | [optional] 
**insurance_amount** | **float** |  | [optional] 
**special_handling_codes** | **str** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.airway_bill_create_dto import AirwayBillCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayBillCreateDto from a JSON string
airway_bill_create_dto_instance = AirwayBillCreateDto.from_json(json)
# print the JSON string representation of the object
print(AirwayBillCreateDto.to_json())

# convert the object into a dict
airway_bill_create_dto_dict = airway_bill_create_dto_instance.to_dict()
# create an instance of AirwayBillCreateDto from a dict
airway_bill_create_dto_from_dict = AirwayBillCreateDto.from_dict(airway_bill_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


