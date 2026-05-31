# AppraisalWorkflowUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_workflow_update_dto import AppraisalWorkflowUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalWorkflowUpdateDto from a JSON string
appraisal_workflow_update_dto_instance = AppraisalWorkflowUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AppraisalWorkflowUpdateDto.to_json())

# convert the object into a dict
appraisal_workflow_update_dto_dict = appraisal_workflow_update_dto_instance.to_dict()
# create an instance of AppraisalWorkflowUpdateDto from a dict
appraisal_workflow_update_dto_from_dict = AppraisalWorkflowUpdateDto.from_dict(appraisal_workflow_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


