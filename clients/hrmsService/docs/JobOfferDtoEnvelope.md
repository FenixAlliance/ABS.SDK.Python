# JobOfferDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**JobOfferDto**](JobOfferDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.job_offer_dto_envelope import JobOfferDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of JobOfferDtoEnvelope from a JSON string
job_offer_dto_envelope_instance = JobOfferDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(JobOfferDtoEnvelope.to_json())

# convert the object into a dict
job_offer_dto_envelope_dict = job_offer_dto_envelope_instance.to_dict()
# create an instance of JobOfferDtoEnvelope from a dict
job_offer_dto_envelope_from_dict = JobOfferDtoEnvelope.from_dict(job_offer_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


