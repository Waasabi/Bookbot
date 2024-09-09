The_alpha ={}
#{"a":0 ,"b":0,"c":0,"d":0, "e":0,"f":0,"g":0, "h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars = count_chars(text)
    report_Books(chars,book_path,words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    list= string.split()
    return(len(list))

def count_chars(string):
    The_alpha ={}
    for n in string :
        Text = n.lower()
        if Text in The_alpha:
            The_alpha[Text]+=1            
        else:
            The_alpha[Text]=1
    return(The_alpha) 
def sort_on(dict):
    return dict["num"]


  
def report_Books(dic,book,words):
    print(f'--- Begin report of {book} --- \n')
    print(f"{words} words found in the document \n")
    for n in dic:
       if n.isalpha():
            print(f"The '{n}' character was found {dic[n]} times")
    print('\n--- End report ---')
main()
