# ProjectHoursApprovalStatusUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_status** | **int** |  | [optional] 
**comments** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_hours_approval_status_update_dto import ProjectHoursApprovalStatusUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectHoursApprovalStatusUpdateDto from a JSON string
project_hours_approval_status_update_dto_instance = ProjectHoursApprovalStatusUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectHoursApprovalStatusUpdateDto.to_json())

# convert the object into a dict
project_hours_approval_status_update_dto_dict = project_hours_approval_status_update_dto_instance.to_dict()
# create an instance of ProjectHoursApprovalStatusUpdateDto from a dict
project_hours_approval_status_update_dto_from_dict = ProjectHoursApprovalStatusUpdateDto.from_dict(project_hours_approval_status_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


