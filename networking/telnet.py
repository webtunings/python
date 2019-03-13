import getpass
import telnetlib

HOST = "100.1.1.3"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"show ip ospf neighbor\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))

#gns3
#cisco