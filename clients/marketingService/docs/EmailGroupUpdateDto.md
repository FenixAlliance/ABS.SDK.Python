# EmailGroupUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_group_update_dto import EmailGroupUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailGroupUpdateDto from a JSON string
email_group_update_dto_instance = EmailGroupUpdateDto.from_json(json)
# print the JSON string representation of the object
print(EmailGroupUpdateDto.to_json())

# convert the object into a dict
email_group_update_dto_dict = email_group_update_dto_instance.to_dict()
# create an instance of EmailGroupUpdateDto from a dict
email_group_update_dto_from_dict = EmailGroupUpdateDto.from_dict(email_group_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


