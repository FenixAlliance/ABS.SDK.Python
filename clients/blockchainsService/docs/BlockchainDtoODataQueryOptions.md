# BlockchainDtoODataQueryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**HttpRequest**](HttpRequest.md) |  | [optional] 
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**raw_values** | [**ODataRawQueryOptions**](ODataRawQueryOptions.md) |  | [optional] 
**select_expand** | [**SelectExpandQueryOption**](SelectExpandQueryOption.md) |  | [optional] 
**apply** | [**ApplyQueryOption**](ApplyQueryOption.md) |  | [optional] 
**compute** | [**ComputeQueryOption**](ComputeQueryOption.md) |  | [optional] 
**filter** | [**FilterQueryOption**](FilterQueryOption.md) |  | [optional] 
**search** | [**SearchQueryOption**](SearchQueryOption.md) |  | [optional] 
**order_by** | [**OrderByQueryOption**](OrderByQueryOption.md) |  | [optional] 
**skip** | [**SkipQueryOption**](SkipQueryOption.md) |  | [optional] 
**skip_token** | [**SkipTokenQueryOption**](SkipTokenQueryOption.md) |  | [optional] 
**top** | [**TopQueryOption**](TopQueryOption.md) |  | [optional] 
**count** | [**CountQueryOption**](CountQueryOption.md) |  | [optional] 
**validator** | **object** |  | [optional] 
**if_match** | [**BlockchainDtoETag**](BlockchainDtoETag.md) |  | [optional] 
**if_none_match** | [**BlockchainDtoETag**](BlockchainDtoETag.md) |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_dto_o_data_query_options import BlockchainDtoODataQueryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainDtoODataQueryOptions from a JSON string
blockchain_dto_o_data_query_options_instance = BlockchainDtoODataQueryOptions.from_json(json)
# print the JSON string representation of the object
print(BlockchainDtoODataQueryOptions.to_json())

# convert the object into a dict
blockchain_dto_o_data_query_options_dict = blockchain_dto_o_data_query_options_instance.to_dict()
# create an instance of BlockchainDtoODataQueryOptions from a dict
blockchain_dto_o_data_query_options_from_dict = BlockchainDtoODataQueryOptions.from_dict(blockchain_dto_o_data_query_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


