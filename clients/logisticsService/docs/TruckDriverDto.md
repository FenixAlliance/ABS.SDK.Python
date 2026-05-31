# TruckDriverDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**national_id_number** | **str** |  | [optional] 
**license_number** | **str** |  | [optional] 
**license_class** | **str** |  | [optional] 
**license_expiry_date** | **datetime** |  | [optional] 
**adr_certified** | **bool** |  | [optional] 
**adr_certificate_expiry_date** | **datetime** |  | [optional] 
**medical_exam_expiry_date** | **datetime** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**shipping_courier_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.truck_driver_dto import TruckDriverDto

# TODO update the JSON string below
json = "{}"
# create an instance of TruckDriverDto from a JSON string
truck_driver_dto_instance = TruckDriverDto.from_json(json)
# print the JSON string representation of the object
print(TruckDriverDto.to_json())

# convert the object into a dict
truck_driver_dto_dict = truck_driver_dto_instance.to_dict()
# create an instance of TruckDriverDto from a dict
truck_driver_dto_from_dict = TruckDriverDto.from_dict(truck_driver_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


