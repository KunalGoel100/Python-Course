###### **Git \[Version Control]**

**(Its like bank passbook, to keep track of our code)**

* Used to collaborate: Other people can see our work and can work along, similar to Google Docs
* **Git** is the Version control, **GitHub** is the website that uses the **Git**
* In GitHub we can make folders (Repository) to organize our work, like Google Drive
* **Commit** is like a snapshot, it will create a history (locally)



###### **File Status**

* **Untracked:** The git is not tracking the file, it shows that a new file is present
* **Modified:** The file is modified (after the git start tracking the file)
* **Staged:** The file is ready to be Commited



###### **Add and Commit**

**git add <file name>:** To stage the file (git will start tracking the file and make it ready for commit)

**git add .:** To stage all the changed files at once

**git commit -m "Some message":** to commit the file, we have to give a meaning full message (why we are commiting the changes)

**git push origin main:** To publish the commited changes to the GitHub repository (The files will go in server)



###### **Pushing our own local folder to GitHub:**

**git init:** Makes the folder a Git tracked folder

**git remote add origin <link to the GitHub folder>:** This is to link the GitHub repo to the local folder and we'll refer to it as origin. \[GitHub (website) Repository must be present]

**git remote -v:** To verify the link is properly set or not

**git branch:** To see on which branch we are currently working

**git branch -M main:** To change the branch name (default Master) to "Main"



###### **Branch Commands**

**git branch:** to check which branch we are currently working

**git branch -M <New branch name>:** to rename the branch

**git checkout <branch name>:** to shift to some other branch

**git checkout -b <newbranch name>:** to create a new branch

**git branch -d <branch name>:** to delete a branch (we cant delete the current branch we are working on)



###### **Merging Branch**

**git diff <branch name>:** to compare the changes in files in diff branches

**git merge <branch name>:** to merge 2 branches



###### **Undoing Changes**

* **Staged Changes**

**git reset <file name>:** revert the added/staged status of a particular file

**git reset:** revert the added/staged status of all file



* **Commited Changes**

**git reset HEAD~1:** revert the commited changes by one commit

**git reset <commit hash>:** revert to the commit whose hash is mentioned

**git reset --hard <commit hash>:** to actually change the local files

**git log:** to see all the commits and their hash













































 



###### 

