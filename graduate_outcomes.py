import requests

def make_api_request(url = "https://data.cityofnewyork.us/resource/ns8x-c6af.json"):
    request_content = requests.get(url)
    outcomes = request_content.json()
    return outcomes
    
def get_total_grads():
    grad_info = make_api_request()
    total = 0
    for grad in grad_info:
        if grad['total_grads_n'] != "s":
            total += int(grad['total_grads_n'])
    return total

def get_total_dropped_out():
    grad_info = make_api_request()
    total = 0
    for dropout in grad_info:
        if dropout['dropped_out_n'] != "s":
            total += float(dropout['dropped_out_n'])
    return int(total)

def get_years():
    all_info = make_api_request()
    for grad in all_info:
        print(grad["cohort"])
    pass

# print(get_years())