from random import randint
import praw
import getpass
from colorama import init, Fore

def printemptyline():
	print(Fore.GREEN + username + "@" + "reddit.com$ " + Fore.WHITE, end="")

def printnewline(string_to_print=""):
	print(Fore.GREEN + username + "@" + "reddit.com$ " + Fore.WHITE + str(string_to_print), end="")	
	print("")

def printinfo(string_to_print):
	print(Fore.GREEN + username + "@" + "reddit.com$ " + Fore.WHITE + str(string_to_print))	
	printemptyline()

def subreddit_browse(subreddit_name):
	subreddit_content = r.get_subreddit(subreddit_name)
	i = 1
	for post in subreddit_content.get_hot():
		printnewline(Fore.MAGENTA + "[" + subreddit_name + "] " + Fore.WHITE + str(i) +" " + str(post))
		i = i + 1
	printinfo("Press 'x' if you want to move out of this sub, else type the 'id' of the post you want to see")


r = praw.Reddit(user_agent="vishnugt reddit client on development")
print(Fore.CYAN + "***Welcome to Reddit CLI***")
print("    Your connection id to Reddit is " + str(randint(10,99)))
print("    Server version: 1.7.23 RedditCLI Server (RCS)")
print("")
print("Copyright (c) 2015, 2016, RedditCLI and/or its affiliates.  All rights reserved.")
print("")
print("Type 'help' or 'h' for a list of available commands and give 'man command' to know more about the command")
print("" + Fore.WHITE)
print(Fore.GREEN + "(none)@reddit.com$ " + Fore.WHITE + "Please enter your username to continue: ",end="")
username = input()
printnewline("Welcome " + username + "!!")
printnewline("Subreddit you wanna browse (Example: dota2)")
printemptyline()
subreddit_browse(input())
#printinfo("Its a pleasure!")
nextcommand = input()
if nextcommand == "quit":
	exit()
#password = getpass.getpass("Please enter your password: ")