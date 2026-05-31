# TruckDriverCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**license_number** | **str** |  | [optional] 
**license_class** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**shipping_courier_id** | **str** |  | [optional] 
**adr_certified** | **bool** |  | [optional] 
**license_expiry_date** | **datetime** |  | [optional] 
**medical_exam_expiry_date** | **datetime** |  | [optional] 
**national_id_number** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.truck_driver_create_dto import TruckDriverCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TruckDriverCreateDto from a JSON string
truck_driver_create_dto_instance = TruckDriverCreateDto.from_json(json)
# print the JSON string representation of the object
print(TruckDriverCreateDto.to_json())

# convert the object into a dict
truck_driver_create_dto_dict = truck_driver_create_dto_instance.to_dict()
# create an instance of TruckDriverCreateDto from a dict
truck_driver_create_dto_from_dict = TruckDriverCreateDto.from_dict(truck_driver_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


