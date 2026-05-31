# X509Extension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oid** | [**Oid**](Oid.md) |  | [optional] 
**raw_data** | **bytearray** |  | [optional] 
**critical** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.x509_extension import X509Extension

# TODO update the JSON string below
json = "{}"
# create an instance of X509Extension from a JSON string
x509_extension_instance = X509Extension.from_json(json)
# print the JSON string representation of the object
print(X509Extension.to_json())

# convert the object into a dict
x509_extension_dict = x509_extension_instance.to_dict()
# create an instance of X509Extension from a dict
x509_extension_from_dict = X509Extension.from_dict(x509_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


