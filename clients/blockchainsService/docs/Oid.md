# Oid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.oid import Oid

# TODO update the JSON string below
json = "{}"
# create an instance of Oid from a JSON string
oid_instance = Oid.from_json(json)
# print the JSON string representation of the object
print(Oid.to_json())

# convert the object into a dict
oid_dict = oid_instance.to_dict()
# create an instance of Oid from a dict
oid_from_dict = Oid.from_dict(oid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


