from datetime import datetime
import time

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = int(str(now.hour))

mi = int(str(now.minute))

ss = int(str(now.second))

#9/16/2019 12:57:29
#.zfill(2) adds leading zeros if not exist
print(mm + "/" + dd + "/" + yyyy + " " + str(hour).zfill(2) + ":" + str(mi).zfill(2) + ":" + str(ss).zfill(2))

#2019-09-16 12:57:29.747046
print(datetime.now())

#1568631449.747047
print(time.time())

#time.struct_time(tm_year=2019, tm_mon=9, tm_mday=16, tm_hour=12, tm_min=57, tm_sec=4, tm_wday=0, tm_yday=259, tm_isdst=1)
print(time.localtime())

#Mon Sep 16 13:00:53 2019
print(time.asctime( time.localtime(time.time()) ))

