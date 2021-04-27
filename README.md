# Employee Manager
Python And Data Centric Development

This is a full stack site that allows users to manage a dataset about employees. This project highlights convinient access to the data provided by other members using the application, it also suppors all CRUD operations.

## Home Page
Must have:
As a user I would like to easily and quickly check the available employees in this site

As a user I want to easily add, update and delete a employee.

## Should have:
As a user I would like to read about employee details


# Ux
## Strategy
My goal in the design was to make it as easy as possible to access information on the site while striving for a minimalist and user-friendly design.

This Application uses Bootstrap for Design purpose.

##  Scope
For users, I wanted to provide a brief overview of all employees, also create new entries if have any. This way, many other members of the community get a glimpse about information that they can analyse.

## Structure
I wanted users to be able to quickly access the data that is available, providing a email, phone, name and designation.

## Surface
The bootstrap color schema was chosen to create a modern feel.

## Technologies
1. HTML
2. CSS
3. Bootstrap
4. JS
5. Python + Flask
6. MongoDB database

##  Features
This site uses the bootstrap forms, tables for better organising the content of a page.

# 1. Create
This site allows users to add a employee with certain fields

# 2. Edit
Every employee can be updated with specific details if known with some additional information 

# 3.Delete
Users can delete a employee if it no longer exist in market

# 4. Access
Every user will be provided with complete information about employee that was shared by a single member in a community


## Testing

The user and site owner achieved the intended outcome of providing them with a showcase of common data.

## Deployment
This site is hosted using Heroku Cloud platform, deployed directly from heroku remote master branch. The deployed site will update automatically upon new commits to the master branch of heroku. In order for the site to deploy correctly on heroku, the dependencies must be added to requirements.txt file and given this command web:gunicorn filename:variable_to_run in Procfile

Check it live here: https://employee--manager.herokuapp.com/

To run locally you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/Gumparthypavankumar/Manage-Employees.git into your terminal.

Use command python server.py to run app locally a port 8000 in manage employee folder.

You can check it run at localhost:8000 if followed above procedure correctly.

## Credits
All content and code in this project site was writen by me.
