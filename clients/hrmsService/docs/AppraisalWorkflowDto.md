# AppraisalWorkflowDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_workflow_dto import AppraisalWorkflowDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalWorkflowDto from a JSON string
appraisal_workflow_dto_instance = AppraisalWorkflowDto.from_json(json)
# print the JSON string representation of the object
print(AppraisalWorkflowDto.to_json())

# convert the object into a dict
appraisal_workflow_dto_dict = appraisal_workflow_dto_instance.to_dict()
# create an instance of AppraisalWorkflowDto from a dict
appraisal_workflow_dto_from_dict = AppraisalWorkflowDto.from_dict(appraisal_workflow_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


