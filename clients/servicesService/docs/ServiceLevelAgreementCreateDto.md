# ServiceLevelAgreementCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_level_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_level_agreement_create_dto import ServiceLevelAgreementCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelAgreementCreateDto from a JSON string
service_level_agreement_create_dto_instance = ServiceLevelAgreementCreateDto.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelAgreementCreateDto.to_json())

# convert the object into a dict
service_level_agreement_create_dto_dict = service_level_agreement_create_dto_instance.to_dict()
# create an instance of ServiceLevelAgreementCreateDto from a dict
service_level_agreement_create_dto_from_dict = ServiceLevelAgreementCreateDto.from_dict(service_level_agreement_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


