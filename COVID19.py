import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


# URL
URL = getdata('https://www.mohfw.gov.in/')
soup = BeautifulSoup(URL, 'html.parser')
DATA = ""

# Dictionary of states!
states = {0: 'Total Number Of Cases In India'}

# To get State Data
stateList = []
for tr in soup.find_all('tbody')[0].find_all('tr'):
    sL = tr.get_text()[1:]
    sList = sL.split("\n")[:2]
    stateList.append(sList)
for state in stateList:
    if state[0] == 'Total number of confirmed cases in India':
        break
    states[int(state[0])] = ' '.join(list(state[1].strip().split()))
print()
print("-----------------------------------------------------------")
print("Choose a Value [State / UT]:")
print("---------------")
for keys, values in states.items():
    print(keys, ":", values)
print("-----------------------------------------------------------")
print('ENTER "STOP" to stop the Execution!')
print("-----------------------------------------------------------")

# To get Header Data
for tr in soup.find_all('thead')[0].find_all('tr'):
    myhead = tr.get_text()[1:]
    head_list = myhead.split("\n")
s = 0
flag = False
while (True):
    selectedState = input("Enter a Value: ").upper()
    if selectedState == "STOP":
        break
    else:
        selectedState = int(selectedState)
        if selectedState < 0 or selectedState > (len(states)-1):
            print("Invalid Input: 'Enter Valid State Value'")
            break
    s = 0

    # To get Body Data
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        DATA = tr.get_text()
        DATA1 = DATA[1:]
        state_list = DATA1.split("\n")
        if state_list[1] == states[selectedState]:
            details = f" State :- " + state_list[1] + "\n" + head_list[2] + ": " + \
                state_list[2]+"\n" + "Total number of "+head_list[3]+" : " + \
                state_list[3] + "\n" + \
                "Total number of Death : " + state_list[4]
            print(details)
        if selectedState == 0 and state_list[0] == "Total number of confirmed cases in India":
            print("-----------------------------------------------------------")
            print("Total number of confirmed cases in India :", state_list[1])
            print("-----------------------------------------------------------")
    print()
print("-----------------------------------------------------------")
