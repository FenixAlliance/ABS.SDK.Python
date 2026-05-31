# RoadWaybillDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**document_number** | **str** |  | [optional] 
**road_waybill_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**shipper_contact_id** | **str** |  | [optional] 
**consignee_contact_id** | **str** |  | [optional] 
**carrier_id** | **str** |  | [optional] 
**successive_carriers** | **str** |  | [optional] 
**truck_id** | **str** |  | [optional] 
**truck_driver_id** | **str** |  | [optional] 
**vehicle_registration** | **str** |  | [optional] 
**trailer_registration** | **str** |  | [optional] 
**place_of_taking_over** | **str** |  | [optional] 
**place_of_taking_over_port_id** | **str** |  | [optional] 
**place_of_delivery** | **str** |  | [optional] 
**place_of_delivery_port_id** | **str** |  | [optional] 
**date_of_taking_over** | **datetime** |  | [optional] 
**date_of_delivery** | **datetime** |  | [optional] 
**freight_terms** | **str** |  | [optional] 
**freight_amount** | **float** |  | [optional] 
**freight_currency_id** | **str** |  | [optional] 
**total_gross_weight_kg** | **float** |  | [optional] 
**total_packages** | **int** |  | [optional] 
**total_volume_m3** | **float** |  | [optional] 
**adr_dangerous_goods** | **bool** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**sender_signed_date** | **datetime** |  | [optional] 
**carrier_signed_date** | **datetime** |  | [optional] 
**consignee_signed_date** | **datetime** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**truck_trip_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**lines** | [**List[WaybillLineDto]**](WaybillLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.road_waybill_dto import RoadWaybillDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoadWaybillDto from a JSON string
road_waybill_dto_instance = RoadWaybillDto.from_json(json)
# print the JSON string representation of the object
print(RoadWaybillDto.to_json())

# convert the object into a dict
road_waybill_dto_dict = road_waybill_dto_instance.to_dict()
# create an instance of RoadWaybillDto from a dict
road_waybill_dto_from_dict = RoadWaybillDto.from_dict(road_waybill_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


