class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdrawal(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            self.withdraw(amount)

a = MinimumBalanceAccount(100)
print(a.deposit(100))
print(a.withdrawal(40))

b = MinimumBalanceAccount(100)
print(b.deposit(1000))
print(b.withdrawal(30))
print(b.balance)


























































'''
import re
from time import ctime

str = """Tue Mar 22 18:01:06.601 UTC
Mar 22 12:05:29.965 OTNLC_DOP10_LT_DIRdop100/config 0/LC0 t9035 otnlc_dop100_check::register access failed for slot  [9]
Mar 22 14:50:09.319 OTNLC_DOP10_LT_DIRdop100/config 0/LC0 t676 otnlc_dop100_check::register access failed for slot  [4]
Mar 22 17:08:01.154 OTNLC_DOP10_LT_DIRdop100/config 0/LC0 t1523 otnlc_dop100_check::register access failed for slot  [14]"""


result = re.search(r'otnlc_dop100_check::register access failed for slot',str)
if result:
    print("failure")
else:
    print("no failure")


file_name = result.group(1)
print(file_name)

current_time = ctime()
file_name = '192.0.44.1_var_log_' + current_time.replace(' ','')
print(file_name + "123")


result = str.find(expected_str)

if result !=1:
    print("match found", result)
else:
    print("match not found")


r = re.findall(r'Node Ready',str)
print(len(r))
result_dmesg = re.search(r'pcieport .*? Device .*? Stopped Responding, Disabling the link',host_dmesg_output)

if result_dmesg:
    print("found Stopped Responding, Disabling the link. exiting")
    print(result_dmesg.group())
    #sys.exit()
else:
    print("no issue in dmesg")'''