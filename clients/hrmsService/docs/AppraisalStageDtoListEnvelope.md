# AppraisalStageDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AppraisalStageDto]**](AppraisalStageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_stage_dto_list_envelope import AppraisalStageDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalStageDtoListEnvelope from a JSON string
appraisal_stage_dto_list_envelope_instance = AppraisalStageDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AppraisalStageDtoListEnvelope.to_json())

# convert the object into a dict
appraisal_stage_dto_list_envelope_dict = appraisal_stage_dto_list_envelope_instance.to_dict()
# create an instance of AppraisalStageDtoListEnvelope from a dict
appraisal_stage_dto_list_envelope_from_dict = AppraisalStageDtoListEnvelope.from_dict(appraisal_stage_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


