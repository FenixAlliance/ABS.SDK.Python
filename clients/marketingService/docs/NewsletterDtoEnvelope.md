# NewsletterDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**NewsletterDto**](NewsletterDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.newsletter_dto_envelope import NewsletterDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of NewsletterDtoEnvelope from a JSON string
newsletter_dto_envelope_instance = NewsletterDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(NewsletterDtoEnvelope.to_json())

# convert the object into a dict
newsletter_dto_envelope_dict = newsletter_dto_envelope_instance.to_dict()
# create an instance of NewsletterDtoEnvelope from a dict
newsletter_dto_envelope_from_dict = NewsletterDtoEnvelope.from_dict(newsletter_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


