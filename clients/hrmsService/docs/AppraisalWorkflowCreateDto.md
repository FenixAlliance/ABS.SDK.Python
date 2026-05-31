# AppraisalWorkflowCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_workflow_create_dto import AppraisalWorkflowCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalWorkflowCreateDto from a JSON string
appraisal_workflow_create_dto_instance = AppraisalWorkflowCreateDto.from_json(json)
# print the JSON string representation of the object
print(AppraisalWorkflowCreateDto.to_json())

# convert the object into a dict
appraisal_workflow_create_dto_dict = appraisal_workflow_create_dto_instance.to_dict()
# create an instance of AppraisalWorkflowCreateDto from a dict
appraisal_workflow_create_dto_from_dict = AppraisalWorkflowCreateDto.from_dict(appraisal_workflow_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


