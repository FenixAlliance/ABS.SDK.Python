# ReviewsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_reviews** | **bool** |  | [optional] 
**enable_star_ratings** | **bool** |  | [optional] 
**force_star_ratings** | **bool** |  | [optional] 
**display_verified_owner_badge** | **bool** |  | [optional] 
**force_verified_owner_verification** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.reviews_options import ReviewsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewsOptions from a JSON string
reviews_options_instance = ReviewsOptions.from_json(json)
# print the JSON string representation of the object
print(ReviewsOptions.to_json())

# convert the object into a dict
reviews_options_dict = reviews_options_instance.to_dict()
# create an instance of ReviewsOptions from a dict
reviews_options_from_dict = ReviewsOptions.from_dict(reviews_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


