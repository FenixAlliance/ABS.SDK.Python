# SuiteLicenseAssignmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SuiteLicenseAssignmentDto]**](SuiteLicenseAssignmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.suite_license_assignment_dto_list_envelope import SuiteLicenseAssignmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SuiteLicenseAssignmentDtoListEnvelope from a JSON string
suite_license_assignment_dto_list_envelope_instance = SuiteLicenseAssignmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SuiteLicenseAssignmentDtoListEnvelope.to_json())

# convert the object into a dict
suite_license_assignment_dto_list_envelope_dict = suite_license_assignment_dto_list_envelope_instance.to_dict()
# create an instance of SuiteLicenseAssignmentDtoListEnvelope from a dict
suite_license_assignment_dto_list_envelope_from_dict = SuiteLicenseAssignmentDtoListEnvelope.from_dict(suite_license_assignment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


