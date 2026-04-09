# ShareIssuanceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**unit_price** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.share_issuance_dto import ShareIssuanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShareIssuanceDto from a JSON string
share_issuance_dto_instance = ShareIssuanceDto.from_json(json)
# print the JSON string representation of the object
print(ShareIssuanceDto.to_json())

# convert the object into a dict
share_issuance_dto_dict = share_issuance_dto_instance.to_dict()
# create an instance of ShareIssuanceDto from a dict
share_issuance_dto_from_dict = ShareIssuanceDto.from_dict(share_issuance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


