# ContactDto


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
**duns** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**street_line1** | **str** |  | [optional] 
**street_line2** | **str** |  | [optional] 
**territory_id** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**annual_revenue** | **str** |  | [optional] 
**related_user_id** | **str** |  | [optional] 
**business_phone** | **str** |  | [optional] 
**owner_contact_id** | **str** |  | [optional] 
**related_tenant_id** | **str** |  | [optional] 
**activity_feed_id** | **str** |  | [optional] 
**parent_contact_id** | **str** |  | [optional] 
**identity_provider** | **str** |  | [optional] 
**partner_profile_id** | **str** |  | [optional] 
**primary_contact_id** | **str** |  | [optional] 
**active_directory_id** | **str** |  | [optional] 
**identity_provider_access_token** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.contact_dto import ContactDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDto from a JSON string
contact_dto_instance = ContactDto.from_json(json)
# print the JSON string representation of the object
print(ContactDto.to_json())

# convert the object into a dict
contact_dto_dict = contact_dto_instance.to_dict()
# create an instance of ContactDto from a dict
contact_dto_from_dict = ContactDto.from_dict(contact_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


