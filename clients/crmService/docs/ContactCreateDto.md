# ContactCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**tenant_id** | **str** |  | 
**type** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | 
**tax_id** | **str** |  | [optional] 
**primary_contact_id** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] [readonly] 
**about** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**business_phone** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**duns** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**street_line1** | **str** |  | [optional] 
**street_line2** | **str** |  | [optional] 
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
**instagram_username** | **object** |  | [optional] 
**tik_tok_username** | **object** |  | [optional] 
**stack_exchange_url** | **object** |  | [optional] 
**stack_overflow_url** | **object** |  | [optional] 
**parent_contact_id** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.contact_create_dto import ContactCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateDto from a JSON string
contact_create_dto_instance = ContactCreateDto.from_json(json)
# print the JSON string representation of the object
print(ContactCreateDto.to_json())

# convert the object into a dict
contact_create_dto_dict = contact_create_dto_instance.to_dict()
# create an instance of ContactCreateDto from a dict
contact_create_dto_from_dict = ContactCreateDto.from_dict(contact_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


