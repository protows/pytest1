import requests
import json
from conf.configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages

payload_dict = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
createDog = requests.post(url=SERVICE_URL, json=payload_dict)
received_posts = createDog.json()
assert received_posts['name'] == 'doggie', GlobalErrorMessages.WRONG_NAME.value

delete_url= SERVICE_URL + '/' + str(received_posts['id'])
deleteDog = requests.delete(url=delete_url, json=payload_dict)
delete_received_posts = deleteDog.json()
assert delete_received_posts['code'] == 200, GlobalErrorMessages.WRONG_DELETE_CODE.value

