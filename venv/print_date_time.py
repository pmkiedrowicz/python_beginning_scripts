from datetime import datetime

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = int(str(now.hour))

mi = int(str(now.minute))

ss = int(str(now.second))

print (mm + "/" + dd + "/" + yyyy + " " + str(hour).zfill(2) + ":" + str(mi).zfill(2) + ":" + str(ss).zfill(2))