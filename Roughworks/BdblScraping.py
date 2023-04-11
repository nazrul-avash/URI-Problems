import requests
from bs4 import BeautifulSoup
branchInfo = {}
file = open("BranchList.txt","w")
req= requests.get("https://bdbl.com.bd/site/page/a6d8eb47-c779-40c7-a136-c063d88229f3/-")
soup = BeautifulSoup(req.content, "html5lib")
tab = soup.find_all("table")
for t in tab:
    branchInfo[t.h3.text.strip()] =t.h4.text.strip()
for key, value in branchInfo.items():
    print(key)
    file.write(key+":\n"+value+"\n")
    file.write("\n")
