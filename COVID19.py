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
          3: 'Arunachal Pradesh',
          4: 'Assam',
          5: 'Bihar',
          6: 'Chandigarh',
          7: 'Chhattisgarh',
          8: 'Delhi',
          9: 'Goa',
          10: 'Gujarat',
          11: 'Haryana',
          12: 'Himachal Pradesh',
          13: 'Jammu and Kashmir',
          14: 'Jharkhand',
          15: 'Karnataka',
          16: 'Kerala',
          17: 'Ladakh',
          18: 'Madhya Pradesh',
          19: 'Maharashtra',
          20: 'Manipur',
          21: 'Mizoram',
          22: 'Odisha',
          23: 'Puducherry',
          24: 'Punjab',
          25: 'Rajasthan',
          26: 'Tamil Nadu',
          27: 'Telengana',
          28: 'Uttarakhand',
          29: 'Uttar Pradesh',
          30: 'West Bengal'}
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
        if selectedState < 0 or selectedState > 30:
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
