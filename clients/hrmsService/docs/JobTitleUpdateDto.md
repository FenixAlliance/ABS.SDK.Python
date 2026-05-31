# JobTitleUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gross_pay** | **float** |  | [optional] 
**net_salary** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.job_title_update_dto import JobTitleUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobTitleUpdateDto from a JSON string
job_title_update_dto_instance = JobTitleUpdateDto.from_json(json)
# print the JSON string representation of the object
print(JobTitleUpdateDto.to_json())

# convert the object into a dict
job_title_update_dto_dict = job_title_update_dto_instance.to_dict()
# create an instance of JobTitleUpdateDto from a dict
job_title_update_dto_from_dict = JobTitleUpdateDto.from_dict(job_title_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


