# import configparser
from serpapi import GoogleSearch
import datetime

# config = configparser.ConfigParser()
# config.read('config.ini')
# api_keys = config['API_KEYS']['MY_API_KEY']

params = {
    "engine": "google",
    "q": "Jadwal sholat di semarang hari ini",
    "hl": "en",
    "gl": "id",
    "api_key": 'c57e779ec89c6d6c54a88bb1a4374648d0aec15d855fd2b6f2c71c3a8d22b7fa'
}

search = GoogleSearch(params)
results = search.get_dict()
answer_box = results["answer_box"]['contents']["formatted"]

# Variable to store the answer
subuh = answer_box[0]['subuh']
dzuhur = answer_box[0]['zuhur']
ashar = answer_box[0]['asar']
maghrib = answer_box[0]['magrib']
isya = answer_box[0]['isya']

# make the value above to datetime, from (05.20) to (05:20)
subuh = datetime.datetime.strptime(subuh, '%H.%M').strftime('%H:%M')
dzuhur = datetime.datetime.strptime(dzuhur, '%H.%M').strftime('%H:%M')
ashar = datetime.datetime.strptime(ashar, '%H.%M').strftime('%H:%M')
maghrib = datetime.datetime.strptime(maghrib, '%H.%M').strftime('%H:%M')
isya = datetime.datetime.strptime(isya, '%H.%M').strftime('%H:%M')

# get the current time
now = datetime.datetime.now()
current_time = now.strftime("%H:%M")
print(f"Waktu Saat Ini\n\033[91m{current_time}\033[0m")

# create case to check the time
if now.strftime("%H:%M") < subuh:
    print("\nJadwal sholat mendatang ")
if now.strftime("%H:%M") < subuh:
    print(f"\033[33mSubuh \n{subuh}\033[0m\n")
elif now.strftime("%H:%M") < dzuhur:
    print("\nJadwal sholat mendatang ")
    print(f"\033[33mDzuhur \n{dzuhur}\033[0m\n")
elif now.strftime("%H:%M") < ashar:
    print("\nJadwal sholat mendatang ")
    print(f"\033[33mAshar \n{ashar}\033[0m\n")
elif now.strftime("%H:%M") < maghrib:
    print("\nJadwal sholat mendatang ")
    print(f"\033[33mMaghrib \n{maghrib}\033[0m\n")
elif now.strftime("%H:%M") < isya:
    print("\nJadwal sholat mendatang ")
    print(f"\033[33mIsya \n{isya}\033[0m\n")


print("Jadwal Sholat Hari Ini")
print("Subuh: " + "\t\t" +subuh)
print("Dzuhur: " + "\t" +dzuhur)
print("Ashar: " + "\t\t" +ashar)
print("Maghrib: " + "\t" +maghrib)
print("Isya: " + "\t\t" +isya)