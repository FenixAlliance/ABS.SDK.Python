# MarketingListDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[MarketingListDto]**](MarketingListDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.marketing_list_dto_list_envelope import MarketingListDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingListDtoListEnvelope from a JSON string
marketing_list_dto_list_envelope_instance = MarketingListDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(MarketingListDtoListEnvelope.to_json())

# convert the object into a dict
marketing_list_dto_list_envelope_dict = marketing_list_dto_list_envelope_instance.to_dict()
# create an instance of MarketingListDtoListEnvelope from a dict
marketing_list_dto_list_envelope_from_dict = MarketingListDtoListEnvelope.from_dict(marketing_list_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


