# TruckUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plate_number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**truck_type** | **str** |  | [optional] 
**max_payload_kg** | **float** |  | [optional] 
**teu_capacity** | **int** |  | [optional] 
**driver_name** | **str** |  | [optional] 
**driver_phone** | **str** |  | [optional] 
**driver_license_number** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_refrigerated** | **bool** |  | [optional] 
**shipping_courier_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.truck_update_dto import TruckUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TruckUpdateDto from a JSON string
truck_update_dto_instance = TruckUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TruckUpdateDto.to_json())

# convert the object into a dict
truck_update_dto_dict = truck_update_dto_instance.to_dict()
# create an instance of TruckUpdateDto from a dict
truck_update_dto_from_dict = TruckUpdateDto.from_dict(truck_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


