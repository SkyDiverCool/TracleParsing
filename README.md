# Parsing Tracle
A bunch of functions to parse tracle into a pandas dataframe. Not maintained

### Usage example (from tracle.py)
Import both scripts
```python
import allmyrequests
import parsergarden
```
Set values accordingly
```python
for_search = "cats" #string with your search query(In this example were looking for: cats)
for_user_data = "ucoSWBde5iI" #string with a user ID(In this example its the user: Wissotsky)
for_video_data = "NPQpcKg_PI8" #string with video ID(In this example its a video named: vlar pills)
```
Get the relevant webpage
```python
page = allmyrequests.amr_request(for_user_data, "user") #this will return the data(requests responce) of the page 
```
Parse the page
```python
#input the page you got into the relevant parsers.
#in the case of a user page you have two relevant parsers
#one returning info about the user and the other one returning the info about the user's videos
userinfodf = parsergarden.pg_parse(page, "user")
uservideosdf = parsergarden.pg_parse(page, "user_videos")

```
You are left with a dataframe(or a couple dataframes) to do whatever with.

### Why is SSL not enforced.
Because danjo cant figure out certbot and I needed this to get me data all the time tracle itself is avaiable to normal users.
Feel free to change that whenver that gets sorted and I will merge it in
