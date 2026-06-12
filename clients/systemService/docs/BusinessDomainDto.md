# BusinessDomainDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**domain** | **str** |  | [optional] 
**txt_record** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.business_domain_dto import BusinessDomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDomainDto from a JSON string
business_domain_dto_instance = BusinessDomainDto.from_json(json)
# print the JSON string representation of the object
print(BusinessDomainDto.to_json())

# convert the object into a dict
business_domain_dto_dict = business_domain_dto_instance.to_dict()
# create an instance of BusinessDomainDto from a dict
business_domain_dto_from_dict = BusinessDomainDto.from_dict(business_domain_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


