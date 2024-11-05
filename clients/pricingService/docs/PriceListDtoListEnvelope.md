# PriceListDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PriceListDto]**](PriceListDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_list_dto_list_envelope import PriceListDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListDtoListEnvelope from a JSON string
price_list_dto_list_envelope_instance = PriceListDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PriceListDtoListEnvelope.to_json())

# convert the object into a dict
price_list_dto_list_envelope_dict = price_list_dto_list_envelope_instance.to_dict()
# create an instance of PriceListDtoListEnvelope from a dict
price_list_dto_list_envelope_from_dict = PriceListDtoListEnvelope.from_dict(price_list_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


