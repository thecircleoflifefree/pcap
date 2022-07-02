def scope_test():
    def do_local():
        spam = "local spam"
    spam = "test spam"
    do_local()
    print("spam:", spam)


scope_test()

