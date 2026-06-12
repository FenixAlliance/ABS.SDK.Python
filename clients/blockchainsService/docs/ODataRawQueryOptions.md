# ODataRawQueryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | [optional] [readonly] 
**apply** | **str** |  | [optional] [readonly] 
**compute** | **str** |  | [optional] [readonly] 
**search** | **str** |  | [optional] [readonly] 
**order_by** | **str** |  | [optional] [readonly] 
**top** | **str** |  | [optional] [readonly] 
**skip** | **str** |  | [optional] [readonly] 
**select** | **str** |  | [optional] [readonly] 
**expand** | **str** |  | [optional] [readonly] 
**count** | **str** |  | [optional] [readonly] 
**format** | **str** |  | [optional] [readonly] 
**skip_token** | **str** |  | [optional] [readonly] 
**delta_token** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.o_data_raw_query_options import ODataRawQueryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ODataRawQueryOptions from a JSON string
o_data_raw_query_options_instance = ODataRawQueryOptions.from_json(json)
# print the JSON string representation of the object
print(ODataRawQueryOptions.to_json())

# convert the object into a dict
o_data_raw_query_options_dict = o_data_raw_query_options_instance.to_dict()
# create an instance of ODataRawQueryOptions from a dict
o_data_raw_query_options_from_dict = ODataRawQueryOptions.from_dict(o_data_raw_query_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


