# ETag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_well_formed** | **bool** |  | [optional] 
**entity_type** | [**Type**](Type.md) |  | [optional] 
**is_any** | **bool** |  | [optional] 
**is_if_none_match** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.e_tag import ETag

# TODO update the JSON string below
json = "{}"
# create an instance of ETag from a JSON string
e_tag_instance = ETag.from_json(json)
# print the JSON string representation of the object
print(ETag.to_json())

# convert the object into a dict
e_tag_dict = e_tag_instance.to_dict()
# create an instance of ETag from a dict
e_tag_from_dict = ETag.from_dict(e_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


