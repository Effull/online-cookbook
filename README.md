# online-cookbook
This is my third mastering Project where I will be in using a mixture of HTML CSS JavaScript python and flask to create an online cookbook


Title

Title - is an open online cookbook which can be used to find recipes or share your own for breakfast, lunch & dinner style meals with an online community with a simple user interface.
 
The ways that the site can be useful

1.	Getting inspiration and recipes for meals for breakfast and lunch.
2.	Upload recipes of your own and get feedback.

img

-maybe
Table of Contents
1.	UX
o	Goals
	User Goals
o	User Stories
o	Wireframes
o	Color Scheme
2.	Features
o	Existing Features
	Home page
	Page for registering a name and an event key
	Page for registering details of the event
	Page for getting a shareable link
	Page for participants
	Page for restoring an existing plan
o	Features Left to Implement
	Delete the data after the event date is passed
o	Defensive Design
3.	Information Architecture
4.	Technologies Used
5.	Testing
o	Manual Testing
o	Bugs
6.	Deployment
o	Local Deployment
o	Heroku Deployment
7.	Credits
UX
Goals
The goal of this project is to create a website to upload, view and comment cooking recipes with different levels of complexity for users with ease.
User Goals
The target audience for this website is:
•	An audience interested in cooking and want to share comment, and get inspired by user uploaded recipes.
The user goal is to have:
•	A website for users to access and upload food.
•	Provide feedback or receive feedback on recipes that they have used or they have uploaded.
User Stories
A user of the site,
•	I would like to have a simple and functional interface to allow users to easily find an add recipes to the website.
•	I would like to view recipes updated by users
•	I would like to upload recipes to the website.
•	I would like to read comments on recipes from other users
•	I would like to be able to comment on recipes
A constant user of the site,
•	I would like to be able to easily filter recipes for different breakfast lunch and dinner Style meals with ease.
•	I would like a scale to see the complexities of the recipes.
•	?.
Wireframes
Wireframes were created with balsamiq.
•	Homepage
•	Create plan page
•	Update participant page
Color Scheme
•	For colour schemes and use the template from Heroic Features on start Bootstrap to take advantage of flask templating with slight modifications but with the same colour scheme with a white background and dark blue footers and title blocks
•	As the illustrations used on main pages had some modern aesthetics of colors, as well as it's important to limit the total numbers of primary colors, I decided to use similar colors to the illustrations as the primary colors for this site.
1.	 rgba(255, 255, 255, 0.75) title & footer.
2.	  #fff text
Features
Existing Features
Home page
•	This page is designed to show a variety of meals to get people inspired and interested into different meals/recipes.
Breakfast
•	Users can go to this page is to see all of the breakfast style meals.
Lunch
•	Users can go to this page is to see all of the Lunch style meals.
Dinner
•	Users can go to this page is to see all of the Dinner style meals.
Upload recipe
•	This page allows recipes to be uploaded by users.
Contact page
•	This is where users can contact the site owners about the site.

Features Left to Implement
Delete the data after the event date is passed
•	A revision section on all of the recipe pages where users who uploaded those recipes can update details they have changed about the recipe and why.
Defensive Design
•	-.
Information Architecture
MongoDB Atlas is used for storing data for this web site.
The following is the data structure.
{
    _id : ObjectId()
    organizer_name : String,
    event_key : String,
    availabilities : Array,
    event_description : String,
    event_name : String,
    event_place : String,
    participants : Array
                   { 
        name: String,
        availabilities: Array,
        participant_note: String
     }
}

