import customtkinter as ctk
from sharedlogic import search
from sharedlogic import authorization
import requests
from requests import get,post
import colorama
from colorama import Fore,Style
import json

class gui():
	def button():
		print("button pressed")


	app = ctk.CTk()
	app.title("Statify")
	app.geometry("800x300")


	def temp_search_function():
		query="madk1d"
		Qtypes=["track","artist","album"]
		types=["tracks","artists","albums"]
		Qsearch_type=Qtypes[2-1]
		search_type = types[1]

		url="https://api.spotify.com/v1/search"
		header= authorization.get_auth_header(authorization.token)
		search=f"?q={query}&type={Qsearch_type}&limit=1"

		search_url=url+search
		result=get(search_url,headers=header)
		json_result=json.loads(result.content)[search_type]["items"]
		print(Fore.GREEN+ json_result[0]["name"] + Style.RESET_ALL)

		for final_answer in json_result:
			print(Fore.GREEN + final_answer["name"]+Style.RESET_ALL)

	button = ctk.CTkButton(app, text="search", command=temp_search_function)
	button.grid(row=0, column=0, padx=20, pady=20)

	app.mainloop()