# AsnEncodedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oid** | [**Oid**](Oid.md) |  | [optional] 
**raw_data** | **bytearray** |  | [optional] 

## Example

```python
from openapi_client.models.asn_encoded_data import AsnEncodedData

# TODO update the JSON string below
json = "{}"
# create an instance of AsnEncodedData from a JSON string
asn_encoded_data_instance = AsnEncodedData.from_json(json)
# print the JSON string representation of the object
print(AsnEncodedData.to_json())

# convert the object into a dict
asn_encoded_data_dict = asn_encoded_data_instance.to_dict()
# create an instance of AsnEncodedData from a dict
asn_encoded_data_from_dict = AsnEncodedData.from_dict(asn_encoded_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


