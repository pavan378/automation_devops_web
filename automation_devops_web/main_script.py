import subprocess
import re
import time
import argparse

def countdown(t):
        while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1

        print('Times up !!!')

def setupad():
    print("***************Started*********************")
    os_distribution = subprocess.check_output("grep -i ^id= /etc/os-release | sed 's/ID=//g'", shell=True, universal_newlines=True)

    if (os_distribution.strip()=='ubuntu'):
        print("You've UBUNTU OS")
        countdown(2)

        print("============================================================================================")
        print("Checking for python3 packages")
        countdown(2)
        python3_packages = subprocess.check_output("apt list --installed python3 2>/dev/null | grep installed | wc -l", shell=True, universal_newlines=True)

        if (int(python3_packages.strip()) == 0):
            print("Package python3 isn't installed, installing it now !!!")
            countdown(2)
            subprocess.check_output("grep -A 3 python3_package conf/configuration_ubuntu_setup.txt | grep -v python3_package > conf/configuration_ubuntu_setup1.txt", shell=True, universal_newlines=True)

            file1 = open('conf/configuration_ubuntu_setup1.txt', 'r')
            Lines = file1.readlines()
            file1.close()

            for line in Lines:
                a1 = "{}".format(line.strip())
                subprocess.call(""+ a1 +"", shell=True, universal_newlines=True)
            subprocess.call("rm -rf conf/configuration_ubuntu_setup1.txt", shell=True, universal_newlines=True)
			
        else:
            print("You've python3 installed")

        print("============================================================================================")
        print("Checking for Python pip packages")
        countdown(2)
        python_pip_packages = subprocess.check_output("apt list --installed python3-pip 2>/dev/null | grep installed | wc -l", shell=True, universal_newlines=True)

        if (int(python_pip_packages.strip()) == 0):
            print("Package Python_pip isn't installed, installing it now !!!")
            countdown(2)

            subprocess.check_output("grep -A 3 pip_package conf/configuration_ubuntu_setup.txt | grep -v pip_package > conf/configuration_ubuntu_setup2.txt", shell=True, universal_newlines=True)

            file1 = open('conf/configuration_ubuntu_setup2.txt', 'r')
            Lines = file1.readlines()
            file1.close()

            for line in Lines:
                a1 = "{}".format(line.strip())
                subprocess.call(""+ a1 +"", shell=True, universal_newlines=True)
            subprocess.call("rm -rf conf/configuration_ubuntu_setup2.txt", shell=True, universal_newlines=True)

        else:
            print("You've Python pip installed")

        print("============================================================================================")
        print("Checking for Django packages")
        countdown(2)
        django_packages = subprocess.check_output("python3 -m pip list 2>/dev/null | grep -i django | wc -l ", shell=True, universal_newlines=True)

        if (int(django_packages.strip()) == 0):
            print("Package Django isn't installed, installing it now !!!")
            countdown(2)

            subprocess.check_output("grep -A 2 django_package conf/configuration_ubuntu_setup.txt | grep -v django_package > conf/configuration_ubuntu_setup3.txt", shell=True, universal_newlines=True)

            file1 = open('conf/configuration_ubuntu_setup3.txt', 'r')
            Lines = file1.readlines()
            file1.close()

            for line in Lines:
                a1 = "{}".format(line.strip())
                subprocess.call(""+ a1 +"", shell=True, universal_newlines=True)
            subprocess.call("rm -rf conf/configuration_ubuntu_setup3.txt", shell=True, universal_newlines=True)

        else:
            print("You've Django installed")

        print("============================================================================================")
        print("Checking for Docker packages")
        countdown(2)
        docker_packages = subprocess.check_output("apt list --installed docker-ce 2>/dev/null | grep -i installed | wc -l", shell=True, universal_newlines=True)

        if (int(docker_packages.strip()) == 0):
            print("Package Docker isn't installed, installing it now !!!")
            countdown(2)
            subprocess.check_output("grep -A 6 docker_package conf/configuration_ubuntu_setup.txt | grep -v docker_package > conf/configuration_ubuntu_setup4.txt", shell=True, universal_newlines=True)

            file1 = open('conf/configuration_ubuntu_setup4.txt', 'r')
            Lines = file1.readlines()
            file1.close()

            for line in Lines:
                a1 = "{}".format(line.strip())
                subprocess.call(""+ a1 +"", shell=True, universal_newlines=True)
            subprocess.call("rm -rf conf/configuration_ubuntu_setup4.txt", shell=True, universal_newlines=True)

        else:
            print("You've Docker installed")

        print("============================================================================================")
        print("Checking for Docker-Compose packages")
        countdown(2)
        dc_packages = subprocess.check_output("ls -1 /usr/local/bin/docker-compose | wc -l", shell=True, universal_newlines=True)

        if (int(dc_packages.strip()) == 0):
            print("Package Docker-compose isn't installed, installing it now !!!")
            countdown(2)
            subprocess.check_output("grep -A 3 docker-compose_package conf/configuration_ubuntu_setup.txt | grep -v docker-compose_package > conf/configuration_ubuntu_setup5.txt", shell=True, universal_newlines=True)

            file1 = open('conf/configuration_ubuntu_setup5.txt', 'r')
            Lines = file1.readlines()
            file1.close()

            for line in Lines:
                a1 = "{}".format(line.strip())
                subprocess.call(""+ a1 +"", shell=True, universal_newlines=True)
            subprocess.call("rm -rf conf/configuration_ubuntu_setup5.txt", shell=True, universal_newlines=True)

        else:
            print("You've Docker-Compose installed")


    print("**************Completed the Work****************")

