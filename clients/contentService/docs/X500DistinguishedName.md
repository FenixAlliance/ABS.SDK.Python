# X500DistinguishedName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oid** | [**Oid**](Oid.md) |  | [optional] 
**raw_data** | **bytearray** |  | [optional] 
**name** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.x500_distinguished_name import X500DistinguishedName

# TODO update the JSON string below
json = "{}"
# create an instance of X500DistinguishedName from a JSON string
x500_distinguished_name_instance = X500DistinguishedName.from_json(json)
# print the JSON string representation of the object
print(X500DistinguishedName.to_json())

# convert the object into a dict
x500_distinguished_name_dict = x500_distinguished_name_instance.to_dict()
# create an instance of X500DistinguishedName from a dict
x500_distinguished_name_from_dict = X500DistinguishedName.from_dict(x500_distinguished_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


