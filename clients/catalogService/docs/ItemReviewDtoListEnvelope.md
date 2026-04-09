# ItemReviewDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ItemReviewDto]**](ItemReviewDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_review_dto_list_envelope import ItemReviewDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReviewDtoListEnvelope from a JSON string
item_review_dto_list_envelope_instance = ItemReviewDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemReviewDtoListEnvelope.to_json())

# convert the object into a dict
item_review_dto_list_envelope_dict = item_review_dto_list_envelope_instance.to_dict()
# create an instance of ItemReviewDtoListEnvelope from a dict
item_review_dto_list_envelope_from_dict = ItemReviewDtoListEnvelope.from_dict(item_review_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


