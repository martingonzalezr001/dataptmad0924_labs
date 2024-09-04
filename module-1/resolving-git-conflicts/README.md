![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Resolving Git Conflicts

## Introduction

Resolving Git conflicts and merging branches is an import skill every software/data engineer must possess because code conflicts occur on daily basis in collaborative projects. This lab will help you learn the main concepts involve in the resolution of git conflicts.

### Prerequisites

* At this point you should have created a fork in your own Git account from the bootcamp's lab repo. 

* You should also have cloned your forked repo to your computer.

If you have any doubts about the prerequisites please clarify with your instructors.

### Overview of Steps

Below is a summary of the steps you will follow in this lab:

1. Create a folder named __`your-code`__ at the same level of this `README.md` file.
2. Create a new file inside the `your-code` folder called __`about_me.md`__ in which you will include the information you shared about yourself on the first day of class.
3. Stage changes on local branch of your working repository for the next commit (i.e.: `git add .`)
4. Commit changes on local branch (i.e.: `git commit -m "<your-message>"`)
5. Check the commit history of your local branch (i.e.: `git log`)
6. If everything is ok, syncronize the local branch with remote branch (i.e.: `git push https://<github-token>@github.com/<your-github-account>/<your-github-repository>.git`)
7. Make a __pull request__ where you will need to set:
- __base repository:__ This is the repository where the changes are proposed to be merged (i.e.: `ih-datapt-mad/dataptmadxxxx_labs`)
- __base branch:__ This is the target branch where the changes should be applied (i.e.: `main`)
- __head repository:__ This is the repository where the changes originate from (i.e.: `<your-github-account>/dataptmadxxxx_labs`)
- __head branch:__ This is the branch that contains the new changes (i.e.: `resolving-git-conflicts`)
- __Pull Request Header:__ Process automation is key, and for that reason, you must be thorough when naming files, folders, branches, pull requests, etc. (i.e.: `[<lab-name>] <Name Surname>`)
- __Pull Request Comments:__ Use this section to inform us of anything you consider relevant regarding the submission. It is very important that we are aware of your thoughts at all times so we can act quickly and effectively.

**Note: The above is also the general procedure with which you submit assignments in this course. You are not likely to encounter conflicts in this course because only you will be working on your own Git repo. But in your future professional work you'll find yourself using these steps a lot.**

### Deliverables

* File `your-code/about-me.md` updated with introductions about yourself.

## Happy Coding!!!