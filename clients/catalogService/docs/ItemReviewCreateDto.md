# ItemReviewCreateDto


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
from openapi_client.models.item_review_create_dto import ItemReviewCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReviewCreateDto from a JSON string
item_review_create_dto_instance = ItemReviewCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemReviewCreateDto.to_json())

# convert the object into a dict
item_review_create_dto_dict = item_review_create_dto_instance.to_dict()
# create an instance of ItemReviewCreateDto from a dict
item_review_create_dto_from_dict = ItemReviewCreateDto.from_dict(item_review_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


