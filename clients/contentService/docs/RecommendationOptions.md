# RecommendationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_weight** | **float** |  | [optional] 
**add_to_cart_weight** | **float** |  | [optional] 
**removed_from_cart_weight** | **float** |  | [optional] 
**added_to_wishlist_weight** | **float** |  | [optional] 
**already_purchased_weight** | **float** |  | [optional] 
**removed_to_wishlist_weight** | **float** |  | [optional] 
**added_to_compare_table_weight** | **float** |  | [optional] 
**removed_to_compare_table_weight** | **float** |  | [optional] 
**enable_cross_selling** | **bool** |  | [optional] 
**enable_bundled_products** | **bool** |  | [optional] 
**enable_recently_viewed_products** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.recommendation_options import RecommendationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationOptions from a JSON string
recommendation_options_instance = RecommendationOptions.from_json(json)
# print the JSON string representation of the object
print(RecommendationOptions.to_json())

# convert the object into a dict
recommendation_options_dict = recommendation_options_instance.to_dict()
# create an instance of RecommendationOptions from a dict
recommendation_options_from_dict = RecommendationOptions.from_dict(recommendation_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


