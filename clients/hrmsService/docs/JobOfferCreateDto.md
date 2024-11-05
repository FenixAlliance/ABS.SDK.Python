# JobOfferCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.job_offer_create_dto import JobOfferCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobOfferCreateDto from a JSON string
job_offer_create_dto_instance = JobOfferCreateDto.from_json(json)
# print the JSON string representation of the object
print(JobOfferCreateDto.to_json())

# convert the object into a dict
job_offer_create_dto_dict = job_offer_create_dto_instance.to_dict()
# create an instance of JobOfferCreateDto from a dict
job_offer_create_dto_from_dict = JobOfferCreateDto.from_dict(job_offer_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


