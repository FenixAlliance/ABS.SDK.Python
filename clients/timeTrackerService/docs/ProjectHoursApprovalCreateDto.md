# ProjectHoursApprovalCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**requester_contact_id** | **str** |  | [optional] 
**approver_contact_id** | **str** |  | [optional] 
**project_period_id** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_hours_approval_create_dto import ProjectHoursApprovalCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectHoursApprovalCreateDto from a JSON string
project_hours_approval_create_dto_instance = ProjectHoursApprovalCreateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectHoursApprovalCreateDto.to_json())

# convert the object into a dict
project_hours_approval_create_dto_dict = project_hours_approval_create_dto_instance.to_dict()
# create an instance of ProjectHoursApprovalCreateDto from a dict
project_hours_approval_create_dto_from_dict = ProjectHoursApprovalCreateDto.from_dict(project_hours_approval_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


