import os
os.system("color 2")

#     docker()  #<<<<<<<----------- call docker() to start the program  END OF THE LINE


#--------->>>>>>>>>>>>>>>>>  options <<<<<<<<<---------------------


dockerStart = 0   # <<<<----------this will tell us whether docker is started or not

def option():
    choice = input("\n\t Enter 1 to start the docker \n \t Enter 2 to stop the docker \n \t Enter 3 to know the Details of docker \n \t Enter 4 for Configuring Docker image \n \t Enter 5 for Hosting web server on docker \n \t Enter x to exit the docker \n \t\n\t\t--------->>>>>\t")
#    ch = int(choice)
    print("\n\n")
    return choice

def Rechoice():
    reChoice = input("\n\tyou have exitted from the service Enter R to re-enter and E to exit")
    if(reChoice == 'R' ):
            service()
    elif(reChoice == 'E'):
            print("\n\tyou have choosen to withdraw \n \t\tHAPPY CODING")

    else:
        print("\t\t\t !!!    EXITING !!!!!!!")
        exit()


#----------->>>>>>>>>> SERVICE() <<<<<<<<-__----------------
def service():
        exitStatus = "dumycode"
        print("\n\t \t Starting Docker \t\t\n")
        os.system("systemctl start docker")
        dockerStart = 1
        ch = 1
        while( exitStatus != "n"):
            os.system("clear")
            ch = option()
            if(ch == "1"):
                print("\n\t \t Starting Docker \t\t\n")
                os.system("systemctl start docker")
                dockerStart = 1
                print("\n\tdocker is running")
            elif(ch == "2"):
                print("\n\tstopping docker")
                os.system("systemctl stop docker")
                print("\n\tThe docker is stoped")
                dockerStart = 0
            elif(ch == "3"):
                print("\n\t\tpresenting docker Details\n")
               # os.system("systemctl status docker")
                showDockerDetails(dockerStart)
            elif(ch == "4"):

                # ==========>>>>>>> here we will ask the user details about the image it wants to run
                configDockerImage(dockerStart)
            elif(ch == "5"):
                dockerHostWebServer(dockerStart)
            elif(ch == "x"):
                print("\n\t\tYou have chosen To exit")
                exit()
                print("\n !!!! \t\tt\t\t\t\ EXITING THE SYSTEM  \t\t\tt\t !!!!")
            else:
                print("You have entered wrong choice")

#            exitStatus = input("Enter y to Return to main menu \nEnter n  to exit [y/n] \n\t------>>\t")



def configDockerImage(dockerStart):
    print("\t\t\t Welcome to docker configuration \n")
    if(dockerStart == 1):
        x = input("\n\t\tEnter 1 to run an image\n\t\tEnter 2 to pull an image\n\t\tEnter 3 to delete an image\n\t\tEnter X to exit\n\t\t----->>")
        if(x == "1"):
            print("\n\tyou have chosen option for Running Image \n")
            dockerRunImage(dockerStart)
        elif(x == "2"):
            dockerRunImage(dockerStart)
            print("\n\tyou have chosen option for Pulling Image \n")
            dockerPullImage(dockerStart)
        elif(x == "3"):
            print("\n\tyou have chosen option for deleting an Image \n")
            deleteDockerImage()
        else:
            choice = input("\n\tPress E to exit and C to continue\n")
            if(choice == "E"):
                print("\n\t\tReturning to main menu\n")
                return

    else:
        print("\n\tUnable to perofrm action , Docker is closed\n")
        print("\t \t Starting Docker \t\t\n")
        os.system("systemctl start docker")
        dockerStart = 1


# --------------------->>>>>>>>> showDockerDetails()<<<<<<<<<<<<____
def showDockerDetails(dockerStart):
    con = "Y"
    while(dockerStart != 1):
        print("\n\tUnable to perofrm action , Docker is closed\n")
        print("\n\t\t Starting Docker \t\t\n")
        os.system("systemctl start docker")
        dockerStart = 1

    while(con !="E"):
        print("\n \t\t\t Below are the option")
        os.system("docker ps --help")
        option = input("\n\n\t Enter details \t--->>\t")
        os.system("docker ps {}".format(option))
        con = input("\n\n\t\tEnter Y to return to option 3\n \t\tEnter E to go to Docker menu\n\t\t--------->>>>" )

    print("\n \t\t\t Exiting option Docker Details\n ")

# ==================>>>>>>>>Here we will ask the user details about the image it wants to pull

