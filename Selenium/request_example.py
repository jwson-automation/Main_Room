import requests, json
URL = 'http://www.tistory.com'
response = requests.get(URL)
j = response.status_code
k = response.text

params = {'param1':'value1', 'param2':'value'}
res = requests.get(URL,params=params)

l =res.url

print(l)

# data = {'outer': {'ineer':'value'}}
# res = requests.post(URL, data=json.dumps(data))

# print

# res.request # 내가 보낸 request 객체에 접근 가능
# res.status_code # 응답 코드
# res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동
# res.json() # json response일 경우 딕셔너리 타입으로 바로 변환
