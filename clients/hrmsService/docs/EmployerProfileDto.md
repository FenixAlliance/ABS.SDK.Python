# EmployerProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.employer_profile_dto import EmployerProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployerProfileDto from a JSON string
employer_profile_dto_instance = EmployerProfileDto.from_json(json)
# print the JSON string representation of the object
print(EmployerProfileDto.to_json())

# convert the object into a dict
employer_profile_dto_dict = employer_profile_dto_instance.to_dict()
# create an instance of EmployerProfileDto from a dict
employer_profile_dto_from_dict = EmployerProfileDto.from_dict(employer_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


