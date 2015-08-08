from time import sleep
import requests
import sys
import webbrowser

_MIN_WAIT_TIME = float(0)
_TUP_STATUS = 0
_TUP_URL = 1
_TUP_HEADER_RETRY_AFTER = 2

def __get_random_url(sesh):
    r = sesh.get('http://reddit.com/r/random/', allow_redirects=True)
    return r.status_code, r.url, r.headers.get('Retry-After', _MIN_WAIT_TIME)

def __session_loop_rand(expected_count, url_set):
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

def __user_amount(attempts):
    user_input = input('How many random results do you want? ')
    while not isinstance(user_input, int):
        user_input = input('How many random results do you want? ')
        try:
            user_input = int(user_input)
        except ValueError:
            print("Expected number value. Try again.\n")
    return user_input

def __open_result_tabs(final_set):
    for found_url in final_set:
        webbrowser.open_new_tab(found_url)

def main():
    request_amount = __user_amount(0)
    my_set = set()
    __session_loop_rand(request_amount, my_set)
    sys.stdout.write("\r100%")
    sys.stdout.flush()
    print("\nOpening tabs...")
    __open_result_tabs(my_set)

if __name__ == '__main__':
    main()
