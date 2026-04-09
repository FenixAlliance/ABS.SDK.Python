# SecurityCertificateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**expire_period** | **str** |  | [optional] 
**expired** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**business_id** | **str** |  | [optional] 
**csr** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.security_certificate_dto import SecurityCertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityCertificateDto from a JSON string
security_certificate_dto_instance = SecurityCertificateDto.from_json(json)
# print the JSON string representation of the object
print(SecurityCertificateDto.to_json())

# convert the object into a dict
security_certificate_dto_dict = security_certificate_dto_instance.to_dict()
# create an instance of SecurityCertificateDto from a dict
security_certificate_dto_from_dict = SecurityCertificateDto.from_dict(security_certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


