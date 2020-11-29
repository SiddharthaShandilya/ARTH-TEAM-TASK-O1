
class Docker_automation():
    def __init__(self):

        print("\n\t!!!\t--->>\t WELCOME TO DOCKER AUTOMATION \t <<---\n")

    def option(self):
        choice = input("\n\t Enter 1 to start the docker \n \t Enter 2 to stop the docker \n \t Enter 3 to know the Details of docker \n \t Enter 4 for Configuring Docker image \n \t Enter 5 for Hosting web server on docker \n \t Enter x to exit the docker \n \t\n\t\t--------->>>>>\t")
        #    ch = int(choice)
        print("\n\n")
        return choice

    def Rechoice(self):
        reChoice = input(
            "\n\tyou have exitted from the service Enter R to re-enter and E to exit")
        if(reChoice == 'R'):
            service()
        elif(reChoice == 'E'):

            print("\n\tyou have choosen to withdraw \n \t\tHAPPY CODING")

        else:

            print("\t\t\t !!!    EXITING !!!!!!!")
            exit()

    def __dockerHostWebServer__(self):
        print("\n\tYou have chosen option 5\n")
        osName = input("\n\tEnter the name of the os \t --->  ")

        os.system("docker start {}".format(osName))
        os.system("docker ps --latest")
        print("\n \n")
    #    print("\n\t\t -->>Enter [ctrl+d] to exit the command line<<---\n")
      #  os.system()
        print("\n The ip of the os is \t --->\t ")
        var = os.system(
            "docker container inspect --format \"{{.NetworkSettings.IPAddress}}\" {}".format(osName))
        os.system("docker exec -it {} yum install httpd".format(osName))
     #   print("\n\t\twrite the codes for the server to deploy\n")
      #  os.system("")
        webFileName = input(
            "\n\tEnter the name of the html file that needs to be launched\t--->\t")
        os.system("docker cp {} {}:/var/www/html".format(webFileName, osName))
        print("\n\t\t--->>>   LAUNCHING {} FILE ON  WEB SERVER on {}  <<<-----\t\n".format(webFileName, osName))
        os.system("docker exec -it {} /usr/bin/httpd".format(osName))

# ----------------------->> SERVICES <<----------------

    def service(self):
        exitStatus = "dumycode"
        print("\n\t \t Starting Docker \t\t\n")
        os.system("systemctl start docker")
        dockerStart = 1
        ch = 1
        while(exitStatus != "n"):
            os.system("clear")
            ch = self.option()
            if(ch == "1"):
                print("\n\t \t Starting Docker \t\t\n")
                os.system("sleep 3")
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
                self.showDockerDetails(dockerStart)
            elif(ch == "4"):

                # ==========>>>>>>> here we will ask the user details about the image it wants to run
                self.configDockerImage(dockerStart)
            elif(ch == "5"):
                self.dockerHostWebServer()
            elif(ch == "x"):
                print("\n\t\tYou have chosen To exit")

                print("\n !!!! \t\tt\t\t\t\ EXITING THE SYSTEM  \t\t\tt\t !!!!")
                break
            else:
                print("You have entered wrong choice")

