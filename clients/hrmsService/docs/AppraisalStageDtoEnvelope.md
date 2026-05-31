# AppraisalStageDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AppraisalStageDto**](AppraisalStageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.appraisal_stage_dto_envelope import AppraisalStageDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AppraisalStageDtoEnvelope from a JSON string
appraisal_stage_dto_envelope_instance = AppraisalStageDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AppraisalStageDtoEnvelope.to_json())

# convert the object into a dict
appraisal_stage_dto_envelope_dict = appraisal_stage_dto_envelope_instance.to_dict()
# create an instance of AppraisalStageDtoEnvelope from a dict
appraisal_stage_dto_envelope_from_dict = AppraisalStageDtoEnvelope.from_dict(appraisal_stage_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


