import os
os.system("color 2")

  #          <<<<<<<----------- call docker() to start the program


#--------->>>>>>>>>>>>>>>>>  options <<<<<<<<<---------------------


dockerStart = 0   # <<<<----------this will tell us whether docker is started or not

def option():
    choice = input(" \t Enter 1 to start the docker \n \t Enter 2 to stop the docker \n \t Enter 3 to know the Details of docker \n \t Enter 4 for COnfiguring Docker image \n \t Enter 5 for settingup Web server in a container \n \t Enter x to exit the docker \n \t\n")
#    ch = int(choice)
    return choice

def Rechoice():
    reChoice = input("you have exitted from the service Enter R to re-enter and E to exit")
    if(reChoice == 'R' ):
            service()
    elif(reChoice == 'E'):
            print("you have choosen to withdraw \n \t\tHAPPY CODING")
            
    else:
        print("\t\t\t !!!    EXITING !!!!!!!")
        exit()

#-------------->>>>>>>>>>> 
def service():
        exitStatus = "dumycode"
        print("\t \t Starting Docker \t\t\n")
        os.system("systemctl start docker")
        dockerStart = 1
        while( exitStatus != "n"):
            os.system("clear")
            ch = option()
            if(ch == "1"):
                print("\t \t Starting Docker \t\t\n")
                os.system("systemctl start docker")
                dockerStart = 1
                print("docker is running")        
            elif(ch == "2"):
                print("stopping docker")
                os.system("systemctl stop docker")
                print("The docker is stoped")
                dockerStart = 0
            elif(ch == "3"):
                print("presenting docker Details") 
               # os.system("systemctl status docker")
                showDockerDetails(dockerStart)   
            elif(ch == "4"):

                # ==========>>>>>>> here we will ask the user details about the image it wants to run
                configDockerImage(dockerStart)
            elif(ch == "5"):
                dockerHostWebServer(dockerStart)
            elif(ch == "x"):
                print("You have chosen To exit")
                exit()
            else:
                print("You have entered wrong choice")
            
            exitStatus = input("Enter y to Return to main menu \n Enter n  to exit [y/n] \t")
        print("\n !!!! \t\tt\t\t\t\ EXITING THE SYSTEM  \t\t\tt\t !!!!")
def configDockerImage(dockerStart):
    print("\t\t\t Welcome to docker configuration \n")
    if(dockerStart == 1):
        x = input("Enter 1 to run an image\nEnter 2 to pull an image\nEnter X to exit\nEnter 3 to delete an image\n")
        if(x == "1"):
            print("you have chosen option for Running Image \n")
            dockerRunImage(dockerStart)
        elif(x == "2"):
            dockerRunImage(dockerStart)
            print("you have chosen option for Pulling Image \n")
            dockerPullImage(dockerStart)
        elif(x == "3"):
            deleteDockerImage()
        else:
            choice = input("Press E to exit and C to continue")
            if(choice == "E"):
                print("\nReturning to main menu\n")
                return
    
    else:
        print("\nUnable to perofrm action , Docker is closed\n")
        print("\t \t Starting Docker \t\t\n")
        os.system("systemctl start docker")
        dockerStart = 1

#------------>>>>>>>>>>>>>>>>>>>>>>>>> showDockerDetails(dockerStart)

def showDockerDetails(dockerStart):
    con = "Y"
    if(dockerStart != "1"):
        print("\n\t\t\tAction cannot be performed Docker is stopped \n")
    else:
        while(con !="E"):
            print("\n \t\t\t Below are the option")
            os.system("docker ps --help")
            option = input("Enter details")
            os.system("docker ps {}".format(option))
            con = input("Enter E to exit  \t")
        
    input("Enter Y to return to option 3\n Enter E to go to Docker menu\n" )
    print("\n Exiting option 3\n ")
    


# ==================>>>>>>>>Here we will ask the user details about the image it wants to pull

def dockerRunImage(dockerStart):  
    if(dockerStart == 1):
        imgPull = input("Enter the name of the image you wan to run")
        print("Running Docker image {}".format(imgPull))
        os.system("docker run -i -t {}".format(imgPull)) 
    else:
        print("The docker has stooped")
           
#-------------------------->>>>>>>>>>>>>>    deleteAllPullImage()   <<<<<<--------------------

def dockerPullImage(dockerStart):        
    if(dockerStart == 1):
        imgStart = input("Enter the name of the image you wan to Pull")
        print("\n \t\t\t\t !!!! PULLING IMAGE {} !!!!\n".format(imgStart))
        os.system("docker pull {}".format(imgStart)) 
    else:
        print("The docker has stooped")


        #-------------------------->>>>>>>>>>>>>>    deleteDockerImage()   <<<<<<--------------------

        
def deleteDockerImage():
    deleteImageName = ""
    deleteDockerImageChoice = input("ENTER DS to delete a single images \n ENTER DR to delete all running images \n ENTER y to delete all the docker images\n ENTER c to continue\n ENTER e to exit\n")
    while(deleteDockerImageChoice == "y" or deleteDockerImageChoice == "c" ):
        if(deleteDockerImageChoice =="y"):
            deleteAllFlag = 1
            deleteAllDockerImage()
            break
        elif(deleteDockerImageChoice == "DS"):
            deleteDockerImage()
            break
        elif(deleteDockerImageChoice == "DR"):
            deleteAllRunningDockerImage()
            break
        else:
            print("Enter [ctrl + c] to exit the code")
            deleteImageName = input("Enter the name of image to delete\t")
            print("Removing docker Image {}".format(deleteImageName))
            os.system("docker rm {}".format(deleteImageName))
            
# 💥 here I'm having trouble exiting the code if wrong ImageName is given          
    
    print("You have entered wrong option ")
    choice = input("Enter C to continue and E to exit\t")
    if(choice != "c" and deleteAllFlag == 1):
        print("ALL IMAGES ARE DELETED")
        return
    else: 
        deleteDockerImage()
        return
def deleteAllDockerImage():
    print("Deleting all docker Images")
    os.system("docker rm `docker ps -a -q`")       
    
    #-------------------------->>>>>>>>>>>>>>    deleteDockerImage()   <<<<<<--------------------

    
def deleteDockerImage():
    imageName = input("Enter the name of the image you want to remove")
    print("\n\t\t\t REMOVING {}\n".format(imageName))
    os.system("docker rm {}".format(imageName))
    
#-------------------------->>>>>>>>>>>>>>    deleteAllDockerImage()   <<<<<<--------------------
def deleteAllDockerImage():
    print("Deleting all docker Images")
    os.system("docker rm `docker ps -a -q`")            

#-------------------------->>>>>>>>>>>>>>    deleteAllRunningDockerImage()   <<<<<<--------------------

def deleteAllRunningDockerImage():
    print("Deleting all running images")
    os.system("docker rm `docker ps -q`")

#-------------------------->>>>>>>>>>>>>>    dockerHostWebServer()   <<<<<<--------------------

def dockerHostWebServer(dockerStart):
    print("You have chosen option 5")
    if(dockerStart == 1):
        print("Hosting Web Server")
        
    else:
        print("Unable to perform action Docker is shut")
        


#-------------------------->>>>>>>>>>>>>>    docker()   <<<<<<--------------------

def docker():
    print("\t Welcome to dockers below are the list of options to use docker \t!!")
    service()
    Rechoice()
 
# ---------------->>>>>>>>>>>>>>>>>>   Here only by calling docker function the whole program will run

docker()                                #<<<<<<<----------- call docker() to start the program


