import json

import requests


from credentials import headers, organization, project, team


### Requisição para coletar sprint atual e recuperar a ID ###
iteration_url = f"https://dev.azure.com/{organization}/{project}/{team}/_apis/work/teamsettings/iterations?$timeframe=current&api-version=7.0"
response = requests.get(iteration_url, headers=headers)
response.raise_for_status()
iteration = response.json()

### Carregar o JSON ###
iteration_string = json.dumps(iteration)
data = json.loads(iteration_string)

### Acessar o valor de "id"
id_value = data["value"][0]["id"]

### Requisição utilizando a ID da sprint corrrente coletada como referência na proxima chamada ###
iterationId = id_value
iterationId_url = f"https://dev.azure.com/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/workitems?api-version=7.0"
response = requests.get(iterationId_url, headers=headers)
response.raise_for_status()
iterationId = response.json()

### Carregar o JSON ###
iterationId_string = json.dumps(iterationId)
data = json.loads(iterationId_string)
workitens = [item["target"]["id"] for item in data["workItemRelations"]]

#### Convertendo a list para string ###
workitem_string = ""
count = len(workitens) - 1
n = 0
for item in workitens:
    if n == count:
        workitem_string = workitem_string + str(item)
    else:
        workitem_string = workitem_string + str(item) + ", "
    n = n + 1

### Requisição utilizando as IDS dos work itens como referencia da próxima chamada ###
ids = workitem_string
workitens_url = f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems?ids={ids}&$expand=all&api-version=7.00"
response = requests.get(workitens_url, headers=headers)
response.raise_for_status()
ids = response.json()
print(ids)
