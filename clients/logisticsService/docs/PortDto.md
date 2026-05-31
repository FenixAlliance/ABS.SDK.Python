# PortDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**custom_city** | **str** |  | [optional] 
**custom_state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**latitude** | **float** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**un_locode** | **str** |  | [optional] 
**iata_code** | **str** |  | [optional] 
**port_type** | **str** |  | [optional] 
**port_authority** | **str** |  | [optional] 
**has_customs_facility** | **bool** |  | [optional] 
**is_free_tradezone** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**parent_port_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.port_dto import PortDto

# TODO update the JSON string below
json = "{}"
# create an instance of PortDto from a JSON string
port_dto_instance = PortDto.from_json(json)
# print the JSON string representation of the object
print(PortDto.to_json())

# convert the object into a dict
port_dto_dict = port_dto_instance.to_dict()
# create an instance of PortDto from a dict
port_dto_from_dict = PortDto.from_dict(port_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


