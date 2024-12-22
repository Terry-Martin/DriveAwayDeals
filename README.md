![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Drive Away Deals

Github link to the project [Github link](https://github.com/Terry-Martin/DriveAwayDeals)

Live Link to the project website [Live link](https://drive-away-deals-4c7671184cf5.herokuapp.com/)

## User Experience (UX)

- DriveAwayDeals is admin tool for those working at a car dealership. It allows the user to view, edit, delete and create entries for Customers, Transactions and Staff.

### Key Information for the site

- Admin tool for workers at the company
- Customer details
- Transaction details
- Staff details
- How to become a registered user and sign up.
- How to manage data and link between tables
-

### User Stories

![User Stories]

As a User, I can view customer information so that i can see their history with the company.
I can check if customer is already existing in the system
I can view the customer details and their previous transaction with the company

As a New User, i can register an account
I can enter their details in a form to capture all the standard info needed
I can save this information
I can get a confirmation that i was added
I am restricted from viewing until after log in

As a User I can make changes to the Transaction and Staff tables
I can view the information
I can edit the information
I can create new information
I can delete information

## Design

## Features

The website is comprised of one app (sale) with a base.html and 13 template files:

- Index Page (Home)
- Customer pages, along with list view, details page, form page and confirm delete page
- Staff pages, along with list view, details page, form page and confirm delete page
- Transaction pages, along with list view, details page, form page and confirm delete page


From the home page, the nav bar is visible but if the user is not already logged in, they will be prompted to do so if any link is clicked.

After log in, user can acess the full site and make or view changes as nessessary


### Home Page

![Home]

- Welcomes user to the site and displays login name if already logged in. If not logged in, user is restricted from accessing any other part of the site. 

### Navigation Bar

- The navigation bar allows users and visitors to navigate around the siteno matter the device used.

### Visitors

![Visitors Nav](media/images/README/nav_visit.png)

- Home - to take the user to the Home Page
- Register - to take the user to the register/sign up page
- Login - to take an already registered user to the login page

#### Registered logged in User

![Logged in Users Nav]

- Have access to Customer, Transaction and Staff pages
- Have access to detailed view of each
- Have access to manipulate data


### Future Implementations

- Add details about Staff members
- Add details for Stock table


## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python and Django

### Frameworks

Django - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

Balsamiq - Used to create WireFrames

Github - To save and store the files for the website

Bootstrap - The framework for the website.

Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.


### Libraries & Programs Used

Font Awesome - For the icongraphy on the website.

Django Allauth

Django_crispy_forms

gunicorn

dj_database_url

psycopg2

Pip - for install python packages

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project:

#### **Create the Live Database**

PostgresSQL was used as the database

#### **Heroku app setup**

1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
2. Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).


Heroku was used to deploy the live website. The instruction to achieve this are below:

1. Log in to Heroku.
2. Find the app from this project
3. Click on deploy.
4. Find 'App connected to Github' and link to Github account.
5. Search for repository
6. Find Manual Deploy and click Deploy Branch.
7. Click on Open App at the top right of the screen to view the live site.


## Testing

Testing was ongoing throughout the entire build. I utilised Chrome developer tools while building to pinpoint and troubleshoot any issues as I went along.

### Auto test

Automatic tests we created in tests.py:
- test_customer_list_view
- test_staff_list_view
- test_transaction_list_view
- test_customer_create_view
- test_staff_create_view
- test_transaction_create_view


### W3C Validator

All codes for Project and App were tested using the [CI Python Linter](https://pep8ci.herokuapp.com/) and are valid.

## Credits

### Code Used

[Kera Cudmore README Template and Deployment Code](https://github.com/kera-cudmore/Bully-Book-Club/blob/main/README.md)

### Content

Content for the website was written by Terry Martin
Research using [w3c](https://www.w3schools.com/), [bootstrap](https://getbootstrap.com/)
Based strongly on I Think Therefore I Blog from Code Institute
