# RoadWaybillCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**document_number** | **str** |  | [optional] 
**road_waybill_type** | **str** |  | [optional] 
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
**freight_terms** | **str** |  | [optional] 
**freight_amount** | **float** |  | [optional] 
**freight_currency_id** | **str** |  | [optional] 
**total_gross_weight_kg** | **float** |  | [optional] 
**total_packages** | **int** |  | [optional] 
**total_volume_m3** | **float** |  | [optional] 
**adr_dangerous_goods** | **bool** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**truck_trip_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.road_waybill_create_dto import RoadWaybillCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoadWaybillCreateDto from a JSON string
road_waybill_create_dto_instance = RoadWaybillCreateDto.from_json(json)
# print the JSON string representation of the object
print(RoadWaybillCreateDto.to_json())

# convert the object into a dict
road_waybill_create_dto_dict = road_waybill_create_dto_instance.to_dict()
# create an instance of RoadWaybillCreateDto from a dict
road_waybill_create_dto_from_dict = RoadWaybillCreateDto.from_dict(road_waybill_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


