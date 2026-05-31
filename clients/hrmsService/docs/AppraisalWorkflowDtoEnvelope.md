# AppraisalWorkflowDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AppraisalWorkflowDto**](AppraisalWorkflowDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_workflow_dto_envelope import AppraisalWorkflowDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalWorkflowDtoEnvelope from a JSON string
appraisal_workflow_dto_envelope_instance = AppraisalWorkflowDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AppraisalWorkflowDtoEnvelope.to_json())

# convert the object into a dict
appraisal_workflow_dto_envelope_dict = appraisal_workflow_dto_envelope_instance.to_dict()
# create an instance of AppraisalWorkflowDtoEnvelope from a dict
appraisal_workflow_dto_envelope_from_dict = AppraisalWorkflowDtoEnvelope.from_dict(appraisal_workflow_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


