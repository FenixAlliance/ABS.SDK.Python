# CourseTeamMembershipDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**course_id** | **str** |  | [optional] 
**instructor_profile_id** | **str** |  | [optional] 
**course_team_membership_type** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_team_membership_dto import CourseTeamMembershipDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseTeamMembershipDto from a JSON string
course_team_membership_dto_instance = CourseTeamMembershipDto.from_json(json)
# print the JSON string representation of the object
print(CourseTeamMembershipDto.to_json())

# convert the object into a dict
course_team_membership_dto_dict = course_team_membership_dto_instance.to_dict()
# create an instance of CourseTeamMembershipDto from a dict
course_team_membership_dto_from_dict = CourseTeamMembershipDto.from_dict(course_team_membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


