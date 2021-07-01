import requests
import requests_cache
import bleach

def amr_request(data, type):
    clean_data = bleach.clean(data)
    requests_cache.install_cache('pagecache', backend='sqlite', expire_after=60)
    if type == "search":
        page = requests.get("https://www.tracle.tv/results?search_terms={}".format(clean_data), verify=False)
        return page
    if type == "video":
        page = requests.get("https://www.tracle.tv/watch?v={}".format(clean_data), verify=False)
        return page
    if type == "user":
        page = requests.get("https://www.tracle.tv/channel/{}/feed".format(clean_data), verify=False)
        return page