# X509Certificate2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **object** |  | [optional] 
**issuer** | **str** |  | [optional] [readonly] 
**subject** | **str** |  | [optional] [readonly] 
**serial_number_bytes** | [**ByteReadOnlyMemory**](ByteReadOnlyMemory.md) |  | [optional] 
**archived** | **bool** |  | [optional] 
**extensions** | [**List[X509Extension]**](X509Extension.md) |  | [optional] [readonly] 
**friendly_name** | **str** |  | [optional] 
**has_private_key** | **bool** |  | [optional] [readonly] 
**private_key** | [**AsymmetricAlgorithm**](AsymmetricAlgorithm.md) |  | [optional] 
**issuer_name** | [**X500DistinguishedName**](X500DistinguishedName.md) |  | [optional] 
**not_after** | **datetime** |  | [optional] [readonly] 
**not_before** | **datetime** |  | [optional] [readonly] 
**public_key** | [**PublicKey**](PublicKey.md) |  | [optional] 
**raw_data** | **bytearray** |  | [optional] [readonly] 
**raw_data_memory** | [**ByteReadOnlyMemory**](ByteReadOnlyMemory.md) |  | [optional] 
**serial_number** | **str** |  | [optional] [readonly] 
**signature_algorithm** | [**Oid**](Oid.md) |  | [optional] 
**subject_name** | [**X500DistinguishedName**](X500DistinguishedName.md) |  | [optional] 
**thumbprint** | **str** |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.x509_certificate2 import X509Certificate2

# TODO update the JSON string below
json = "{}"
# create an instance of X509Certificate2 from a JSON string
x509_certificate2_instance = X509Certificate2.from_json(json)
# print the JSON string representation of the object
print(X509Certificate2.to_json())

# convert the object into a dict
x509_certificate2_dict = x509_certificate2_instance.to_dict()
# create an instance of X509Certificate2 from a dict
x509_certificate2_from_dict = X509Certificate2.from_dict(x509_certificate2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


