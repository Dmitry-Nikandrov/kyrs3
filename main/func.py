import os, json

def load_function():
    '''загружает текстовые данные из внешнего файла'''

    path = "operations.json"
    file_path = os.path.join(path)
    with open(file_path, 'r') as file:
        return json.load(file)


def sorted_list (operations):
  '''сортирует список по дате совершаения операции'''

  operation = sorted(operations,  key=lambda x: x['date'], reverse=True)
  return operation


def data_transform (operationss):
  '''преобразует дату в требуемый формат'''

  operation_list = []
  for operation in operationss:
    unit = {"date":operation["date"][8:10]+"."+operation["date"][5:7]+"."+operation["date"][0:4],
            'description':operation['description'],
            'from':operation['from'],
            'to':operation['to'],
            'amount':operation['amount'],
            'name':operation['name']
    }
    operation_list.append(unit)
  return operation_list[0:5]

def filter_and_mask_account(operations):
  '''Отбирает из списка операции со статусом "EXECUTED" и скрывает
  данные о счет отправителя и получателя платежа'''

  operation_list =[]
  for operation in operations:
    try:
      if operation["state"] == "EXECUTED":
        unit = {"date": operation["date"][0:10],
                "description":operation["description"],
                "from":operation["from"][:-16]+" "+operation["from"][-16:-14]+" ** **** "+operation["from"][-4:],
                "to":operation["to"][:-21]+" **"+operation["to"][-4:],
                "amount":operation["operationAmount"]["amount"],
                "name":operation["operationAmount"]["currency"]["name"],
                }
        operation_list.append(unit)
    except KeyError:
      continue
  return operation_list


