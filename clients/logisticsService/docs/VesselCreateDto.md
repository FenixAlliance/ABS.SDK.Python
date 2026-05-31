# VesselCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**imo_number** | **str** |  | [optional] 
**mmsi_number** | **str** |  | [optional] 
**call_sign** | **str** |  | [optional] 
**flag_country_id** | **str** |  | [optional] 
**vessel_type** | **str** |  | [optional] 
**vessel_status** | **str** |  | [optional] 
**gross_tonnage** | **float** |  | [optional] 
**deadweight_tonnage** | **float** |  | [optional] 
**teu_capacity** | **int** |  | [optional] 
**length_meters** | **float** |  | [optional] 
**beam_meters** | **float** |  | [optional] 
**draft_meters** | **float** |  | [optional] 
**year_built** | **int** |  | [optional] 
**shipping_courier_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.vessel_create_dto import VesselCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of VesselCreateDto from a JSON string
vessel_create_dto_instance = VesselCreateDto.from_json(json)
# print the JSON string representation of the object
print(VesselCreateDto.to_json())

# convert the object into a dict
vessel_create_dto_dict = vessel_create_dto_instance.to_dict()
# create an instance of VesselCreateDto from a dict
vessel_create_dto_from_dict = VesselCreateDto.from_dict(vessel_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


