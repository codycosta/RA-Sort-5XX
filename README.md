# 5XX RA Sort Python script

## !! Please read if you are new to using python or need assistance with setting up your machine !!

### Setup should not take more than 20 minutes and is a one time deal, after that there's no other prerequisites to begin use

<br>

## TLDR (or you're already a pro)
### Usage:
Navigate to a folder where you have some RA files located:
> cd ~/Documents/5XX/52XX/SV_RA

Run RA-sort.py:
> ~/Documents/5XX/52XX/SV_RA >> python [path to RA-sort.py]

<hr>
<br>
<br>

# Priming Your Machine For Python
## Step 1: Make sure you have python installed (version 3.7 or later)
Python can be downloaded from https://www.python.org/. I would recommend installing the latest version if you are unsure.\
To check if your machine already has a version of python installed, simply press the windows key and search for 'python':\
![image](readme-imgs/check-python.png)\
<br>
<br>
If you do not see a version installed, follow the instructions on Python's website linked above for a fresh install. After downloading, be sure to run the .exe file to install it.

<br>

## Step 2: Adding Python to your system path
This step will take the most work, but is not difficult to do.\
First, keep your path to python handy, we will need it later.\
<br>

You can find this located at: 
### C:\Users\USER\AppData\Local\Programs\Python\Python312\
Just enter your USER name and substitute Python312 with whichever version you downloaded.\
Python 3.13 is the latest release at the time of development.\
<br>

Next, press the windows key and type out 'env', and click on **Edit the system environment variables**
![image](readme-imgs/sys-env.png)\
<br>
<br>

A new 'System Properties' window will open, and we want to click on **Environment Variables**\
![image](readme-imgs/sys-props.png)\
<br>
<br>

This will bring up a new window called 'Environment Variables'\
Navigate to the **system variables** section and click on the item labeled Path and then click **Edit**
![image](readme-imgs/env-vars.png)\
<br>
<br>

Another new window will pop up, and we will then click on **New**\
In the field that pops up, here is where you will paste in your PYTHON PATH from earlier\
You can see mine listed at the bottom\
![image](readme-imgs/edit-vars.png)\
<br>

#### Go ahead and click on **OK** on all the open windows to close them, and you are done with path setup!

<br>

## Step 3:  Diasabling Execution Aliasing
This part is easier than step 2.\
Press the windows key and search for 'app exec', and click on **Manage app execution aliases**
![image](readme-imgs/execution.png)\
<br>
<br>

Scroll down until you see 2 programs named **App Installer** with python.exe and python3.exe listed below the titles.\
Turn both of these **OFF**
![image](readme-imgs/alias-off.png)\
<br>
<br>
