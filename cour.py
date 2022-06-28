def searcher():
    import time
    # some 4 secs task
    book = "this is mirage and mirage is a good boy and rhea is a beautiful girl"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text is in your book")
        else:
            print("your text is not in the book")

search = searcher()
next(search)
input("press any key")
search.send("mriage is a good boy")