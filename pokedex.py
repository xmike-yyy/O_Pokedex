#Importing packages
import urllib.request, json, time, requests
from cgitb import html
from re import S
from traceback import print_tb
from urllib import request
from bs4 import BeautifulSoup

#Loading in JSON
with urllib.request.urlopen("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json") as url:
    data = json.loads(url.read().decode())

#Search Pokemon within Dictionary
def searchPokemon():
    print("Welcome to the Online Pokédex!")
    time.sleep(1)
    exist = False
    while exist == False:
        n = input("Which Pokemon do you want to know?")
        x = n.capitalize()
        found = False
        while found == False:
            for i in data:
                if x == i["name"]["english"]:
                    found = True
                    print("Pokémon Requested:", x)
                    time.sleep(0.5)
                    print("Chinese:", i["name"]["chinese"])
                    time.sleep(0.5)
                    print("French:", i["name"]["french"])
                    time.sleep(0.5)
                    print("Japanese:", i["name"]["japanese"])
                    time.sleep(0.5)
                    print("Type:", i['type'][0])
                    time.sleep(0.5)
                    print("Base Health:", i["base"]["HP"])
                    time.sleep(0.5)
                    print("Base Attack:", i["base"]["Attack"])
                    time.sleep(0.5)
                    print("Base Defense:", i["base"]["Defense"])
                    time.sleep(0.5)
                    print("Base Sp. Attack:", i["base"]["Sp. Attack"])
                    time.sleep(0.5)
                    print("Base Sp. Defense:", i["base"]["Sp. Defense"])
                    time.sleep(0.5)
                    print("Base Speed:", i["base"]["Speed"])
                    exist = True
            break;
        if found == False:
            print("Does not exist, please try again.")
            time.sleep(0.5)
    #Providing description of Pokemon upon request
    desc = False
    vers = False
    time.sleep(0.5)
    while desc == False:
        a = input("Do you want a description? Please type y for Yes or any other key for No. \n").lower()
        time.sleep(0.5)
        if a != "y":
            print("Thank you for using this!")
            desc = True
            break;
        else:
            #Web-Scraping
            n_url = "https://www.pokemon.com/us/pokedex/{}".format(n)
            r = requests.get(n_url)
            doc = BeautifulSoup(r.text, "html.parser")
            result = doc.get_text()
            while vers == False:
                #Selecting Version of Description for Pokemon
                b = input("Which version do you want? Please type x for version X and y for version Y. \n")
                time.sleep(0.5)
                if b == "x":
                    tag = doc.find(class_= "version-x")
                    print("Description: ", tag.get_text(strip=True))
                    break
                elif b == "y":
                    tag = doc.find(class_= "version-y")
                    print("Description: ", tag.get_text(strip=True))
                    break
                else:
                    print("Please try again. ")
                    time.sleep(0.5)
            break
    time.sleep(1)
    print("Finished usage, shutting down...")


#Initiating Script 
if __name__ == "__main__":
    searchPokemon()
