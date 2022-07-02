list_1 = [5, 8, 34]
tuple_1 = ('t', 'y', 'v')
set_1 = {4, 7, 9}
dict_1 = {"a": "1", "b": "2"}
try:
    print(dict(list_1))
except Exception as e:
    try:
        print(dict(tuple_1))
    except Exception as ex:
        try:
            print(dict(set_1))
        except Exception as exc:
                print("e -> ", e)
                print("ex -> ", ex)
                print("exc -> ", exc)

try:
    print(dict(dict_1))
except Exception as exce:
        print("exce -> ", exce)
