# MaintenanceVisitDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**MaintenanceVisitDto**](MaintenanceVisitDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.maintenance_visit_dto_envelope import MaintenanceVisitDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceVisitDtoEnvelope from a JSON string
maintenance_visit_dto_envelope_instance = MaintenanceVisitDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(MaintenanceVisitDtoEnvelope.to_json())

# convert the object into a dict
maintenance_visit_dto_envelope_dict = maintenance_visit_dto_envelope_instance.to_dict()
# create an instance of MaintenanceVisitDtoEnvelope from a dict
maintenance_visit_dto_envelope_from_dict = MaintenanceVisitDtoEnvelope.from_dict(maintenance_visit_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


