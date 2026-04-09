# BlogOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts_per_page** | **int** |  | [optional] 
**enable_blog_post_comments** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.blog_options import BlogOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BlogOptions from a JSON string
blog_options_instance = BlogOptions.from_json(json)
# print the JSON string representation of the object
print(BlogOptions.to_json())

# convert the object into a dict
blog_options_dict = blog_options_instance.to_dict()
# create an instance of BlogOptions from a dict
blog_options_from_dict = BlogOptions.from_dict(blog_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


