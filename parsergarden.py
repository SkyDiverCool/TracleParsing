from re import S
from bs4 import BeautifulSoup
import pandas as pd

def pg_parse(data, type):
    soup = BeautifulSoup(data.content, 'html.parser')
    if type == "search":
        feeds = soup.find_all(class_="feed__video")
        dfcolnames =  ['Title', 'Desc', 'Creator', 'Views', 'Thumbnail', 'Timestamp', 'Link', 'CreatorLink']
        videodataframe = pd.DataFrame(columns = dfcolnames)
        for i in feeds:
            video = pd.Series(data=[str(i.find(class_="feed__video__details__title").text), 
                                    str(i.find(class_="feed__video__details__description").text),
                                    str(i.find(class_="feed__video__details__channel").text),
                                    str(i.find(class_="feed__video__details__views").text),
                                    str(i.img['src']),
                                    str(i.find(class_="feed__video__details__timestamp").text),
                                    str(i.a['href']),
                                    str(i.find(class_="feed__video__details__channel")['href'])], index=videodataframe.columns)
            
            videodataframe = videodataframe.append(video, ignore_index=True)

        return videodataframe

    if type == "video":
        videodeets = soup.find(class_="panel")
        dfcolnames = ['Title', 'Description', 'Creator', 'Views', 'Likes', 'Timestamp', 'CreatorID']
        videodataframe = pd.DataFrame(columns = dfcolnames)
        #https://www.tracle.tv/embed/NPQpcKg_PI8
        video = pd.Series(data=[str(soup.title.text),
                                str(videodeets.find(class_="panel__details__description").text),
                                str(videodeets.find(class_="panel__details__uploader").text),
                                str(videodeets.find(class_="panel__actions__views").text),
                                str(videodeets.find(class_="panel__details__likes").text),
                                str(videodeets.find(class_="panel__details__uploader").text),
                                str(videodeets.find(class_="panel__details__uploader").a['href'])], index=videodataframe.columns)

        videodataframe = videodataframe.append(video, ignore_index=True)

        return videodataframe

    if type == "user":
        userdeets = soup
        dfcolnames =  ['Username', 'Subscribers', 'Views', 'Description']
        userdataframe = pd.DataFrame(columns = dfcolnames)
        userdata = pd.Series(data=[str(userdeets.find(class_="channel__header__title").text),
                                   str(userdeets.find(id="sub-count").text),
                                   str(userdeets.find(class_="channel__header__views").find("span").text),
                                   str(userdeets.find(class_="channel-profile__about").text)], index=userdataframe.columns)

        userdataframe = userdataframe.append(userdata, ignore_index=True)
        
        return userdataframe

    if type == "user_videos":
        feeds = soup.find_all(class_="activity-feed__item")
        dfcolnames =  ['Title', 'Desc', 'Views', 'Thumbnail', 'Timestamp', 'Link']
        videodataframe = pd.DataFrame(columns = dfcolnames)
        for i in feeds:
            video = pd.Series(data=[str(i.find(class_="title").text), 
                                    str(i.find(class_="description").text),
                                    str(i.find(class_="views").text),
                                    str(i.img['src']),
                                    str(i.find(class_="activity-feed__item__timestamp").text),
                                    str(i.find(class_="title")['href'])], index=videodataframe.columns)
            
            videodataframe = videodataframe.append(video, ignore_index=True)

        return videodataframe
    
