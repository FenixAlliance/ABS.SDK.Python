# IPLookupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**ua** | **str** |  | [optional] 
**city** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ip_lookup_dto import IPLookupDto

# TODO update the JSON string below
json = "{}"
# create an instance of IPLookupDto from a JSON string
ip_lookup_dto_instance = IPLookupDto.from_json(json)
# print the JSON string representation of the object
print(IPLookupDto.to_json())

# convert the object into a dict
ip_lookup_dto_dict = ip_lookup_dto_instance.to_dict()
# create an instance of IPLookupDto from a dict
ip_lookup_dto_from_dict = IPLookupDto.from_dict(ip_lookup_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


