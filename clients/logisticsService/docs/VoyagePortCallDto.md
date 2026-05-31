# VoyagePortCallDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**port_call_status** | **str** |  | [optional] 
**eta** | **datetime** |  | [optional] 
**ata** | **datetime** |  | [optional] 
**etd** | **datetime** |  | [optional] 
**atd** | **datetime** |  | [optional] 
**berth_number** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**voyage_id** | **str** |  | [optional] 
**port_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.voyage_port_call_dto import VoyagePortCallDto

# TODO update the JSON string below
json = "{}"
# create an instance of VoyagePortCallDto from a JSON string
voyage_port_call_dto_instance = VoyagePortCallDto.from_json(json)
# print the JSON string representation of the object
print(VoyagePortCallDto.to_json())

# convert the object into a dict
voyage_port_call_dto_dict = voyage_port_call_dto_instance.to_dict()
# create an instance of VoyagePortCallDto from a dict
voyage_port_call_dto_from_dict = VoyagePortCallDto.from_dict(voyage_port_call_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


