import allmyrequests
import parsergarden

raw_searchterm = "ucoSWBde5iI"
# search,video,user
page = allmyrequests.amr_request(raw_searchterm, "user")

# search,video,video_comments,user
videodf = parsergarden.pg_parse(page, "user_videos")

print(videodf)