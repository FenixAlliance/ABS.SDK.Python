# ItemReviewDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**item_id** | **str** |  | [optional] 
**review_score** | **float** |  | [optional] 
**review_message** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_review_dto import ItemReviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReviewDto from a JSON string
item_review_dto_instance = ItemReviewDto.from_json(json)
# print the JSON string representation of the object
print(ItemReviewDto.to_json())

# convert the object into a dict
item_review_dto_dict = item_review_dto_instance.to_dict()
# create an instance of ItemReviewDto from a dict
item_review_dto_from_dict = ItemReviewDto.from_dict(item_review_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


