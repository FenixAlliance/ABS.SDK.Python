# JobTitleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gross_pay** | **float** |  | [optional] 
**net_salary** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.job_title_dto import JobTitleDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobTitleDto from a JSON string
job_title_dto_instance = JobTitleDto.from_json(json)
# print the JSON string representation of the object
print(JobTitleDto.to_json())

# convert the object into a dict
job_title_dto_dict = job_title_dto_instance.to_dict()
# create an instance of JobTitleDto from a dict
job_title_dto_from_dict = JobTitleDto.from_dict(job_title_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


