from time import sleep
import requests
import sys
import webbrowser

_MIN_WAIT_TIME = float(0)
_TUP_URL = 0
_TUP_HEADER_RETRY_AFTER = 1
_REDDIT_RANDOM_URL = 'http://reddit.com/r/random/'

def __get_random_url(sesh):
    request = sesh.get(_REDDIT_RANDOM_URL, allow_redirects=True)
    return request.url, request.headers.get('Retry-After', _MIN_WAIT_TIME)

def collect_urls(expected_count, url_set):
    s = requests.Session()
    wait_time = _MIN_WAIT_TIME
    entry_iter = 0
    current_count = expected_count
    while current_count > 0:
        sleep(wait_time)
        resultTup = __get_random_url(s)
        wait_time = float(resultTup[_TUP_HEADER_RETRY_AFTER])
        current_percent = (1-(current_count/expected_count))*100
        sys.stdout.write("\r%d%%" % current_percent)
        sys.stdout.flush()
        if "/r/random/" not in resultTup[_TUP_URL]:
            current_count-=1
            entry_iter+=1
            url_set.add(resultTup[_TUP_URL])
    __final_print()

def user_amount():
    user_input = None
    while not isinstance(user_input, int):
        user_input = input('How many random results do you want? ')
        try:
            user_input = int(user_input)
        except ValueError:
            print("Expected number value. Try again.\n")
    return user_input

def open_result_tabs(final_set):
    print("\nOpening tabs...")
    for found_url in final_set:
        webbrowser.open_new_tab(found_url)

def __final_print():
    sys.stdout.write("\r100% done.\n")
    sys.stdout.flush()

def main():
    request_amount = user_amount()
    my_set = set()
    collect_urls(request_amount, my_set)
    open_result_tabs(my_set)

if __name__ == '__main__':
    main()