def startad():
    #subprocess.check_output("rm -rf logs && mkdir logs && touch logs/ad.log", shell=True, universal_newlines=True)
    subprocess.call("python3 manage.py runserver 0.0.0.0:8001", shell=True, universal_newlines=True)

def stopad():
    print ("==============================================================================")
    
    print("Checking for containers")
    a = subprocess.check_output("sudo docker ps -a | grep -v NAME | wc -l", shell=True, universal_newlines=True) 
    if (int(a.strip()) == 0):
        print("No Containers running")
    elif (int(a.strip()) != 0):
        print ("One or more containers running, killing all containers")
        countdown(2)
        subprocess.call("sudo docker ps -a | grep -v NAMES | awk {'print $1'} | xargs sudo docker rm -f", shell=True, universal_newlines=True)
    print ("==============================================================================")
    
    print("Checking for images")
    b = subprocess.check_output("sudo docker images | grep -v SIZE | wc -l", shell=True, universal_newlines=True)
    if (int(b.strip()) == 0):
         print("No images")
    elif (int(b.strip()) != 0):
        print ("Killing all images")
        countdown(2)
        subprocess.call("sudo docker images | grep -v SIZE | awk {'print $3'} | xargs sudo docker rmi -f", shell=True, universal_newlines=True)
    print ("==============================================================================")

    print("Checking for volumes")
    c = subprocess.check_output("sudo docker volume ls | grep -v NAME | wc -l", shell=True, universal_newlines=True)
    if (int(c.strip()) == 0):
         print("No Volumes")
    elif (int(c.strip()) != 0):
        print ("Killing all volumes")
        countdown(2)
        subprocess.call("sudo docker volume ls | grep -v NAME | awk {'print $2'} | xargs sudo docker volume rm", shell=True, universal_newlines=True)
    print ("==============================================================================")

    print ("Checking for networks")
    d = subprocess.check_output("sudo docker network ls | grep -v NAME | awk {'print $2'} | grep -v bridge | grep -v none | grep -v host | wc -l", shell=True, universal_newlines=True)
    if (int(d.strip()) == 0):
         print("No Networks")
    elif (int(d.strip()) != 0):
        print("Killing the networks")
        countdown(2)
        subprocess.call("sudo docker network ls | grep -v NAME | awk {'print $2'} | grep -v bridge | grep -v none | grep -v host | xargs sudo docker network rm", shell=True, universal_newlines=True)
    print ("==============================================================================")
    
    print ("Checking Program")
    e = subprocess.check_output("ps -ef | grep -v grep | egrep 'start.sh|runserver|ad.log' | awk {'print $2'} | wc -l", shell=True, universal_newlines=True)
    if (int(e.strip()) == 0):
         print("No Process running")
    elif (int(e.strip()) != 0):
        print ("Killing Program")
        countdown(2)
        subprocess.check_output("ps -ef | grep -v grep | egrep 'start.sh|runserver|ad.log' | awk {'print $2'} | xargs kill -9", shell=True, universal_newlines=True)
    print ("==============================================================================")

def statusad():
    print ("==============================================================================")
    print ("Process Status")
    #(should be 4, then program is running)
    
    a = subprocess.check_output("ps -ef | grep -v grep | egrep 'start.sh|runserver|ad.log' | wc -l", shell=True, universal_newlines=True)
    if (int(a.strip()) == 4):
        print ("AD is up & running")
    elif (a != 4):
        print ("AD is not running")

    print ("==============================================================================")
    
    b = subprocess.check_output("sudo docker ps -a | grep -v NAME | wc -l", shell=True, universal_newlines=True)
    if (int(b.strip()) == 0):
         print("No Containers running")
    elif (int(b.strip()) != 0):
        print ("CONTAINER ID of containers running")
        subprocess.call("sudo docker ps -a | grep -v NAMES | awk {'print $1'}", shell=True, universal_newlines=True)
    print ("==============================================================================")
    
    c = subprocess.check_output("sudo docker images | grep -v SIZE | wc -l", shell=True, universal_newlines=True) 
    if (int(c.strip()) == 0):
         print("No images")
    elif (int(c.strip()) != 0):
        print ("Images present in this box")
        subprocess.call("sudo docker images | grep -v SIZE | awk {'print $1\":\"$2'}", shell=True, universal_newlines=True)
    print ("==============================================================================")
    
    d = subprocess.check_output("sudo docker volume ls | grep -v NAME | wc -l", shell=True, universal_newlines=True)
    if (int(d.strip()) == 0):
         print("No Volumes")
    elif (int(d.strip()) != 0):
        print ("Volumes present in this box")
        subprocess.call("sudo docker volume ls | grep -v NAME | awk {'print $2'}", shell=True, universal_newlines=True)
    print ("==============================================================================")

    e = subprocess.check_output("sudo docker network ls | grep -v NAME | awk {'print $2'} | grep -v bridge | grep -v none | grep -v host | wc -l", shell=True, universal_newlines=True)
    if (int(e.strip()) == 0):
         print("No Networks")
    elif (int(e.strip()) != 0):
        print ("Networks present in this box")
        subprocess.call("sudo docker network ls | grep -v NAME | awk {'print $2'} | grep -v bridge | grep -v none | grep -v host", shell=True, universal_newlines=True)
    print ("==============================================================================")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-A', '--action', dest='action', help='Action you would like to do', type=str)
    args = parser.parse_args()

    action = args.action

    if (action=='setup'):
       setupad()
    elif (action=='start'):
        startad()
    elif (action=='stop'):
        stopad()
    elif (action=='status'):
        statusad()
    else:
        print("python3 automation_devops.py -A <setup|start|stop|status>")
