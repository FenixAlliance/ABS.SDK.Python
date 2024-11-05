# EmployerProfileCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.employer_profile_create_dto import EmployerProfileCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployerProfileCreateDto from a JSON string
employer_profile_create_dto_instance = EmployerProfileCreateDto.from_json(json)
# print the JSON string representation of the object
print(EmployerProfileCreateDto.to_json())

# convert the object into a dict
employer_profile_create_dto_dict = employer_profile_create_dto_instance.to_dict()
# create an instance of EmployerProfileCreateDto from a dict
employer_profile_create_dto_from_dict = EmployerProfileCreateDto.from_dict(employer_profile_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


