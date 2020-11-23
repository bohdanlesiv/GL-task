import pandas as pd
import json
from jsonschema import validate


transactionSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "id_str": {
          "type": "string"
        },
        "order_type": {
          "type": "integer"
        },
        "datetime": {
          "type": "string"
        },
        "microtimestamp": {
          "type": "string"
        },
        "amount": {
          "type": "number"
        },
        "amount_str": {
          "type": "string"
        },
        "price": {
          "type": "number"
        },
        "price_str": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "id_str",
        "order_type",
        "datetime",
        "microtimestamp",
        "amount",
        "amount_str",
        "price",
        "price_str"
      ]
    },
    "channel": {
      "type": "string"
    },
    "event": {
      "type": "string"
    }
  },
  "required": [
    "data",
    "channel",
    "event"
  ]
}

class Processor(object):
  def __init__(self):
    self._storage_top_10 = pd.DataFrame(columns=['id', 'datetime', 'price'])

  @staticmethod
  def _prepare_msg(msg_json):
    idtr = msg_json.get('data').get('id')
    datetime = msg_json.get('data').get('datetime')
    price = msg_json.get('data').get('price')
    return {'id': idtr, 'datetime': datetime, 'price': price }

  @staticmethod
  def _is_msg_valid(msg):
    try:
      msg_json = json.loads(msg)
      validate(instance=msg_json, schema=transactionSchema)
    except:
      return False
    return True

  def add_msg(self, msg):
    if Processor._is_msg_valid(msg=msg):
      msg_json = json.loads(msg)
      prep_msg = Processor._prepare_msg(msg_json)
      self._storage_top_10 = self._storage_top_10.append(prep_msg, ignore_index=True)
      self._storage_top_10.sort_values(by=['price'], inplace=True, ascending=False)
      self._storage_top_10 = self._storage_top_10.head(10)
    else:
      print('Message is not valid')

  def print_msg(self):
    self._storage_top_10.to_clipboard(sep=',', index=False)
    print(self._storage_top_10)



# text ='{"data":{ "id":1297851689496576,"id_str":"1297851689496576","order_type":1,"datetime":"1605693298","microtimestamp":"1605693298239000","amount":0.014,"amount_str":"0.01400000","price":18058.68, "price_str":"18058.68"}, "channel":"live_orders_btcusd","event":"order_deleted"}'
# text1 ='{"data":{ "id":1297851689496579,"id_str":"1297851689496576","order_type":1,"datetime":"1605693298","microtimestamp":"1605693298239000","amount":0.014,"amount_str":"0.01400000","price":44.68, "price_str":"18058.68"}, "channel":"live_orders_btcusd","event":"order_deleted"}'
# text2='{"data":{ "id":456456,"id_str":"1297851689496576","order_type":1,"datetime":"1605693298","microtimestamp":"1605693298239000","amount":0.014,"amount_str":"0.01400000","price":19999458.68, "price_str":"18058.68"}, "channel":"live_orders_btcusd","event":"order_deleted"}'
# text3 ='{"data":{ "id":45646,"id_str":"1297851689496576","order_type":1,"datetime":"1605693298","microtimestamp":"1605693298239000","amount":0.014,"amount_str":"0.01400000","price":148.68, "price_str":"18058.68"}, "channel":"live_orders_btcusd","event":"order_deleted"}'
#
# proc = Processor()
# proc.add_msg(text1)
# proc.add_msg(text3)
# proc.add_msg(text2)
# proc.add_msg(text)
# proc.add_msg(text)
# proc.print_msg()
# msg_json = json.loads(text)
#
# storage_top_10 = pd.DataFrame(columns=['id', 'datetime', 'price'])
#
# id = msg_json.get('data').get('id')
# datetime = msg_json.get('data').get('datetime')
# price = msg_json.get('data').get('price')
#
# msg_dict = {'id': id,'datetime': datetime,'price': price }
# msg_dict1 = {'id': 34534,'datetime': 45,'price': 444 }
# msg_dict3 = {'id': 435345,'datetime': 45,'price': 55 }
# msg_dict4 = {'id': 345,'datetime': 45,'price': 9999999 }
# msg_dict5 = {'id': 45,'datetime': 4545,'price': 777 }
# storage_top_10 = storage_top_10.append(msg_dict, ignore_index=True)
# storage_top_10 = storage_top_10.append(msg_dict1, ignore_index=True)
# storage_top_10 = storage_top_10.append(msg_dict4, ignore_index=True)
# storage_top_10 = storage_top_10.append(msg_dict3, ignore_index=True)
# storage_top_10 = storage_top_10.append(msg_dict5, ignore_index=True)
#
# storage_top_10.sort_values(by=['price'], inplace=True,ascending=False)
# storage_top_10 = storage_top_10.head(3)
# print(storage_top_10)



