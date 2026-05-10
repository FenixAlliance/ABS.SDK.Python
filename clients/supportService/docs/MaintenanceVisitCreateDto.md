# MaintenanceVisitCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.maintenance_visit_create_dto import MaintenanceVisitCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceVisitCreateDto from a JSON string
maintenance_visit_create_dto_instance = MaintenanceVisitCreateDto.from_json(json)
# print the JSON string representation of the object
print(MaintenanceVisitCreateDto.to_json())

# convert the object into a dict
maintenance_visit_create_dto_dict = maintenance_visit_create_dto_instance.to_dict()
# create an instance of MaintenanceVisitCreateDto from a dict
maintenance_visit_create_dto_from_dict = MaintenanceVisitCreateDto.from_dict(maintenance_visit_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


