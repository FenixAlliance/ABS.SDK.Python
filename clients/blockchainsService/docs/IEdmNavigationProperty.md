# IEdmNavigationProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**property_kind** | **str** |  | [optional] [readonly] 
**type** | [**IEdmTypeReference**](IEdmTypeReference.md) |  | [optional] 
**declaring_type** | [**IEdmStructuredType**](IEdmStructuredType.md) |  | [optional] 
**partner** | [**IEdmNavigationProperty**](IEdmNavigationProperty.md) |  | [optional] 
**on_delete** | **str** |  | [optional] [readonly] 
**contains_target** | **bool** |  | [optional] [readonly] 
**referential_constraint** | [**IEdmReferentialConstraint**](IEdmReferentialConstraint.md) |  | [optional] 

## Example

```python
from openapi_client.models.i_edm_navigation_property import IEdmNavigationProperty

# TODO update the JSON string below
json = "{}"
# create an instance of IEdmNavigationProperty from a JSON string
i_edm_navigation_property_instance = IEdmNavigationProperty.from_json(json)
# print the JSON string representation of the object
print(IEdmNavigationProperty.to_json())

# convert the object into a dict
i_edm_navigation_property_dict = i_edm_navigation_property_instance.to_dict()
# create an instance of IEdmNavigationProperty from a dict
i_edm_navigation_property_from_dict = IEdmNavigationProperty.from_dict(i_edm_navigation_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


