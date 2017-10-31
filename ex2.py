import subprocess
import os

#first we are going to dig each domain before going to scrawl it.
#we will save each domain's dig record into a file which have name
#like domain and append dig at the end.

#function domain_data's list variable
u_dom_name = []

#function will open file which contains domain name
#save the result in variable u_dom_name as list

def domain_data():
    u_ask_file_name = input("Please provide us a file \n")
    if os.path.exists('{}'.format(u_ask_file_name)):
        print("yes")
    else:
        print("FILE DOESN'T EXISTS")
        exit()
    u_file = open(r"{}".format(u_ask_file_name),'r')
    u_data = str(u_file.read()).split("\n")
    for i in u_data:
        u_dom_name.append(i)
    u_file.close()
    # print(u_dom_name)


#The function will going to dig domain
#save result in a variable called u_dig_result
#parse that u_dig_result to get these attributes
#status and ANSWER SECTION
#if status is NXDOMAIN then do nothing.
#if status is NOERROR open file domain_dig add domain's name, A record and MX record

#function domain_data's list variable
u_dig_list = []

def get_dns():
    count = 0
    while count < len(u_dom_name):
        for i in u_dom_name:
            u_list = subprocess.Popen(["dig", "{}".format(i), "A", "+short"], stdout=subprocess.PIPE)
            u_output = u_list.communicate()
            u_str_output = str(u_output)
            u_dig_list.append(u_str_output[3:18])
            u_dig_f = open(r'domain_dig','a')
            u_dig = u_dig_f.write(i + "\n" + " IP " + "\n"  + u_dig_list[count] + "\n")
            count += 1
    u_dig_f.close()

domain_data()
get_dns()