#            exitStatus = input("Enter y to Return to main menu \nEnter n  to exit [y/n] \n\t------>>\t")
    def configDockerImage(self, dockerStart):
        print("\t\t\t Welcome to docker configuration \n")
        if(dockerStart == 1):
            x = input(
                "\n\t\tEnter 1 to run an image\n\t\tEnter 2 to pull an image\n\t\tEnter 3 to delete an image\n\t\tEnter X to exit\n\t\t----->>")
            if(x == "1"):
                print("\n\tyou have chosen option for Running Image \n")
                self.dockerRunImage(dockerStart)
            elif(x == "2"):
                self.dockerRunImage(dockerStart)
                print("\n\tyou have chosen option for Pulling Image \n")
                self.dockerPullImage(dockerStart)
            elif(x == "3"):
                print("\n\tyou have chosen option for deleting an Image \n")
                self.deleteDockerImage()
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

    def showDockerDetails(self, dockerStart):
        con = "Y"
        while(dockerStart != 1):
            print("\n\tUnable to perofrm action , Docker is closed\n")
            print("\n\t\t Starting Docker \t\t\n")
            os.system("systemctl start docker")
            dockerStart = 1

        while(con != "E"):
            print("\n \t\t\t Below are the option")
            os.system("docker ps --help")
            option = input("\n\n\t Enter details \t--->>\t")
            os.system("docker ps {}".format(option))
            con = input(
                "\n\n\t\tEnter Y to return to option 3\n \t\tEnter E to go to Docker menu\n\t\t--------->>>>")

        print("\n \t\t\t Exiting option Docker Details\n ")

    def __dockerRunImage__(self, dockerStart):
        if(dockerStart == 1):

            os.system("docker ps -a")

            imgPull = input(
                "\n\nEnter the name of the image you want to run\t -------> \t")
            os.system("docker search {}".format(imgPull))
            imgChoicePull = input(
                "\nEnter the version of the image you want to run\t ---->> \t")
            choiceDesiredName = input(
                "\n\tDo you want to give a name to your image [y/n]\t -------->>\t")

            if(choiceDesiredName == "y"):
                print("\n\tRunning Docker image\t---->> {}".format(imgChoicePull))
                self.configImageName(imgChoicePull)

            else:
                print(
                    "\nENTER  -->>>  exit  <<----- to exit the image or press [ctrl+c] to exit")
                os.system("docker run -i -t {}".format(imgChoicePull))
                print("\n\t!!!!\tEXITING\t!!!!!!\n")

        else:
            print("\n\t\t The docker has stooped\n")

    def __configImageName__(self, imgChoicePull):
        desiredImageName = input("\n\tEnter the name \t\n \t------>  ")
        os.system(
            "docker run -it --name {} {}".format(desiredImageName, imgChoicePull))

    def __dockerPullImage__(self, dockerStart):
        if(dockerStart == 1):
            imgStart = input(
                "\n\tEnter the name of the image you want to Pull\t ------>\t")
            os.system("docker search {}".format(imgStart))
            imgChoicePull = input(
                "\n\tEnter the version of the image you want to Pull\t ---->> \t")
            print("\n \t\t\t\t !!!! PULLING IMAGE {} !!!!\n".format(imgChoicePull))
            os.system("docker pull {}".format(imgChoicePull))
        else:
            print("\n\tThe docker has stooped")
        return

    def __deleteDockerImage__(self):
       # deleteImageName = ""
        chooseExit = "c"
        while(chooseExit == "c"):
            os.system("clear")
            print("\n\tBelow are the available images\n")
            os.system("docker ps -a")
            deleteDockerImageChoice = input(
                " ENTER 1 to delete a single images \n ENTER 2 to delete all running images \n ENTER 3 to delete all the docker images\n ")

            if(deleteDockerImageChoice == "3"):
                deleteAllFlag = 1
                print("\n\tDeleting all docker Image\n")
                self.deleteAllDockerImage()

            elif(deleteDockerImageChoice == "1"):
                print("\n\tDeleting single IMAGE\n")
                self.deleteDockerImageChoiceFunction()

            elif(deleteDockerImageChoice == "2"):
                self.deleteAllRunningDockerImage()

            else:

                print("\n\t\t WRONG OPTION\n")
                chooseExit = input(
                    "\n\tENTER c to continue\n\tENTER e to exit\n")
                if(chooseExit == "e"):
                    return
# 💥 here I'm having trouble exiting the code if wrong ImageName is given

        print("\n\tYou have entered wrong option ")
        choice = input("Enter C to continue and E to exit\t------------>\t")
        if(choice != "c" and deleteAllFlag == 1):
            print("\n\tALL IMAGES ARE DELETED\n\t")
            return
        else:
            self.configDockerImage(self.dockerStart)

    def __deleteAllDockerImage__(self):
        print("\n\tDeleting all docker Images")
        os.system("docker rm `docker ps -a -q`")

    # -------------------------->>>>>>>>>>>>>>    deleteDockerImage()   <<<<<<--------------------

    def __deleteDockerImageChoiceFunction__(self):
        imageName = input("\n\tEnter the name of the image you want to remove")
        print("\n\t\t\t REMOVING {}\n".format(imageName))
        os.system("docker rm {}".format(imageName))

# -------------------------->>>>>>>>>>>>>>    deleteAllDockerImage()   <<<<<<--------------------
    def __deleteAllDockerImage__(self):
        print("\n\tDeleting all docker Images")
        os.system("docker rm `docker ps -a -q`")

# -------------------------->>>>>>>>>>>>>>    deleteAllRunningDockerImage()   <<<<<<--------------------

    def __deleteAllRunningDockerImage__(self):
        print("\n\tDeleting all running images")
        os.system("docker rm `docker ps -q`")

    def docker(self):

        os.system("clear")
        print("\n\t Welcome to dockers below are the list of options to use docker \t!!")
        self.service()
        self.Rechoice()
