# SalesLiteratureDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SalesLiteratureDto]**](SalesLiteratureDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.sales_literature_dto_list_envelope import SalesLiteratureDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SalesLiteratureDtoListEnvelope from a JSON string
sales_literature_dto_list_envelope_instance = SalesLiteratureDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SalesLiteratureDtoListEnvelope.to_json())

# convert the object into a dict
sales_literature_dto_list_envelope_dict = sales_literature_dto_list_envelope_instance.to_dict()
# create an instance of SalesLiteratureDtoListEnvelope from a dict
sales_literature_dto_list_envelope_from_dict = SalesLiteratureDtoListEnvelope.from_dict(sales_literature_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


