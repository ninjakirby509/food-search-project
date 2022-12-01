# [food-search-project](https://github.com/ninjakirby509/food-search-project)

Hello and welcome to Luke Renner & Chuong Vu's project! \
This was built as a test to understand and comprehend group work,
and also build a site we would find interesting. 

Both of us enjoyed the premise of getting free rein to create what we wanted,
and were even further surprised to see how much we learned for version control with multiplayer git.

On the other hand, the DB was having trouble getting connected for both of us, 
so we had to make it work with fly. Once that was complete, it was smooth sailing, besides us being concerned about prettiness. 

For project submission:
Choung pull requests [1](https://github.com/ninjakirby509/food-search-project/pull/2) & [2](https://github.com/ninjakirby509/food-search-project/pull/4)
Luke pull requests [1](https://github.com/ninjakirby509/food-search-project/pull/5) & [2](https://github.com/ninjakirby509/food-search-project/pull/7)

# TECHNICAL REQUIREMENTS
1. Flask server
2. Postgres database
3. User login using said database
4. Yelp REST API Integration 


# Implementation

This program was built in python and html using Flask and Jinja,
& API calls were made using the requests library.
After debugging, this was deployed [here](https://foodsearch.fly.dev/) using gunicorn and fly.io.

For this version, a database was built using postgresql and hosted on fly.io as well.

If you are looking to implement this yourself locally,
make sure to install requirements.txt, uncomment the bottom line of movieproject2.py,
and also create a .env file that contains ur api key and DB URL like so:\
`TMDB_API_KEY = *API CODE*`\
`DATABASE_URL = *db URL`
NOTE: you will also need to make a local proxy of your DB:

# Design issues

This was one of the most well done projects! It was done quickly and effectively,
and was properly split between us using [This document](https://docs.google.com/document/d/1uRxDllJQ2ZGM4v92ahzNubK1KAg4ZLNd5rClH7TnhUw/edit#heading=h.2e49ugtutnjr)

For future development, This project could definitely be further decorated on the main page.
It could definitely use a more refined search technique for the yelp, as it only really filters off of location.
