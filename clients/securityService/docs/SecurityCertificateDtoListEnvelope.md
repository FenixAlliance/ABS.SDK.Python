# SecurityCertificateDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SecurityCertificateDto]**](SecurityCertificateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_certificate_dto_list_envelope import SecurityCertificateDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityCertificateDtoListEnvelope from a JSON string
security_certificate_dto_list_envelope_instance = SecurityCertificateDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SecurityCertificateDtoListEnvelope.to_json())

# convert the object into a dict
security_certificate_dto_list_envelope_dict = security_certificate_dto_list_envelope_instance.to_dict()
# create an instance of SecurityCertificateDtoListEnvelope from a dict
security_certificate_dto_list_envelope_from_dict = SecurityCertificateDtoListEnvelope.from_dict(security_certificate_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


