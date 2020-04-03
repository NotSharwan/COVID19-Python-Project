from plyer import notification
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


myhtmldata = getdata('https://www.mohfw.gov.in/')
soup = BeautifulSoup(myhtmldata, 'html.parser')
mydata = ""
states = {0: 'Total Number Of Cases In India',
          1: 'Andhra Pradesh',
          2: 'Andaman and Nicobar Islands',
          3: 'Assam',
          4: 'Bihar',
          5: 'Chandigarh',
          6: 'Chhattisgarh',
          7: 'Delhi',
          8: 'Goa',
          9: 'Gujarat',
          10: 'Haryana',
          11: 'Himachal Pradesh',
          12: 'Jammu and Kashmir',
          13: 'Jharkhand',
          14: 'Karnataka',
          15: 'Kerala',
          16: 'Ladakh',
          17: 'Madhya Pradesh',
          18: 'Maharashtra',
          19: 'Manipur',
          20: 'Mizoram',
          21: 'Odisha',
          22: 'Puducherry',
          23: 'Punjab',
          24: 'Rajasthan',
          25: 'Tamil Nadu',
          26: 'Telengana',
          27: 'Uttarakhand',
          28: 'Uttar Pradesh',
          29: 'West Bengal'}
print("-----------------------------------------------------------")
print("Choose a Value [State / UT]:")
print("---------------")
for keys, values in sorted(states.items()):
    print(keys, ":", values)
print("-----------------------------------------------------------")
print('ENTER "STOP" to stop the Execution!')
print("-----------------------------------------------------------")

s = 0
flag = False
while (True):
    selectedState = input("Enter a Value: ").upper()
    if selectedState == "STOP":
        break
    else:
        selectedState = int(selectedState)
        if selectedState < 0 or selectedState > 29:
            print("Invalid Input: 'Enter Valid State Value'")
            break
    s = 0
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        mydata = tr.get_text()
        mydata1 = mydata[1:]
        state_list = mydata1.split("\n")
        if state_list[1] == states[selectedState]:
            details = f" State :- " + state_list[1] + "\n" + "Total Confirmed Cases(Including 55 foreign Nationals) :" + \
                state_list[2]+"\n" + "Total number of Cured/Discharged/Migrated :" + \
                state_list[3] + "\n" + \
                "Total number of Death :" + state_list[4]
            print(details)
        if selectedState == 0 and state_list[0] == "Total number of confirmed cases in India":
            print("-----------------------------------------------------------")
            print("Total number of confirmed cases in India :", state_list[1])
            flag = True
    if flag:
        print(state_list[0])
        flag = False
        print("-----------------------------------------------------------")
    print()
print("-----------------------------------------------------------")
