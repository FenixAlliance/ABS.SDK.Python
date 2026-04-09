# BlogAuthorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**cover_url** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**git_hub_url** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**social_feed_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**public_identifier** | **str** |  | [optional] 
**phone_number_confirmed** | **bool** |  | [optional] 
**availability** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blog_author_dto import BlogAuthorDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlogAuthorDto from a JSON string
blog_author_dto_instance = BlogAuthorDto.from_json(json)
# print the JSON string representation of the object
print(BlogAuthorDto.to_json())

# convert the object into a dict
blog_author_dto_dict = blog_author_dto_instance.to_dict()
# create an instance of BlogAuthorDto from a dict
blog_author_dto_from_dict = BlogAuthorDto.from_dict(blog_author_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


