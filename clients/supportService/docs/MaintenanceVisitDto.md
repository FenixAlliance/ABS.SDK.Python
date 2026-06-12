# MaintenanceVisitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.maintenance_visit_dto import MaintenanceVisitDto

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceVisitDto from a JSON string
maintenance_visit_dto_instance = MaintenanceVisitDto.from_json(json)
# print the JSON string representation of the object
print(MaintenanceVisitDto.to_json())

# convert the object into a dict
maintenance_visit_dto_dict = maintenance_visit_dto_instance.to_dict()
# create an instance of MaintenanceVisitDto from a dict
maintenance_visit_dto_from_dict = MaintenanceVisitDto.from_dict(maintenance_visit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


