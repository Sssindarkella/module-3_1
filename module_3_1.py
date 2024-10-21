calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string, c = None):
    count_calls()
    if c is None:
        c = ()
    c = len(string), string.upper(), string.lower()
    print(c)

def is_contains(string, list_to_search = []):
    count_calls()
    for i in list_to_search:
        if string in list_to_search:
            print("True")
            break
        else:
            print('False')
            break

string_info('Anna')
string_info('Tamara')
is_contains('Anna', ['Masha', 'Anna', 'Katya'])
is_contains('Anna', ['Masha', 'Tanya', 'Katya'])
print(calls)