Technologies Used
the sites design was taken from a temper on start bootstrap using Flask to overlay over the pages to have a basic template set up very quickly with large amount of HTML and CSS already completed. This application contains key CRUD functionalities and they are used to maximize user's experience in this site. The main technologies used are HTML, CSS, JavaScript and bootstrap for front end and Python and Flask for the back end.
Languages
•	HTML, CSS, JavaScript, Python
Libraries
•	Bootstrap (v4.4.1)
•	JQuery
•	JQuery-UI
•	Popper.js
•	Font Awesome
•	Flask
•	Jinja
•	PyMongo
Tools
•	Git/GitHub
•	Gitpod
•	Heroku
•	PIP3
•	MongoDB Atlas
Testing
Validation Tools
I used these validation tools below for each file.
•	HTML: W3C HTML Validator
•	CSS: W3C CSS validator
•	JavaScript: JSHint
•	Python: PEP8 online
Formatter
•	HTML: HTML Formatter
•	CSS: CSS Formatter
•	JavaScript: Online JavaScript Beautifier
•	Python:PEP8 online
Manual Testing
Testing was done throughout the application being built. This application is built with a mobile first responsive design in mind. I created this testing matrix to make sure the site works as expected in different devices with the emuration funtion in Google Developer Tool, browsers and screen sizes.
Bugs
Python and Database
•	In the page for creating a new event(create_new_plan.html), if users added many empty availabilities forms at the same time and remove the forms randomly, the date was not correctly updated in the MongoDB collection. It was caused by the try/except method which I used in order to check if a key for availabilities exists in the request.form MultiDict object. After I replaced the try/except method with if/else statement, this bug was fixed.
JavaScript
•	In the page for registering participants(update_plan_participants.html), if a participant uses a whitespace in their name, it caused a rendering issue after clicking 'Edit' button. It was caused by whitespaces surrounding the selected name which was created by text() function in JavaScript used to get the text for the name from the HTML. This bug was fixed by using the trim() function, which deletes all whitespaces before and after the selected text(in this case, the selected name).
Browser Compatibility
•	Safari: The css styling for a delete button in the Modal window in restored_data.html was not working in Safari. It was caused by type="button" in the anchor tag that works as the delete button, and after deleting type="button" it started working as expected.
Deployment
Local Deployment
For local deployment, you need to have an IDE such as Gitpod and you need to install the following in your IDE:
•	Git, Python3, PIP3
1.	At the top of this repository, click the green button Clone or download.
2.	In the Clone with HTTPs section, copy the clone URL for the repository.
3.	Open your favourite terminal (cmd, powershell, bash, git bash, etc.)
4.	Change the current working directory to the location where you want the cloned directory to be made.
5.	Type git clone, and then paste the URL you copied in Step 2: git clone https://github.com/AsunaMasuda/MilestoneProject3.git
6.	Press Enter. Your local clone will be created.
7.	You can either
o	Create a virtual environment and create environment variables of IP, PORT, MONGO_URI and SECRET_KEY.
Or edit the app.py file like the following variables:
'IP', '127.0.0.1'

'PORT', '5000'

'SECRET_KEY', '<somethingsecret>'

'MONGO_URI', 'mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority'
o	
9.	Install all required modules from requirements.txt with the commandpip3 install -r requirements.txt
10.	Now you can run the website with the command python3 app.py
11.	You can now access the website at http://127.0.0.1:5000
Heroku Deployment
This website is deployed on Heroku, following these steps:
1.	Create a requirements.txt file using the command pip3 freeze > requirements.txt in the terminal.
2.	Create a Procfile using the commant echo web: python app.py > Procfile in the terminal.
3.	Commit and push all the changes to the Github repositoty of this project.
4.	Go to Heroku and create a new app. Set a name for this app and select the closest region.
5.	Choose Deployment method as GitHub in Heroku Dashboard and link the Github repository to the Heroku app.
6.	Go to Settings then Reveal Config Vars in Heroku Dashboard and set the values as follows:
Key	Value
IP	0.0.0.0
PORT	5000
MONGO_URI	mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
SECRET_KEY	<your_secret_key>
Credits
Content
•	All text within this project was written by the developer.
Media
Icons
•	All the icons in this website were provided by Font Awesome.
Images
•	The images used in the home page are created by pikisuperstar - www.freepik.com.
•	The favicon for this site is provided by flaticon
UX
•	I used this article as reference when deciding the color scheme. 7 Tips To Organize Colors for UI Design
JavaScript
•	The datetime picker is powered by flatpickr.
Acknowledgements
•	Thanks to: my Code Institute Mentor Guido Cecilio Garcia Bernal for his advice throughout the development process.
•	Code Institute Slack Community that gave me a light when I was stuck in my coding.

