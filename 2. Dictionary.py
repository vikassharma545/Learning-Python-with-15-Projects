
import difflib

class Dictionary:
    
    def __init__(self) -> None:
        
        with open("2. Oxford English Dictionary.txt") as d:
            self.raw_dictinory = d.read()
            
        # split lines
        self.raw_dictinory = self.raw_dictinory.split("\n")
        
        # removing line having one word or empty string
        self.raw_dictinory = filter(lambda item: len(item.split()) > 1, self.raw_dictinory)
        
        # dictinory dict
        self.dictionory_data = {value.split(maxsplit=1)[0].title() : value.split(maxsplit=1)[-1] for value in self.raw_dictinory}
        
        # word_lst
        self.word_list = list(self.dictionory_data.keys())
        
    def find_related_word(self, word):
        word = word.title()
        similar = difflib.get_close_matches(word, self.word_list, n=5)
        return similar
        
    def search_word(self, word):
        
        word = word.title()
        
        if word in self.dictionory_data:
            word_data = self.dictionory_data[word]
            print(word_data.replace('.', '.\n'))
        else:
            print(f"Word - '{word}' not Found !!!")
            print("Do u mean? -", *self.find_related_word(word))
            
if __name__ == "__main__":
    
    dict = Dictionary()    
    dict.search_word("appel")