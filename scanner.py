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
