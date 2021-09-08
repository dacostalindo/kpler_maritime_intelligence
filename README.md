# KPLER Maritime Intelligence

### Instructions

The source code is divided between the frontend and backend. The former is a VueJs project and the latter a Flask framework.

## State of the Project

<img src="resources\kpler_browser.png" alt="Drawing" style="width: 800px;">

## Frontend

The VueJS project has two main components; the map and navigation bar. Once the user chooses a vessel, the it will render its path at predefined speed, regarless of changes in time. It is a flaw of my design, where the following point is shown at the same rate regardless of how much received_time_utc has elapsed. I think I could have solved this with some more time. 

Another concern that arose at the end of my development, even if you only click on vessel they all start at the same time. For example, if you click on 5291, it will render that specific vessel. However, if later on you decide you want to visualize 5091, it will see it way ahed on its path as if it had started at same time as 5291. This is a problem with a watcher, a VueJS area that I want to learn more about, and haven't really worked on in the past.

## Backend

The POST method - insertNewEntry - checks the validity of any entry to be inserted into our database. It checks wether the vessel_id is a positive integer, whether the latitude and longitude fall within the physical constraints, for example is it on land or is it between the acceptable numerical range. It sets the time to UTC, non naive time. Finally, it checks for duplicate entries in the database. 

The GET methods - get_all_vessels_ids, get_vessel_data - are pretty straightforward, the former gets all the vessel ids, so that upon launching the web app it will show 5291, 5091, and 4378. The latter gets all of the date entries for a specific vessel_id.


