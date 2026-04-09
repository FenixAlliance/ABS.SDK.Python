# ContactOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email1** | **str** |  | [optional] 
**email2** | **str** |  | [optional] 
**phone_number1** | **str** |  | [optional] 
**phone_number2** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contact_options import ContactOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ContactOptions from a JSON string
contact_options_instance = ContactOptions.from_json(json)
# print the JSON string representation of the object
print(ContactOptions.to_json())

# convert the object into a dict
contact_options_dict = contact_options_instance.to_dict()
# create an instance of ContactOptions from a dict
contact_options_from_dict = ContactOptions.from_dict(contact_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


