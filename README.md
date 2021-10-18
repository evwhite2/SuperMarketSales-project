# Project Rebric

The group project is an important course component in which students use the Python programming language to manipulate and analyze data to support business decision making. Each of the groups will be responsible for selecting their topic and identifying relevant data to use, and having that topic approved by the instructor.  

Each completed project should include the following components: 

1. The project must utilize a set of stored data in order to obtain information used in business decision making. 
     This stored data ideally is obtained via the World Wide Web, but can also be in files and/or in an Access database.  
     The data set(s) for the project must not be the Taxi Trips or GSS data sets used in our textbook.  
     Each observation (row) in the data should pertain to a unique object of interest and have multiple attributes (columns) that pertain to the object.
     As you are identifying and/or creating this data set, it is particularly important to identify a dependent variable (or variables), that is a specific attribute (or attributes) that you would like to predict based on the values of the remaining attributes. 
     You should have at least 3 numerical values (think of values that result from measuring or counting something) 
     and at least 3 categorical variables (think of yes/no situations and values that are not numbers).  
     Note that the numerical attributes will later be used to explain the dependent variable that you identified.  For example, if you had salaries of basketball players as the dependent variable, numerical variables could include the player’s height in inches, average rebounds per game and average points scored per game.  Categorical variables could include team, if the player has been an all-star (yes/no), and player position (i.e. guard).  
     Your data set needs to have at the very minimum 50 observations, but ideally has hundreds or thousands (or more). 

2. Statistical calculations used to summarize the data for the business decision being supported.  These calculations can be constructed using formulas and functions and ideally utilize Python packages.

3. The use of data visualization for analyzing your data using the matplotlib and/or the seaborn Python packages.

4. The use of Machine Learning to develop a model using either supervised or unsupervised learning with your data.  

5. A user interface to enable the user to specify (type in) variations and/or restrictions affecting the supported decision.  Some examples include using different time periods, different products, or different objectives.   

6. Help/guidance for the user, particularly to ensure proper input values, but also to provide explanations to the user when needed. 

7. Validation of user inputs that prevents incomplete, inaccurate or unrealistic entries by the user.  


Each group will present their project to the class on 11/1/2021.  
The graded components of the project will be the completed project (70%), a group presentation to the class (20%) and a peer evaluation (10%).  
Due Date Item Due 9/27/21 Brief description of your group's project and description of data to be used 11/1/21 Complete Project and In-Class Presentation 


# Proposal 
### Group 3: 
Dawood Ahmed, Ellen White, Krista Galvin, Sean Daley
Brief description of your group's project and description of data to be used

##### Data set source
Kaggle.com

##### Description
Historical sales data over 3 month period in 2019 from a supermarket company from 3 different branches. 

##### Attribute Information
Invoice id: Computer generated sales slip invoice identification number
Branch: Branch of supercenter (3 branches are available identified by A, B and C).
City: Location of supercenters

Customer type: “Members” for customers using member card and “Normal” for without member card.

Gender: Gender type of customer

Product line: Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel

Unit price: Price of each product in $

Quantity: Number of products purchased by customer

Tax: 5% tax fee for customer buying

Total: Total price including tax

Date: Date of purchase (January 2019 to March 2019)

Time: Purchase time (10am to 9pm)

Payment: Cash, Credit card and Ewallet

COGS: Cost of goods sold

Gross margin percentage: Gross margin percentage

Gross income: Gross income

Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)

#### Research questions:
1.	Avg purchase price for each city- does the size of a city affect the amount purchased?

2.	Payment method- do customers buy more when using cc, cash, etc.?

3.	What is the most popular category?  Are people more likely to use a cc to buy electronics, for example.

4.	Avg. Product price in a particular category

5.	Total cost of goods sold

6.	Avg. Customer satisfaction as per rating (per store)

7.	Time frame when the stores are most busy

8.	Are most of the customers satisfied overall?

9.	If most customer are male or female and members or non-members?

10.	Does customer gender influence what product categories the customer buys?


##### Required Packages

pandas
matplotlib
statsmodels
sklearn
