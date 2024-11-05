# NewsletterUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.newsletter_update_dto import NewsletterUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewsletterUpdateDto from a JSON string
newsletter_update_dto_instance = NewsletterUpdateDto.from_json(json)
# print the JSON string representation of the object
print(NewsletterUpdateDto.to_json())

# convert the object into a dict
newsletter_update_dto_dict = newsletter_update_dto_instance.to_dict()
# create an instance of NewsletterUpdateDto from a dict
newsletter_update_dto_from_dict = NewsletterUpdateDto.from_dict(newsletter_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


