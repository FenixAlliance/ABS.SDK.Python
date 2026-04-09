# SocialMediaOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facebook_page_url** | **str** |  | [optional] 
**twitter_username** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**my_space_url** | **str** |  | [optional] 
**pinterest_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**github_url** | **str** |  | [optional] 
**reddit_url** | **str** |  | [optional] 
**whats_app_number** | **str** |  | [optional] 
**wikipedia_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_media_options import SocialMediaOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SocialMediaOptions from a JSON string
social_media_options_instance = SocialMediaOptions.from_json(json)
# print the JSON string representation of the object
print(SocialMediaOptions.to_json())

# convert the object into a dict
social_media_options_dict = social_media_options_instance.to_dict()
# create an instance of SocialMediaOptions from a dict
social_media_options_from_dict = SocialMediaOptions.from_dict(social_media_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


