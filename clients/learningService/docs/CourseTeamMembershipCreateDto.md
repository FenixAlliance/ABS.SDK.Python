# CourseTeamMembershipCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**course_id** | **str** |  | 
**instructor_profile_id** | **str** |  | 
**course_team_membership_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_team_membership_create_dto import CourseTeamMembershipCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseTeamMembershipCreateDto from a JSON string
course_team_membership_create_dto_instance = CourseTeamMembershipCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseTeamMembershipCreateDto.to_json())

# convert the object into a dict
course_team_membership_create_dto_dict = course_team_membership_create_dto_instance.to_dict()
# create an instance of CourseTeamMembershipCreateDto from a dict
course_team_membership_create_dto_from_dict = CourseTeamMembershipCreateDto.from_dict(course_team_membership_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


