# AppraisalStageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**appraisal_workflow_id** | **str** |  | [optional] 
**stage_order** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_stage_dto import AppraisalStageDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalStageDto from a JSON string
appraisal_stage_dto_instance = AppraisalStageDto.from_json(json)
# print the JSON string representation of the object
print(AppraisalStageDto.to_json())

# convert the object into a dict
appraisal_stage_dto_dict = appraisal_stage_dto_instance.to_dict()
# create an instance of AppraisalStageDto from a dict
appraisal_stage_dto_from_dict = AppraisalStageDto.from_dict(appraisal_stage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


