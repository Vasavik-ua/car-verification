# Car Verification
> This site is designed to help manage car check-up information for companies while also providing detailed insights for users.

This project models a comprehensive system to manage vehicle data, ownership details, and maintenance records. The relationships between the entities are carefully designed to ensure seamless interaction between cars, their owners, the companies performing check-ups, and the check-up data itself.


### Initial Configuration

To perform the check of functionality use this user:
Username: User
Password: User12345

## Developing

Ensure you have Python and Django installed on your system.

```shell
git clone https://github.com/Vasavik-ua/car-verification.git
cd car-verification/
pip install -r requirements.txt
```


### Building

If you make any migrations or changes to models, run:

```shell
python manage.py makemigrations
python manage.py migrate
```

### Deploying / Publishing

In case there's some step you have to take that publishes this project to a
server, this is the right time to state it.

```shell
packagemanager deploy awesome-project -s server.com -u username -p password
```

And again you'd need to tell what the previous code actually does.

## Features

Car:
* Represents individual vehicles in the system.
* Fields: Includes attributes like mark, model, year, and a unique win_code.
* Relation:
  * Each car is associated with one InfoCar instance through a OneToOneField.
  * This link ensures that every car has specific location details (country_location, city_location) managed in the InfoCar model.

InfoCar:
* Serves as a shared entity containing location-based information about cars and check-ups.
* Fields: country_location and city_location.
* Relation:
  * Linked to Car via a OneToOneField (related_name="cars").
  * Acts as a central hub connecting multiple owners (CarOwner) and check-ups (CheckUpCar) via ForeignKey relationships.

CarOwner:
* Represents the individuals who own vehicles in the system.
* Fields: Includes personal details like first_name, last_name, country, and email.
* Relation:
  * Each owner is linked to an InfoCar instance via a ForeignKey (related_name="owners").
  * This allows tracking multiple owners tied to the same car or location data.

CompanyCheckUp:
* Represents companies performing vehicle inspections.
* Fields: Extends the AbstractUser class with additional attributes for country and city.
* Relation:
  * Each company is linked to the check-ups they perform (CheckUpCar) through a ForeignKey (related_name="company").

CheckUpCar:
* Logs individual maintenance or diagnostic check-ups performed on cars.
* Fields: Includes details such as data_of_execution, kilometers, body_state, and health_check.
* Relation:
  * Linked to InfoCar via a ForeignKey (related_name="checkups"), associating each check-up with specific car/location data.
  * Also linked to CompanyCheckUp (related_name="company") to identify the company responsible for performing the check.

## Configuration

Here you should write what are all the configurations a user can enter when
using the project.

#### Settings
* Add your 'DATABASES' configuration in settings.py to connect to your preferred database.
* Update the 'ALLOWED_HOSTS' for deployment.

State what an argument does and how you can use it. If needed, you can provide
an example below.


## Links

- Project homepage: https://github.com/Vasavik-ua/car-verification.git
- Repository: https://github.com/Vasavik-ua?tab=repositories
- Deployed website: https://car-verification.onrender.com
