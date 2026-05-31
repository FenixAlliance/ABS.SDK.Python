# StructLayoutAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **object** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.struct_layout_attribute import StructLayoutAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of StructLayoutAttribute from a JSON string
struct_layout_attribute_instance = StructLayoutAttribute.from_json(json)
# print the JSON string representation of the object
print(StructLayoutAttribute.to_json())

# convert the object into a dict
struct_layout_attribute_dict = struct_layout_attribute_instance.to_dict()
# create an instance of StructLayoutAttribute from a dict
struct_layout_attribute_from_dict = StructLayoutAttribute.from_dict(struct_layout_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


