[![Build Status](https://travis-ci.org/Duncanian/Meal.svg?branch=feature)](https://travis-ci.org/Duncanian/Meal)
[![Coverage Status](https://coveralls.io/repos/github/Duncanian/Meal/badge.svg?branch=feature)](https://coveralls.io/github/Duncanian/Meal?branch=feature)

### Meal API

#### Description
This is a meal booking website that is used by users(customers) alongside with Admins (Caterers). Users should create an account and log in. After beign authenticated :- they can see the menu for a specific day, select an option out of the menu, change their meal choice, see their order history and get notifications when the menu for the day has been set. Admin (Caterer) manages meal options in the website. Admin (Caterer) should be able to setup menu for a specific day by selecting from the meal options available on the system. Admin (Caterer) should be able to see the orders made by the user Admin should be able to see amount of money made by end of day Admin (Caterer) should be able to see order history The application should be able to host more than one caterer.

### Development

Clone the repository: 

```git clone https://github.com/Duncanian/Meal.git```

Navigate to the cloned repo. 

Ensure you have the following:

```
1. python3 & a virtualenv
2. Flask
3. Postman
```

Create a virtualenv and activate it. [Refer here](https://docs.python.org/3/tutorial/venv.html)

### Dependencies
- Install the project dependencies:
> $ pip install -r requirements.txt

After setting up the above. Run:

```python api.py```

Test the endpoints registered on `api.py` on Postman/curl on the port the app is running on. 

#### Contribution
Fork the repo, create a PR to this repository's develop.
