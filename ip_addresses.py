# Jessie Chapman
# Lab 2: ip_addresses.py - lists all possible IPv4 addresses
# Date: 2/20/2014                        

def addresses():
        IP = ""
        for i in range(256):
                first = IP + str(i) + "."
                for j in range(256):
                        second = IP + str(j) + "."
                        for k in range(256):
                                third = IP + str(k) + "."
                                for l in range(256):
                                        fourth = IP + str(l)
                                        IP = first + second + third + fourth
                                        print IP
                                        IP = ""

if __name__ == '__main__':
        addresses()
