# BusinessDomainCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**domain** | **str** |  | 

## Example

```python
from openapi_client.models.business_domain_create_dto import BusinessDomainCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDomainCreateDto from a JSON string
business_domain_create_dto_instance = BusinessDomainCreateDto.from_json(json)
# print the JSON string representation of the object
print(BusinessDomainCreateDto.to_json())

# convert the object into a dict
business_domain_create_dto_dict = business_domain_create_dto_instance.to_dict()
# create an instance of BusinessDomainCreateDto from a dict
business_domain_create_dto_from_dict = BusinessDomainCreateDto.from_dict(business_domain_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


