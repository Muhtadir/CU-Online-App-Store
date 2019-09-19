<--"CU ONLINE APP STORE" ENVIRONMENT SETUP AND RUNNING GUIDE FOR WINDOWNS, LINUX AND MACOS BASED SYSTEMS-->

1. Copy the project folder "CU_Online_App_Store" from this CD's root directory and paste it into any location of your computer.

2. To run the Django web server, you must have Python Anaconda Distribution(i.e. python version 3.7 atleast) installed inside your computer.

	<--Python 3.7 version i.e. Anaconda Distribution installation Guide-->
	
	a. Go to google and search typing "Download Anaconda" or follow this link "https://www.anaconda.com/distribution/" to download Anaconda Distribution i.e. Python 3.7 version.
	b. Select your operating system from the download page and install the distribution(Python 3.7 version) into your computer.
	(You must follow the installation guideline of Anaconda for different Operating systems from the download page.)
	c. Find/Search the program "Anaconda Prompt" from your computer and then open it. 
	d. Run the command "conda info" from Anaconda Prompt.	
	e. If you are having trouble in finding the "Anaconda Prompt" into your computer, then install Python properly again.
	
3. Now, you need to create a virtual environment to configure or work with the web project "CU_Online_App_Store".
	
	<--Virtual Environment Creation-->
	Run the following command from "Anaconda Prompt" :		
	conda create --name myEnv django
	
	Your virtual environment "myEnv" is created!
	
4. STARTING THE PROJECT WITH THE SERVER: 
   First you need to activate the virtual environment you have created previously in step 3.
   Then you need to run the project from the pasted project location of your computer in Anaconda Prompt.
   
	<--Activation of Virtual Environment-->
    Open "Anaconda Prompt" and run the following command:	
	activate myEnv	
	or, source activate myEnv
	
	<--Run the server-->
	While environment is activated, don't close the Anaconda Prompt. On Anaconda Prompt, change your current working directory into the project directory and run the following command:
	
	python manage.py runserver
	
	Django Web Server is now running!
	

5. RUN/USE: 
	a. Open your browser
	b. Go to the url: "http://127.0.0.1:8000/"
	c. Enjoy!
	
6. CU ONLINE APP STORE USER GUIDE:
	a. Open the video "CU_Online_App_Store.mp4" from this CD's root directory.
	b. Watch the video till end for seeing various features of this web application.

7. REUSE/EDIT THE PRIJECT FOR FUTURE USE:
	If you want to reuse the project, you can install any popular web project editor like "Atom" or "Pycharm" etc to open the project folder and edit.
	Then you can run and test the edited project.
	
Note: In every run, you will need to activate the virtual environment i.e. you will need to follow the step 4 in each run.