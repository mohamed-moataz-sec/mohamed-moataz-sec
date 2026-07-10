import os

target_ip = input("Enter the target IP address: ")

print("Scanning process started for: " + target_ip)

response = os.system("ping -c 1 " + target_ip)


with open("results.txt", "a") as file:
    if response == 0:
        result = target_ip + " is UP!"
        print(result)
        file.write(result + "\n")  
    else:
        result = target_ip + " is DOWN!"
        print(result)
        file.write(result + "\n")

print("Result has been saved to results.txt")


print("Scanning process started for: " + target_ip)


response = os.system("ping -c 1 " + target_ip)

if response == 0:
    print("Host is UP!")
else:
    print("Host is DOWN!")
  
>>>>>>> ae45ef7b08bf2fe8a0e2ce1ead2db6585dab5015
