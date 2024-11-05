# ContactUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**birthday** | **datetime** |  | [optional] 
**duns** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**primary_contact_id** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] [readonly] 
**about** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**business_phone** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**parent_contact_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**street_line1** | **str** |  | [optional] 
**street_line2** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**cover_url** | **str** |  | [optional] 
**github_username** | **str** |  | [optional] 
**instagram_username** | **str** |  | [optional] 
**twitch_url** | **str** |  | [optional] 
**reddit_url** | **str** |  | [optional] 
**git_hub_url** | **str** |  | [optional] 
**github_url** | **str** |  | [optional] 
**tik_tok_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**tik_tok_username** | **str** |  | [optional] 
**stack_exchange_url** | **str** |  | [optional] 
**stack_overflow_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contact_update_dto import ContactUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateDto from a JSON string
contact_update_dto_instance = ContactUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateDto.to_json())

# convert the object into a dict
contact_update_dto_dict = contact_update_dto_instance.to_dict()
# create an instance of ContactUpdateDto from a dict
contact_update_dto_from_dict = ContactUpdateDto.from_dict(contact_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


