# Project for course TKT20011 Tietokantasovellus

## DinoPark
A web application for a dinosaur park, where users can view information about the park and dinosaurs, reserve viewing for feeding times and see the park map.

## Test DinoPark on Heroku
https://dino-park-app.herokuapp.com/
Please feel free to create your own user. If you want to test admin features, user: Boss, pw: spielberg. Admin login can be accessed at /admin. The database currently only has content until 16.10.2021. If you are accessing the app after that, please go to admin and add some feeding times manually for the full experience.

### Features
* User account creation and login
* Admin account login
* Viewing dinosaur info
* Reserving feeding times
* Searching for dinosaurs (location and info)
* Searching for feeding times (browsing or by search criteria)
* Admins can edit/remove/add feeding times

### Progress 26.9
The following features are implemented and working:
* User account creation and login
* Viewing dinosaur info
* Reserving feeding times

### Progress 10.10
Overview:
All critical features have been implemented. The app currently does not have graphics or a good user interface. Search/browse can be accessed at /search.
The following features are implemented and working:
* Admin account login 
* Reserving feeding times
* Searching for dinosaurs (by name)
* Searching for feeding times (by date)
* Browsing dinosaurs & feeding times today
* Admins can edit/remove/add feeding times

### Progress 24.10 final turn in
Overview:
All planned features have been implemented and the app has basic graphics. Some notes about the code and app itself:
* The map_hover() function in scripts.js could be improved. For some reason .getElementById did not work here.
* All dinosaurs share the same image, which could be improved. This photo is also not saved in the db. The correct version would have an image in dinosaurs db table.
* Search & browse content could be improved by adding links to reserving feeding times.
* In the Heroku version of the app, the homepage map seems a bit slow sometimes.
* The homepage map could have some text explaining the diferent areas.