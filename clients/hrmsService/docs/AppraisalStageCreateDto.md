# AppraisalStageCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**appraisal_workflow_id** | **str** |  | 
**stage_order** | **int** |  | 

## Example

```python
from openapi_client.models.appraisal_stage_create_dto import AppraisalStageCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalStageCreateDto from a JSON string
appraisal_stage_create_dto_instance = AppraisalStageCreateDto.from_json(json)
# print the JSON string representation of the object
print(AppraisalStageCreateDto.to_json())

# convert the object into a dict
appraisal_stage_create_dto_dict = appraisal_stage_create_dto_instance.to_dict()
# create an instance of AppraisalStageCreateDto from a dict
appraisal_stage_create_dto_from_dict = AppraisalStageCreateDto.from_dict(appraisal_stage_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


