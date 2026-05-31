# SeawayBillDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**document_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**shipper_contact_id** | **str** |  | [optional] 
**consignee_contact_id** | **str** |  | [optional] 
**notify_party_contact_id** | **str** |  | [optional] 
**carrier_id** | **str** |  | [optional] 
**vessel_id** | **str** |  | [optional] 
**voyage_id** | **str** |  | [optional] 
**port_of_loading_id** | **str** |  | [optional] 
**port_of_discharge_id** | **str** |  | [optional] 
**place_of_receipt** | **str** |  | [optional] 
**place_of_delivery** | **str** |  | [optional] 
**date_issued** | **datetime** |  | [optional] 
**date_shipped** | **datetime** |  | [optional] 
**date_delivered** | **datetime** |  | [optional] 
**freight_terms** | **str** |  | [optional] 
**freight_amount** | **float** |  | [optional] 
**freight_currency_id** | **str** |  | [optional] 
**total_weight** | **float** |  | [optional] 
**total_packages** | **int** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**lines** | [**List[WaybillLineDto]**](WaybillLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.seaway_bill_dto import SeawayBillDto

# TODO update the JSON string below
json = "{}"
# create an instance of SeawayBillDto from a JSON string
seaway_bill_dto_instance = SeawayBillDto.from_json(json)
# print the JSON string representation of the object
print(SeawayBillDto.to_json())

# convert the object into a dict
seaway_bill_dto_dict = seaway_bill_dto_instance.to_dict()
# create an instance of SeawayBillDto from a dict
seaway_bill_dto_from_dict = SeawayBillDto.from_dict(seaway_bill_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


