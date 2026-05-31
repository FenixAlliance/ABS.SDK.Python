# ODataQueryContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_query_configurations** | [**DefaultQueryConfigurations**](DefaultQueryConfigurations.md) |  | [optional] 
**model** | [**IEdmModel**](IEdmModel.md) |  | [optional] 
**element_type** | [**IEdmType**](IEdmType.md) |  | [optional] 
**navigation_source** | [**IEdmNavigationSource**](IEdmNavigationSource.md) |  | [optional] 
**element_clr_type** | [**Type**](Type.md) |  | [optional] 
**path** | [**List[ODataPathSegment]**](ODataPathSegment.md) |  | [optional] 
**request_container** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.o_data_query_context import ODataQueryContext

# TODO update the JSON string below
json = "{}"
# create an instance of ODataQueryContext from a JSON string
o_data_query_context_instance = ODataQueryContext.from_json(json)
# print the JSON string representation of the object
print(ODataQueryContext.to_json())

# convert the object into a dict
o_data_query_context_dict = o_data_query_context_instance.to_dict()
# create an instance of ODataQueryContext from a dict
o_data_query_context_from_dict = ODataQueryContext.from_dict(o_data_query_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


