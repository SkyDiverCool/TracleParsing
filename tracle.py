import allmyrequests
import parsergarden
# usage example where we get the videos uploaded by userid ucoSWBde5iI(Wissotsky) and print the dataframe
raw_searchterm = "ucoSWBde5iI" 
# search,video,user
page = allmyrequests.amr_request(raw_searchterm, "user")

# search,video,user,user_videos
# user_videos is parsed from user page input
videodf = parsergarden.pg_parse(page, "user_videos")

print(videodf)
