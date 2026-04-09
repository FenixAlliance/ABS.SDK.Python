# ItemReviewUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_score** | **float** |  | [optional] 
**review_message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_review_update_dto import ItemReviewUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReviewUpdateDto from a JSON string
item_review_update_dto_instance = ItemReviewUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemReviewUpdateDto.to_json())

# convert the object into a dict
item_review_update_dto_dict = item_review_update_dto_instance.to_dict()
# create an instance of ItemReviewUpdateDto from a dict
item_review_update_dto_from_dict = ItemReviewUpdateDto.from_dict(item_review_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


