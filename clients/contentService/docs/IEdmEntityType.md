# IEdmEntityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_kind** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**is_abstract** | **bool** |  | [optional] [readonly] 
**is_open** | **bool** |  | [optional] [readonly] 
**base_type** | [**IEdmStructuredType**](IEdmStructuredType.md) |  | [optional] 
**declared_properties** | [**List[IEdmProperty]**](IEdmProperty.md) |  | [optional] [readonly] 
**schema_element_kind** | **str** |  | [optional] [readonly] 
**namespace** | **str** |  | [optional] [readonly] 
**declared_key** | [**List[IEdmStructuralProperty]**](IEdmStructuralProperty.md) |  | [optional] [readonly] 
**has_stream** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.i_edm_entity_type import IEdmEntityType

# TODO update the JSON string below
json = "{}"
# create an instance of IEdmEntityType from a JSON string
i_edm_entity_type_instance = IEdmEntityType.from_json(json)
# print the JSON string representation of the object
print(IEdmEntityType.to_json())

# convert the object into a dict
i_edm_entity_type_dict = i_edm_entity_type_instance.to_dict()
# create an instance of IEdmEntityType from a dict
i_edm_entity_type_from_dict = IEdmEntityType.from_dict(i_edm_entity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