def dockerRunImage(dockerStart):
    if(dockerStart == 1):

        os.system("docker ps -a")

        imgPull = input("\n\nEnter the name of the image you want to run\t -------> \t")
        os.system("docker search {}".format(imgPull))
        imgChoicePull = input("\nEnter the version of the image you want to run\t ---->> \t")
        choiceDesiredName = input("\n\tDo you want to give a name to your image [y/n]\t -------->>\t")

        if(choiceDesiredName == "y"):
            print("\n\tRunning Docker image\t---->> {}".format(imgChoicePull))
            configImageName(imgChoicePull)

        else:
            print("\nENTER  -->>>  exit  <<----- to exit the image or press [ctrl+c] to exit")
            os.system("docker run -i -t {}".format(imgChoicePull))
        print("\n\t!!!!\tEXITING\t!!!!!!\n")

    else:
        print("\n\t\t The docker has stooped\n")

# --------------------->>>>>>>>>>       configImageName() <<<<<<<<<<<<<------------------------

def configImageName(imgChoicePull):
    desiredImageName = input("\n\tEnter the name \t\n \t------>  ")
    os.system("docker run -it --name {} {}".format(desiredImageName,imgChoicePull))

#-------------------------->>>>>>>>>>>>>>    deleteAllPullImage()   <<<<<<--------------------

def dockerPullImage(dockerStart):
    if(dockerStart == 1):
        imgStart = input("\n\tEnter the name of the image you want to Pull\t ------>\t")
        os.system("docker search {}".format(imgStart))
        imgChoicePull = input("\n\tEnter the version of the image you want to Pull\t ---->> \t")
        print("\n \t\t\t\t !!!! PULLING IMAGE {} !!!!\n".format(imgChoicePull))
        os.system("docker pull {}".format(imgChoicePull))
    else:
        print("\n\tThe docker has stooped")
    return



        #-------------------------->>>>>>>>>>>>>>    deleteDockerImage()   <<<<<<--------------------


def deleteDockerImage():
   # deleteImageName = ""
    chooseExit = "c"
    while(chooseExit == "c" ):
        os.system("clear")
        print("\n\tBelow are the available images\n")
        os.system("docker ps -a")
        deleteDockerImageChoice = input(" ENTER 1 to delete a single images \n ENTER 2 to delete all running images \n ENTER 3 to delete all the docker images\n ")

        if(deleteDockerImageChoice =="3"):
            deleteAllFlag = 1
            print("\n\tDeleting all docker Image\n")
            deleteAllDockerImage()

        elif(deleteDockerImageChoice == "1"):
            print("\n\tDeleting single IMAGE\n")
            deleteDockerImageChoiceFunction()

        elif(deleteDockerImageChoice == "2"):
            deleteAllRunningDockerImage()

        else:
            print("\n\t\t WRONG OPTION\n")
        chooseExit = input("\n\tENTER c to continue\n\tENTER e to exit\n")
        if(chooseExit == "e"):
            return
#  here I'm having trouble exiting the code if wrong ImageName is given

    print("\n\tYou have entered wrong option ")
    choice = input("Enter C to continue and E to exit\t------------>\t")
    if(choice != "c" and deleteAllFlag == 1):
        print("\n\tALL IMAGES ARE DELETED\n\t")
        return
    else:
        configDockerImage(dockerStart)
# ------------------>>>>>>deleteAllDockerImage()<<<_------------------
def deleteAllDockerImage():
    print("\n\tDeleting all docker Images")
    os.system("docker rm `docker ps -a -q`")

    #-------------------------->>>>>>>>>>>>>>    deleteDockerImage()   <<<<<<--------------------


def deleteDockerImageChoiceFunction():
    imageName = input("\n\tEnter the name of the image you want to remove")
    print("\n\t\t\t REMOVING {}\n".format(imageName))
    os.system("docker rm {}".format(imageName))

#-------------------------->>>>>>>>>>>>>>    deleteAllDockerImage()   <<<<<<--------------------
def deleteAllDockerImage():
    print("\n\tDeleting all docker Images")
    os.system("docker rm `docker ps -a -q`")

#-------------------------->>>>>>>>>>>>>>    deleteAllRunningDockerImage()   <<<<<<--------------------

def deleteAllRunningDockerImage():
    print("\n\tDeleting all running images")
    os.system("docker rm `docker ps -q`")

#-------------------------->>>>>>>>>>>>>>    dockerHostWebServer()   <<<<<<--------------------

def dockerHostWebServer(dockerStart):
    print("\n\tYou have chosen option 5")
    if(dockerStart == 1):
        print("\n\tHosting Web Server")
        os.system("docker pull httpd")
        os.system("docker run httpd")
        print("\n\t\t you have successfully started the web server")

    else:
        print("\n\tUnable to perform action Docker is shut")



#-------------------------->>>>>>>>>>>>>>    docker()   <<<<<<--------------------

def docker():
    os.system("clear")
    print("\n\t Welcome to dockers below are the list of options to use docker \t!!")

    service()
    Rechoice()

# ---------------->>>>>>>>>>>>>>>>>>   Here only by calling docker function the whole program will run


docker()  #<<<<<<<----------- call docker() to start the program
