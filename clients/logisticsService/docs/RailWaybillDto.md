# RailWaybillDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**document_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**shipper_contact_id** | **str** |  | [optional] 
**consignee_contact_id** | **str** |  | [optional] 
**carrier_id** | **str** |  | [optional] 
**rail_operator_name** | **str** |  | [optional] 
**station_of_departure** | **str** |  | [optional] 
**station_of_departure_code** | **str** |  | [optional] 
**station_of_destination** | **str** |  | [optional] 
**station_of_destination_code** | **str** |  | [optional] 
**prescribed_route** | **str** |  | [optional] 
**wagon_numbers** | **str** |  | [optional] 
**date_of_acceptance** | **datetime** |  | [optional] 
**date_of_delivery** | **datetime** |  | [optional] 
**freight_terms** | **str** |  | [optional] 
**freight_amount** | **float** |  | [optional] 
**freight_currency_id** | **str** |  | [optional] 
**total_gross_weight_kg** | **float** |  | [optional] 
**total_packages** | **int** |  | [optional] 
**total_volume_m3** | **float** |  | [optional] 
**customs_formalities** | **str** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**sender_signed_date** | **datetime** |  | [optional] 
**carrier_signed_date** | **datetime** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**lines** | [**List[WaybillLineDto]**](WaybillLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.rail_waybill_dto import RailWaybillDto

# TODO update the JSON string below
json = "{}"
# create an instance of RailWaybillDto from a JSON string
rail_waybill_dto_instance = RailWaybillDto.from_json(json)
# print the JSON string representation of the object
print(RailWaybillDto.to_json())

# convert the object into a dict
rail_waybill_dto_dict = rail_waybill_dto_instance.to_dict()
# create an instance of RailWaybillDto from a dict
rail_waybill_dto_from_dict = RailWaybillDto.from_dict(rail_waybill_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


