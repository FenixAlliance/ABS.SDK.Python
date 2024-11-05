# LicenseKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**seats** | **int** |  | [optional] 
**license_type** | **int** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**features** | [**List[LicenseFeature]**](LicenseFeature.md) |  | [optional] 
**additional_attributes** | [**List[AdditionalAttribute]**](AdditionalAttribute.md) |  | [optional] 

## Example

```python
from openapi_client.models.license_key_request import LicenseKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseKeyRequest from a JSON string
license_key_request_instance = LicenseKeyRequest.from_json(json)
# print the JSON string representation of the object
print(LicenseKeyRequest.to_json())

# convert the object into a dict
license_key_request_dict = license_key_request_instance.to_dict()
# create an instance of LicenseKeyRequest from a dict
license_key_request_from_dict = LicenseKeyRequest.from_dict(license_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


