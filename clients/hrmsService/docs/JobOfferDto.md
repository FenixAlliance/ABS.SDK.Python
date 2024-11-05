# JobOfferDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.job_offer_dto import JobOfferDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobOfferDto from a JSON string
job_offer_dto_instance = JobOfferDto.from_json(json)
# print the JSON string representation of the object
print(JobOfferDto.to_json())

# convert the object into a dict
job_offer_dto_dict = job_offer_dto_instance.to_dict()
# create an instance of JobOfferDto from a dict
job_offer_dto_from_dict = JobOfferDto.from_dict(job_offer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


