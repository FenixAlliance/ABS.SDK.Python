# SimpleContactDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**qualified_name** | **str** |  | [optional] [readonly] 
**tenant_id** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**public_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**cover_url** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**git_hub_url** | **str** |  | [optional] 
**twitch_url** | **str** |  | [optional] 
**reddit_url** | **str** |  | [optional] 
**tik_tok_url** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**github_username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.simple_contact_dto import SimpleContactDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleContactDto from a JSON string
simple_contact_dto_instance = SimpleContactDto.from_json(json)
# print the JSON string representation of the object
print(SimpleContactDto.to_json())

# convert the object into a dict
simple_contact_dto_dict = simple_contact_dto_instance.to_dict()
# create an instance of SimpleContactDto from a dict
simple_contact_dto_from_dict = SimpleContactDto.from_dict(simple_contact_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


