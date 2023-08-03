import requests

def get_definition(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    request = requests.get(url)
    if request.status_code == 200:
        response = request.json()
        definition = response[0]["meanings"][0]["definitions"]
        
        print()
        print("Word: " + word)
        print("---"*20)

        count = 0
        for d in definition:
            count = count + 1
            print(str(count) + ". "+ d['definition'])
            print()
  

def main():
    word = input("Enter a word: ")
    definition = get_definition(word)
 

if __name__ == "__main__":
    main()
