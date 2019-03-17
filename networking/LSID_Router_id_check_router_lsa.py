import re
import time
import telnetlib

user = 'gns3'
password = 'cisco'

hosts = ['100.1.1.3', '100.1.1.4', '100.1.1.2', '100.1.1.1', '101.6.11.1', '101.5.6.1', '101.4.6.1', '101.7.8.1', '101.7.8.2']

for HOST in hosts:
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"terminal length 0\n")
    time.sleep(1)
    tn.read_very_eager()
    tn.write(b"show ip ospf database\n")
    time.sleep(1)
    router_output = tn.read_very_eager()
    print("******************************************************************")
    #print("ospf data:",router_output.decode('ascii'))
    str_output = str(router_output,'utf-8')
    print("ascii string", str_output)
    matches = re.findall(r'^\d.*\s\d+\s$', str_output, re.MULTILINE)
    print("matches = ", len(matches))

    for match in matches:
        lsa = match.split()
        print("Link ID = ", lsa[0])
        print("ADV Router = ", lsa[1])
        if lsa[0] == lsa[1]:
            print("matching")

    tn.write(b"exit\n")
    time.sleep(1)

