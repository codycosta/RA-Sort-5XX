# 5XX RA Sort Python script

### Turn a cluttered directory into a well organized file storage, ready for excel!

>[!NOTE]
>Please read if you are new to using python or need assistance with setting up your machine
>Setup should not take more than 20 minutes and is a one time deal, after that there's no other prerequisites to begin use. I've tried to make this guide as easy and beginner friendly as possible.

<br>
<br>

# Usage

### Step 1: Navigate to RA folder
For example let's say we have some RA's that exist in the following folder:

```powershell
cd ~/Documents/5XX/SV_RA
```
<br>

### Step 2: Run RA-sort.py
To do this, run the following command below. You can use either **python** or **py** prefixes to reference the python file. Let's say we downloaded and moved RA-sort.py to the following folder:

```powershell
~/Documents/5XX/RA-sort.py
```

>[!TIP]
>After downloading RA-sort.py from github here, I'd recommend keeping it (or a copy) close to, or even inside, the RA directory you intend to sort. This way, typing out the file path is not a hassle.
<br>

Your command line execution would look something like this:
```powershell
~/Documents/5XX/SV_RA>      python [path to RA-sort.py]



or with the example file/folder names:

~/Documents/5XX/SV_RA>      python ../RA-sort.py
```
<br>

## Optional
### Step 3: Organize excel along with RA's

You can also elect to have the script copy and organize your excel workbooks along with the RA files.\
To do this, after calling RA-sort.py, add an extra argument that references the path to the blank workbook folder.\
Say we have our blank workbooks in the following folder:

```powershell
~/Documents/5XX/blank-workbooks/
```

To reference this folder while sorting so the excel workbooks can be copied and organized too, we would run the following:

```powershell
~/Documents/5XX/SV_RA >     py [path to RA-sort.py] [path to blank workbooks]



or with the example file/folder names:

~/Documents/5XX/SV_RA>      python ../RA-sort.py ../blank-workbooks
```

>[!IMPORTANT]
>If you would like to do this, make sure that each of your blank excel workbooks at least has 'COG', 'EPSM', 'CETUS' and 'SL' in the name.
>[!TIP]
> Like with the RA-sort.py script, I recommend keeping your folder of blank excel workbooks nearby to easily access
<br>

When organizing the excel workbooks, RA-sort.py will count the number of RA P0 files in each folder and will duplicate the needed excel workbook should the quantity of unique RA files exceed 10. This way there are the required number of excel files within each base/threshold folder.

## Example
In the below photos you can see I have some RA files stored in:
```powershell
~/KLA-RA-scripts/sample-RAs/
```
<br>

and my copy of RA-sort.py stored in the previous folder:
```powershell
~/KLA-RA-scripts/RA-sort.py
```
<br>

Keeping RA-sort.py close to the RA folder makes execution easy.\
I just need to navigate to my RA folder (samlple-RAs) and call on RA-sort.py which is in the previous folder:\
<br>

When running, you can use the **python** or **py** prefix command\
![image](etc/readme-imgs/cmd.png)
<br>
<br>

### Before
![image](etc/readme-imgs/cluttered-folder.png)
<br>
<br>

### After
![image](etc/readme-imgs/cleaned-2.png)
<br>
<br>
<br>

# How To Download RA-sort.py
At the top of the page if you are reading this, click on RA-sort.py\
![image](etc/readme-imgs/file.png)
<br>

Next, on the top right of the file page, click the button to download raw file\
![image](etc/readme-imgs/download.png)
<br>

### That's it, your file will be in your downloads folder
<br>
<br>

# Priming Your Machine For Python
## Step 1: Make sure you have python installed (version 3.7 or later)
Python can be downloaded from https://www.python.org/. I would recommend installing the latest version if you are unsure.\
To check if your machine already has a version of python installed, simply press the windows key and search for 'python':\
![image](etc/readme-imgs/check-python.png)
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
![image](etc/readme-imgs/sys-env.png)
<br>
<br>

A new 'System Properties' window will open, and we want to click on **Environment Variables**\
![image](etc/readme-imgs/sys-props.png)
<br>
<br>

This will bring up a new window called 'Environment Variables'\
Navigate to the **system variables** section and click on the item labeled Path and then click **Edit**
![image](etc/readme-imgs/env-vars.png)
<br>
<br>

Another new window will pop up, and we will then click on **New**\
In the field that pops up, here is where you will paste in your PYTHON PATH from earlier\
You can see mine listed at the bottom\
![image](etc/readme-imgs/edit-vars.png)
<br>

#### Go ahead and click on **OK** on all the open windows to close them, and you are done with path setup!

<br>

## Step 3:  Diasabling Execution Aliasing
This part is easier than step 2.\
Press the windows key and search for 'app exec', and click on **Manage app execution aliases**
![image](etc/readme-imgs/execution.png)
<br>
<br>

Scroll down until you see 2 programs named **App Installer** with python.exe and python3.exe listed below the titles.\
Turn both of these **OFF**\
![image](etc/readme-imgs/alias-off.png)
<br>
<br>


### Setup is finished, your computer is ready to run Python
### Navigate back to the top to read about the file Usage
