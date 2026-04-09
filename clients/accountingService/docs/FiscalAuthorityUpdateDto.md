# FiscalAuthorityUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_authority_update_dto import FiscalAuthorityUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalAuthorityUpdateDto from a JSON string
fiscal_authority_update_dto_instance = FiscalAuthorityUpdateDto.from_json(json)
# print the JSON string representation of the object
print(FiscalAuthorityUpdateDto.to_json())

# convert the object into a dict
fiscal_authority_update_dto_dict = fiscal_authority_update_dto_instance.to_dict()
# create an instance of FiscalAuthorityUpdateDto from a dict
fiscal_authority_update_dto_from_dict = FiscalAuthorityUpdateDto.from_dict(fiscal_authority_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


