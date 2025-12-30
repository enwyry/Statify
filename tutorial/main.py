import os,sys,time,base64,json,signal
from gui import gui
from sharedlogic import search,authorization
from time import sleep
from colorama import Fore,Style
from dotenv import load_dotenv
from requests import post,get
from effects import print,nprint #type:ignore (gives warning idk why but it works)
load_dotenv()


def main():
	print("what do you want to do? [1=search] ")
	todo_answer=int(input())

	if todo_answer==1:
		search(authorization.token)

	print("\nrestart? y/n")
	confirmation_restart=input()
	pid = os.getpid()

	if confirmation_restart=="y":
		main()
	elif confirmation_restart=="n":
		print("PID: "+str(pid))
		sys.exit(0)
	else:
		print("invalid argument. exiting...")
		print("PID: "+os.getpid())
		sleep(2)
		sys.exit(0)
		
main()