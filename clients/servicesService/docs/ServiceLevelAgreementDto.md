# ServiceLevelAgreementDto


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
from openapi_client.models.service_level_agreement_dto import ServiceLevelAgreementDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelAgreementDto from a JSON string
service_level_agreement_dto_instance = ServiceLevelAgreementDto.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelAgreementDto.to_json())

# convert the object into a dict
service_level_agreement_dto_dict = service_level_agreement_dto_instance.to_dict()
# create an instance of ServiceLevelAgreementDto from a dict
service_level_agreement_dto_from_dict = ServiceLevelAgreementDto.from_dict(service_level_agreement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


