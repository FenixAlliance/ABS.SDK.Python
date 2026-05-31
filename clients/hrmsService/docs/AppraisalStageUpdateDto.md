# AppraisalStageUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**appraisal_workflow_id** | **str** |  | [optional] 
**stage_order** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_stage_update_dto import AppraisalStageUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalStageUpdateDto from a JSON string
appraisal_stage_update_dto_instance = AppraisalStageUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AppraisalStageUpdateDto.to_json())

# convert the object into a dict
appraisal_stage_update_dto_dict = appraisal_stage_update_dto_instance.to_dict()
# create an instance of AppraisalStageUpdateDto from a dict
appraisal_stage_update_dto_from_dict = AppraisalStageUpdateDto.from_dict(appraisal_stage_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


