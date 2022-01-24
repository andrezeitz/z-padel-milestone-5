# Z Padel
Z Padel is a B2C business selling padel equipment to padel tennis players. We have products from all the major padel brands so the user is able to find the correct equipment. We sell everything from rackets to cloth and have a lot of different sizes to fit everyone.

This website can not be used as a template for a business since it's a project for educational purposes.

Live website: [Z Padel](https://z-padel.herokuapp.com/)

## Table of Contents

* [UX (User Experience)](#ux-user-experience)
  * [User Stories](#user-stories)
  * [Site Owner Goals](#site-owner-goals)
* [Design](#design)
  * [Fonts](#fonts)
  * [Colors](#colors)
  * [Wireframe](#wireframe)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks and Tools](#frameworks-and-tools)
  * [Contrast Checker](#contrast-checker)
* [Features](#features)
* [Testing](#testing)
  * [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [Python](#python)
  * [Different Screen Size](#different-screen-size)
* [Issues found during site development](#issues-found-during-site-development)
* [Deployment](#deployment)
  * [Heroku](#heroku)
  * [AWS-S3](#aws-s3)
  * [Cloning](#cloning)
* [Credits](#credits)

## UX (User Experience)

### Target Audience

The target audience for this site are for people who want to be able to buy padel equipment to a good price. It's easy for shoppers to read reviews from real customers on each product to really be sure the product is good or not. The site target all kind of people, it dosen't matter if you are an experianced padel player or if you just started your journey. Everyone is welcomed.

### Business Goals

* To provide a navigable site that can entice users to shop.
* Have a secure and trustworthy payment solution
* Connect customers to our social media platforms.

### User Stories

* As a shopper
  * I can view a different kind of products so that I can select something to buy
  * I can see individual product details so that I can take a closer look on price, information, pictures and different sizes
  * I can easy see how much the current shoppingbag will cost so that I can see if I can afford everything
  * I can select size and quantity of product so that I can choose the correct size and how many I want to buy
  * I can see what I have in my shoppingbag so that I can see how much I will spend on my purchase
  * I can change the quantity of individual items in my bag so that I can easy make a change to the products before checkout
  * I can enter my credit card so that I can pay for my items
  * I can get an order confirmation after purchase is successful so that I can see so everything is correct
  * I can get a email confirmation on my purchase so that I can know that my order was completed successful
  * I can read reviews about different products so that I can decide if this product is good or bad

* As a user
  * I can register for an account so that I can have a personal account
  * I can login and out of my account so that I can access my private account
  * I can recover my password if i forget it so that I can get back in to my account
  * I can have a personalized profile so that I can see my old order history
  * I can search for different products so that I can find what I'm looking for
  * I can choose a specific category of product so that I can easily find the best product in that category
  * I can review a product so that other people can get better information about a product

### Site Owner Goals
* As a site owner
  * I can add a product so that I can update with new items
  * I can edit a product so that I can change product price, descriptions and other criteria
  * I can delete a product so that I can remove it from the store and it will no longer be able to purchase
  * I can get an order confirmation when someone is making a purchase

* I planned the project [here](https://github.com/andrezeitz/z-padel/projects/1)

## Scope

The following features are must have for this site to function, and are correlated to the user stories above. Any features that are not included are optional and can be added later.

* Secure payment method
* Secure authentication
* Search for a product
* View products in cart
* Different size options
* User sign up and login
* User profile
* User order history.
* Save user profile information
* Clear and fully responsive design
* Full admin access
* Add, edit and delete product as admin
* Review a product

## Design

### Fonts
I have chosen Lato for the headers as it is easy to read and has sufficient contrast to the main body font. Roboto for all other text.

### Colors
The site features complementary Azure, Davys Grey, Cadet Blue Crayola, white and black to create a good contrast and improve readability.

The colors chosen are:

![colorss](https://user-images.githubusercontent.com/85236391/150809793-160855e7-24e8-49a8-ba18-1850c920295b.png)

### Wireframe

#### Desktop

<img width="698" alt="WEB" src="https://user-images.githubusercontent.com/85236391/147922980-ef5683d9-9647-4777-9a3e-68ec68b2da39.png">

#### Mobile

<img width="696" alt="MOBILE" src="https://user-images.githubusercontent.com/85236391/147923016-761bbe79-8b11-4963-b383-79cc32be64f2.png">

## Technologies

### Languages
* HTML
* CSS
* Python
* JavaScript

### Frameworks and Tools
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/home)
* [Postgres](https://www.postgresql.org/)
* [Bootstrap](https://www.bootstrap.com/)
* [AWS](https://aws.amazon.com/)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/)
* [W3C HTML Validation](https://validator.w3.org/)
* [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
* [http://pep8online.com/](http://pep8online.com/)
* [Am I responsive](http://ami.responsivedesign.is/)
* [WebAim](https://webaim.org/resources/contrastchecker/)

### Contrast Checker
All colors was checked in a contrast checker and pass the test.

![contrastcheck](https://user-images.githubusercontent.com/85236391/150809931-5dcd34eb-937d-4bd4-8945-cc9ab872a7c3.png)

## Features
The website has the following features:
### Navigation bar

### Home

### Products

### Cart

### Checkout

### Checkout Success

### Account

### Footer


## Testing


### Code Validation

### HTML
The W3C Markup Validation Service was used to validate the HTML page of the project. No errors or warnings to show.

##### Home Page


### CSS
The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.



### Python
The PEP8 Online Check was used to validate all Python code. No errors or warnings to show



### Different Screen Size
The site is optimized for all screen sizes and tested with a Macbook Pro 13" and iPhone 13 Pro.
I use media queries to make everything look and feel good on mobile devices.

### Issues found during site development
1. I had a problem to get the slug-field to work properly.

##### Solution:

2. 

## Deployment

Below describes the deployment of the site on Heroku and set up process to store static files and images on AWS.

### Heroku

#### From your browser:

1. On the home screen click on create new app button
2. Enter a name for the project and select your region to the correct region
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on Heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are able to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on connect to Github button that appears
13. Click into the search box and search for the project name
14. Once located select connect
15. Then click deploy branch, this will then be shown in the box below
16. You can the click view to show the app in a browser
17. Click on Resources in your Heroku app.
18. In the add-ons field search for Heroku Postgres and press submit.

The program is set to be deployed automatically after each push from gitpod.

#### From IDE:

1. In the consolse type pip install dj_database_url and psycopg2-binary to be able to use the postgres database.
2. Add the new dj_database_url in setting.py
3. Comment out the existing sqlite3 database.
4. Login to Heroku using the command line by typing heroku login -i
5. Once logged in you will need migrate the models to the postgres database.
6. You will now need to create a new superuser to access the admin side of the site.
7. Install the gunicorn package by typing pip install gunicorn
8. Now you can create your requirements.txt file by typing pip freeze > requirements.txt
9. Create a Procfile file by typing touch Procfile

### AWS-S3

#### How to set up AWS S3:
1. Go to AWS and login to your account. If you don't have an account, create one. If you have to create an account be mindful that you will need to enter your card details, no billing will occur unless you go over the free tier limit.
2. After logging in, go to the S3 and create a bucket.
3. Make sure you name your bucket the same as you did for Heroku and choose the nearest region to your location.
4. Scroll down to the "Block Public Access" section and unchecked the "Block public access" checkbox. Confirm that you want to allow access to the bucket. Scroll down to the bottom of the page and click on "Create bucket"

#### Customizing the bucket properties:
1. Click on the Properties tab. Scroll to the end of that page and click on edit button.
2. At the top it will allow you to choose between "Enable" and "Disable" static website hosting. Choose Enable.
3. The section below will allow you to select "Host a static website", Select "Host a static website" and then scroll down to the index "Document inputs"
4. In the input field, enter the home file which is the "index.html" file and in the error field, enter "error.html".
5. Leave the redirection rules empty and click on "Save changes".

#### Generating A Bucket Policy
1. Click on the "Policy Generator" button. Select "S3 Bucket Policy" from the dropdown list.
2. You will need to set following permissions:
* Effect – Allow
* Principle - *
* Actions – GetObject, GetObjectAcl, PutObject, PutObjectAcl and DeleteObject
* Amazon Resource Name – This can be found on the previous page, under "Bucket ARN". Copy and paste it into this box
3. After these have been entered, click "Add Statemen" and "Generate Policy".
4. Copy the policy into the bucket policy editor, adding /* onto the end, the click "Save Changes".

#### Access Control List
1. While in the permissions tab, click "edit" under the "Access Control List" section.
2. Next, navigate to "Everyone (public access)" and tick the box on the left, "List" under the "Objects" heading. Tick the box that you understand the effect then click on "Save Changes".

#### Creating A Group and Policy with IAM
1. Next, search for IAM in the search bar at the top, and click on it to set up a group policy.
2. Under "Access Management", Select "User Groups" and create a new group.
3. Give the group a name (try keep it relational to the project name) and click "Create Group".
4. This will bring you to the IAM dashboard. Go to the "Access Management" section, and click on "Policies".
5. Click "Create Policy" and click on the JSON tab, and select "Import Managed Policy".
6. Search for "AmazonS3FullAccess" and select it, then Import".
7. Copy your ARN and place it in the code twice (the second time with /*).
8. Select "Next: Tags", "Next: Review", Enter a name and click on "Create Policy".

#### Attaching the Group Policy
1. Go to "User Groups", under "Access Management". Click on the your newly created group and go over to the "Permissions" tab
2. Select the "Add Permissions" button, and select "Attach Policy".
3. Search for and click on the checkbox next to the policy you have just created, then Select "Add Permissions".

#### Create User for IAM
1. Head back to the IAM dashboard, click on "Users", then "Add User".
2. Choose a name and tick the checkbox to give the user access, then select "Next: Permissions".
3. Select the group to put the user in and keep clicking the next buttons until the very end and click "Create user".
4. Click on “Download .csv” file (Keep this is a secure location as you wont be able to get these details again), as you will not have access to this page again! This file will contain information required as shown in the Heroku table above.

#### Saving Images To S3 Bucket
1. If you need to save images to your S3 bucket, you will need to do the following;
2. Go to the s3 dashboard and click on the bucket you want to save the images to.
3. Click "Create Folder", call it "media" and click the second "Create Folder" button.
4. When you are in this folder, click "Upload", then 'Add Files" or "Add Folder", then "Upload".

### Cloning
How to clone this repository.

* On GitHub go to the main page of the Repository.
* Above the list of files click the code button with the drop-down arrow.
* To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
* Open the Git Bash terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier from step 3.
* Press Enter to create your local clone.

## Credits
