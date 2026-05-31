# BillOfLadingLineDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**package_type** | **str** |  | [optional] 
**gross_weight_kg** | **float** |  | [optional] 
**volume_m3** | **float** |  | [optional] 
**marks_and_numbers** | **str** |  | [optional] 
**hs_code** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**bill_of_lading_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bill_of_lading_line_dto import BillOfLadingLineDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillOfLadingLineDto from a JSON string
bill_of_lading_line_dto_instance = BillOfLadingLineDto.from_json(json)
# print the JSON string representation of the object
print(BillOfLadingLineDto.to_json())

# convert the object into a dict
bill_of_lading_line_dto_dict = bill_of_lading_line_dto_instance.to_dict()
# create an instance of BillOfLadingLineDto from a dict
bill_of_lading_line_dto_from_dict = BillOfLadingLineDto.from_dict(bill_of_lading_line_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


