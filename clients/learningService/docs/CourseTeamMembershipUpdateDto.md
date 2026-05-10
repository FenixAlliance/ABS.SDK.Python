# CourseTeamMembershipUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructor_profile_id** | **str** |  | [optional] 
**course_team_membership_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_team_membership_update_dto import CourseTeamMembershipUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseTeamMembershipUpdateDto from a JSON string
course_team_membership_update_dto_instance = CourseTeamMembershipUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseTeamMembershipUpdateDto.to_json())

# convert the object into a dict
course_team_membership_update_dto_dict = course_team_membership_update_dto_instance.to_dict()
# create an instance of CourseTeamMembershipUpdateDto from a dict
course_team_membership_update_dto_from_dict = CourseTeamMembershipUpdateDto.from_dict(course_team_membership_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


