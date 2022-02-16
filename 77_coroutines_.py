def searcher():
    import time
    # some 4 seconds time consuming task
    book = "This is a book on gaurav and code with gaurav and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("Search started")
next(search)
print("Next method run")
search.send("gaurav")

search.close()
# input("Press any key")
search.send("gaurav and")