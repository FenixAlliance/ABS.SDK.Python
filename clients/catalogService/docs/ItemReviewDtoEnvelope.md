# ItemReviewDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemReviewDto**](ItemReviewDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_review_dto_envelope import ItemReviewDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReviewDtoEnvelope from a JSON string
item_review_dto_envelope_instance = ItemReviewDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemReviewDtoEnvelope.to_json())

# convert the object into a dict
item_review_dto_envelope_dict = item_review_dto_envelope_instance.to_dict()
# create an instance of ItemReviewDtoEnvelope from a dict
item_review_dto_envelope_from_dict = ItemReviewDtoEnvelope.from_dict(item_review_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


