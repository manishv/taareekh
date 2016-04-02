import datetime, logging, requests


def getCauseList(url, date, listtype):
    payload = {'date' : date, 'criteria':'full', 'type': listtype }
    s = requests.Session()
    r = s.post(url, data=payload)

    if r.status_code != 200:
        ## Do you want throw an exception
        logging.error("post request failed with %d" % r.status_code)
        return None

    logging.info("Post request successful: <status_code>: %d" % r.status_code)
        ## Use beautifulsoup to parse the webpage
    return r.text


def getWorkingDay():
    day = datetime.date.today()
    if day.isoweekday() == 6:
        day = day + datetime.timedelta(2)
    elif day.isoweekday() == 7:
        day = day + datetime.timedelta(1)
    return day.strftime("%d/%m/%Y")

def main():

    logging.basicConfig(filename="test.log", level=logging.INFO, 
                        format='%(asctime)s %(levelname)s : %(message)s')


    LISTTYPE = {'DailyList': 'cause', 'FreshList':'fresh', 
                'Additional': 'unlisted' }
    url = "http://www.allahabadhighcourt.in/causelist/tempL.jsp"
    today = getWorkingDay()
    
    logging.info("##########################DAILYLIST#######################")
    logging.info(getCauseList(url, today, LISTTYPE['DailyList']))
    logging.info("##########################FRESHLIST#######################")
    logging.info(getCauseList(url, today, LISTTYPE['FreshList']))
    logging.info("##########################ADDITIONAL#######################")
    logging.info(getCauseList(url, today, LISTTYPE['Additional']))

if __name__ == '__main__':
    main()
