calls = 0

def count_call ():
    global calls
    calls += 1
    return
def string_info (string):
    count_call()
    return len(string), string.upper(), string.lower()
def is_contains (string, list_to_search):
    count_call()
    return string.upper() in (i.upper() for i in list_to_search)

result1 = string_info('Dobrokrot')
result2 = string_info('Svinomorj')
result3 = is_contains('Urban', ['ban', 'BaNAN', 'urBAN'])
result4 = is_contains('cycle', ['recycling', 'cyclic'])






print('string_info:', result1)
print('string_info:', result2)
print('is_contains:', result3)                                #'Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print('is_contains:', result4)
print(calls)                                                   #'cycle', ['recycling', 'cyclic'])) # No matches




