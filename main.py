import json
import requests
 
zc = input_data[‘submissionID’]
url = 'https://fds.jotform.com/API/submission/' + zc + '?apiKey=*************************'
response = requests.get(url)
response.raise_for_status() # optional but good practice in case the call fails!
data = response.json()
data['line_items'] = []
for line in data['content']['answers']:
    answer = data['content']['answers'][line]
    if "answer" in answer:
        drugArray = answer['answer']
        try:
            if "Drug name" in drugArray:
                drugArray = drugArray.replace('Eye(s) to treat', 'Eyes to treat')
                drugArray = json.loads(drugArray)
                for drugData in drugArray:
                    data['line_items'].append(drugData)
        except:
            continue
return {"output": json.dumps(data)}