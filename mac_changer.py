import subprocess

int_face = input("Enter the interface name whose mac address is to be changed:")
mac_id = input("Enter the mac id u want to change:")
subprocess.call("ifconfig " + int_face + " down", shell=True)
subprocess.call("ifconfig " + int_face + " hw ether " + mac_id, shell=True)
subprocess.call("ifconfig " + int_face + " up", shell=True)
print("Command Executed!")