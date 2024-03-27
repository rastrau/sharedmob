import os
import zipfile
import requests
import datetime

urls = ["https://sharedmobility.ch/providers.json",
        "https://sharedmobility.ch/station_information.json",
        "https://sharedmobility.ch/free_bike_status.json",
        "https://sharedmobility.ch/station_status.json",
        "https://sharedmobility.ch/system_pricing_plans.json",
        "https://www.uvek-gis.admin.ch/BFE/disharing/geofences/geofencing_zones.json"]

filenames = []
for url in urls:
    print("Download %s..." % url)
    request = requests.get(url)

    filename = url.split("/")[-1]
    with open(filename, "w", encoding="utf-8") as f:
        f.write(request.text)
        filenames.append(filename)
        print("\tDone.")

now = datetime.datetime.now()
sharding_path = now.astimezone(datetime.timezone.utc).strftime("%Y-Week-%V")

if not os.path.exists(sharding_path):
    os.makedirs(sharding_path)

zipfilename = now.astimezone(
    datetime.timezone.utc).strftime("%Y-%m-%dT%H%M%S.zip")
with zipfile.ZipFile(os.path.join(sharding_path, zipfilename),
                     "w", compression=zipfile.ZIP_LZMA) as zf:
    for filename in filenames:
        zf.write(filename)
