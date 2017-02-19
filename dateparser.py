import parsedatetime as pdt
import datetime

#for speech time to date time string. For instance, day after tomorrow when Jay Hack ends is 2017-02-19T10:00:00
def grabTime(timeString):
    cal = pdt.Calendar()
    now = datetime.datetime.now()

    strAll =  str(cal.parseDT(timeString, now)[0])
    strDay = strAll[0:10]
    strTime = strAll[11:16]
    finalDateTime = strDay + 'T' + strTime
    return finalDateTime
