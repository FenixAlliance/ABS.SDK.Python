# JobTitleDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**JobTitleDto**](JobTitleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.job_title_dto_envelope import JobTitleDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of JobTitleDtoEnvelope from a JSON string
job_title_dto_envelope_instance = JobTitleDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(JobTitleDtoEnvelope.to_json())

# convert the object into a dict
job_title_dto_envelope_dict = job_title_dto_envelope_instance.to_dict()
# create an instance of JobTitleDtoEnvelope from a dict
job_title_dto_envelope_from_dict = JobTitleDtoEnvelope.from_dict(job_title_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


