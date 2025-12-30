import os,sys,time,base64,json
from time import sleep
from colorama import Fore,Style
from dotenv import load_dotenv
from requests import post,get
from effects import print,nprint #type:ignore (gives warning idk why but it works)
load_dotenv()

client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")

class authorization:
	def get_token():
		auth_string = client_id + ":" + client_secret
		auth_bytes = auth_string.encode("utf-8")
		auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
		url="https://accounts.spotify.com/api/token"
		headers ={
			"Authorization": "Basic " + auth_base64,
			"Content-Type": "application/x-www-form-urlencoded"
		}
		data={"grant_type": "client_credentials"}
		result= post(url, headers=headers, data=data)
		json_result=json.loads(result.content)
		token=json_result["access_token"]

		#extra info
		nprint(auth_string, Fore.GREEN + "this is the auth_string"+Style.RESET_ALL)
		nprint(auth_bytes, Fore.GREEN + "this is the auth_bytes"+Style.RESET_ALL)
		nprint(auth_base64, Fore.GREEN + "this is the auth_base64"+Style.RESET_ALL)

		return token

	token=get_token()
	nprint(token, Fore.GREEN + "this is the token"+Style.RESET_ALL)


	def get_auth_header(token):
		return {"Authorization": "Bearer " + token}

	def logs(): #nice to see what functions were executed
		if authorization.token:
			print("-------------------------------token function done-----------------------------------")
		else:
			print("ERROR with get_token")

		if authorization.get_auth_header(authorization.token):
			print("-------------------------auth header function done-----------------------------------")
		else:
			print("ERROR with get_auth_header")

authorization.logs()

#search tracks,artists or albums
def search(token):
	print("what do you want to search (~ for test) ")
	query_raw=input()
	query=query_raw.replace(" ","+")

	Qtypes=["track","artist","album"]
	types=["tracks","artists","albums"]
	if query_raw!="~" and query!="~":
			print("what type? [1=tracks,2=artists,3=albums] ")
			Qsearch_type = Qsearch_type_temp = int(input())
			Qsearch_type = Qtypes[Qsearch_type-1]
			search_type = types[Qsearch_type_temp-1]
	
			url="https://api.spotify.com/v1/search"
			header= authorization.get_auth_header(token)
			search=f"?q={query}&type={Qsearch_type}&limit=10"

	elif query_raw=="~" or query=="~":
			query="madk1d"
			Qsearch_type=Qtypes[2-1]
			search_type = types[1]

			url="https://api.spotify.com/v1/search"
			header= authorization.get_auth_header(token)
			search=f"?q={query}&type={Qsearch_type}&limit=1"

	search_url=url+search
	result=get(search_url,headers=header)
	json_result=json.loads(result.content)[search_type]["items"]
	# nprint(json_result) #I just used this for testing	
	# print(Fore.GREEN + "this was the json_result\n" + Style.RESET_ALL)
	print(Fore.GREEN+ json_result[0]["name"] + Style.RESET_ALL) #one song
	
	for final_answer in json_result:
		print(Fore.GREEN + final_answer["name"]+Style.RESET_ALL)