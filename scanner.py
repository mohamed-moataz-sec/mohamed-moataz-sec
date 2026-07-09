import os

target_ip = input("Enter the target IP address: ")

print("Scanning process started for: " + target_ip)


response = os.system("ping -c 1 " + target_ip)

if response == 0:
    print("Host is UP!")
else:
    print("Host is DOWN!")
  
