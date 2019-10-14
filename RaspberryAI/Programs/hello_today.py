# _*_ coding: utf-8 _*_
import datetime

now  = datetime.datetime.now()
today= now.date()
yobi = now.weekday()

print "今日 " + str(today) + " は"

if yobi in (5,6):
    print "週末！"
else:
    print "平日"
