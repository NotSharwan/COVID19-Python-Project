from plyer import notification
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


myhtmldata = getdata('https://www.mohfw.gov.in/')
soup = BeautifulSoup(myhtmldata, 'html.parser')
mydata = ""
states = {1: 'Andhra Pradesh',
          2: 'Andaman and Nicobar Islands',
          3: 'Bihar',
          4: 'Chandigarh',
          5: 'Chhattisgarh',
          6: 'Delhi',
          7: 'Goa',
          8: 'Gujarat',
          9: 'Haryana',
          10: 'Himachal Pradesh',
          11: 'Jammu and Kashmir',
          12: 'Karnataka',
          13: 'Kerala',
          14: 'Ladakh',
          15: 'Madhya Pradesh',
          16: 'Maharashtra',
          17: 'Manipur',
          18: 'Mizoram',
          19: 'Odisha',
          20: 'Puducherry',
          21: 'Punjab',
          22: 'Rajasthan',
          23: 'Tamil Nadu',
          24: 'Telengana',
          25: 'Uttarakhand',
          26: 'Uttar Pradesh',
          27: 'West Bengal'}
print("-----------------------------------------------------------")
print("Select a State:")
for keys, values in sorted(states.items()):
    print(keys, ":", values)
print("-----------------------------------------------------------")
print('ENTER "STOP" to stop the Execution!')
print("-----------------------------------------------------------")
while (True):
    selectedState = input("Enter the State Value: ").upper()
    if selectedState == "STOP":
        break
    else:
        selectedState = int(selectedState)
        if selectedState <= 1 or selectedState >= 27:
            print("Invalid Input: 'Enter Valid State Value'")
            break
    for tr in soup.find_all('tbody')[9].find_all('tr')[0:27]:
        mydata = tr.get_text()
        mydata1 = mydata[1:]
        state_list = mydata1.split("\n")
        details = f" State :- " + state_list[1] + "\n" + "Total number of Indian cases:" + \
            state_list[2]+"\n" + "Total number of Foreign cases:" + \
            state_list[3]+"\n" + "Total number of Cured:" + \
            state_list[4]+"\n" + "Total number of Death:" + state_list[5]
        if state_list[1] == states[selectedState]:
            print(details)
    print()
print("-----------------------------------------------------------")
