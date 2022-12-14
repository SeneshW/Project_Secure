import requests
from pprint import pprint
from bs4 import BeautifulSoup as bsoup
from urllib.parse import urljoin

import colorama
from colorama import Fore


def get_forms(url):
    """Given a `url`, it returns all forms from the HTML content"""
    beaSoup = bsoup (requests.get(url).content, "html.parser")
    return beaSoup.find_all("form")


def get_fdetails(form):
    """
    This function extracts all possible useful information about an HTML `form`
    """
    details = {}
    # get the form action (target url)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def form_submit(form_details, url, value):
    """
    Submits a form given in `form_details`
    Params:
        form_details (list): a dictionary that contain form information
        url (str): the original URL that contain that form
        value (str): this will be replaced to all text and search inputs
    Returns the HTTP Response after form submission
    """
    # construct the full URL (if the url provided in action is relative)
    target_url = urljoin(url, form_details["action"])
    # get the inputs
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # replace all text and search values with `value`
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and value are not None,
            # then add them to the data of form submission
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)


def xss_scan(url):
    """
    Given a `url`, it prints all XSS vulnerable forms and
    returns True if any is vulnerable, False otherwise
    """
    # get all the forms from the URL
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</scripT>"
        # returning value
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = get_fdetails(form)
        content = form_submit(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print('\n')
            print('\033[1m' + " THIS IS VULNERABLE FOR XSS ATTACKS" '\033[0m')
            is_vulnerable = True
            # won't break because we want to print other available vulnerable forms    
        
    return is_vulnerable

print ('\n')
print (Fore.YELLOW + ' ##     ##  ######   ######      ######   ######     ###    ##    ## ##    ## ######## ########  ')
print ('  ##   ##  ##    ## ##    ##    ##    ## ##    ##   ## ##   ###   ## ###   ## ##       ##     ## ')
print ('   ## ##   ##       ##          ##       ##        ##   ##  ####  ## ####  ## ##       ##     ## ')
print ('    ###     ######   ######      ######  ##       ##     ## ## ## ## ## ## ## ######   ########  ')
print ('   ## ##         ##       ##          ## ##       ######### ##  #### ##  #### ##       ##   ##   ')
print ('  ##   ##  ##    ## ##    ##    ##    ## ##    ## ##     ## ##   ### ##   ### ##       ##    ##  ')
print (' ##     ##  ######   ######      ######   ######  ##     ## ##    ## ##    ## ######## ##     ## ')

if __name__ == "__main__":
    url = input(Fore.WHITE + '\n\nEnter the URL that should be scanned: ')
    print ('\n')
    xss_scan(url)

print ('\n---------------------------------------------------------------------------\n')

print ('Would you like to do another scan?')
print ('  [1] Yes')
print ('  [2] No')

selection = input('\nPlease enter the number: ')

if selection == "1":
  import isp_project.py

else:
  print('\n    - Thank you for using' '\033[1m' + " Project Secure! " '\033[0m' '-\n')
  exit ()

