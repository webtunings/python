import telnetlib

user = 'gns3'
password = 'cisco'

hosts = ['100.1.1.3', '100.1.1.4']

for HOST in hosts:
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