# MaintenanceVisitDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[MaintenanceVisitDto]**](MaintenanceVisitDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.maintenance_visit_dto_list_envelope import MaintenanceVisitDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceVisitDtoListEnvelope from a JSON string
maintenance_visit_dto_list_envelope_instance = MaintenanceVisitDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(MaintenanceVisitDtoListEnvelope.to_json())

# convert the object into a dict
maintenance_visit_dto_list_envelope_dict = maintenance_visit_dto_list_envelope_instance.to_dict()
# create an instance of MaintenanceVisitDtoListEnvelope from a dict
maintenance_visit_dto_list_envelope_from_dict = MaintenanceVisitDtoListEnvelope.from_dict(maintenance_visit_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


