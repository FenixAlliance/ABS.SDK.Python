# SuiteLicenseAssignmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**assigned** | **bool** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**suite_license_id** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**available_seats** | **int** |  | [optional] 
**total_seats** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.suite_license_assignment_dto import SuiteLicenseAssignmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SuiteLicenseAssignmentDto from a JSON string
suite_license_assignment_dto_instance = SuiteLicenseAssignmentDto.from_json(json)
# print the JSON string representation of the object
print(SuiteLicenseAssignmentDto.to_json())

# convert the object into a dict
suite_license_assignment_dto_dict = suite_license_assignment_dto_instance.to_dict()
# create an instance of SuiteLicenseAssignmentDto from a dict
suite_license_assignment_dto_from_dict = SuiteLicenseAssignmentDto.from_dict(suite_license_assignment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


