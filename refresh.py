import os
import getpass

os.chdir("/Users/"+str(getpass.getuser())+"/Library/Application Support/Google/chrome/Default")
os.remove("Top Sites")
os.remove("Top Sites-journal")

print("Chrome 'Most Visited' Updated!")