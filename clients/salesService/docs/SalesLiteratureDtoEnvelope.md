# SalesLiteratureDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SalesLiteratureDto**](SalesLiteratureDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.sales_literature_dto_envelope import SalesLiteratureDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SalesLiteratureDtoEnvelope from a JSON string
sales_literature_dto_envelope_instance = SalesLiteratureDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SalesLiteratureDtoEnvelope.to_json())

# convert the object into a dict
sales_literature_dto_envelope_dict = sales_literature_dto_envelope_instance.to_dict()
# create an instance of SalesLiteratureDtoEnvelope from a dict
sales_literature_dto_envelope_from_dict = SalesLiteratureDtoEnvelope.from_dict(sales_literature_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


