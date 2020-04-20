import bs4
import requests
import json
import datetime
import re

def ppa_data_raw(url = 'https://mapa.paa.gov.pl/'):
    data = requests.get(url).content
    soup = bs4.BeautifulSoup(data,features="lxml")

    scripts = soup.find_all('script')
    scripts = [s.contents[0] for s in scripts if len(s.contents)]

    data = None

    class ForEscaper(Exception): pass

    try:
        for script in scripts:
            for line in script.splitlines():
                if 'data_object' in line:
                    data = line.split('=',2)[1]
                    if data[-1] == ';':
                        data = data[0:-1]
                    data = data.strip()
                    data = json.loads(data)
                    raise ForEscaper()
    except ForEscaper: pass
    return { v['nazwa']:v for k,v in data.items()  }

def ppa_data_locations(url = 'https://mapa.paa.gov.pl/'):
    data = ppa_data_raw(url)

    loc_data = {}
    for city, city_data in data.items():
        loc_data[city]={'lon':city_data['loc_y'],'lat':city_data['loc_x']}

    return loc_data

def ppa_data_day(url = 'https://mapa.paa.gov.pl/'):
    data = ppa_data_raw(url)

    data_day = {}
    for city, city_data in data.items():
        series = []
        for s in city_data['srednie_dobowe']:
            date = [int(i) for i in re.findall(r"[\w']+", s[0])]
            date = datetime.datetime(*date)
            series.append( (date, float(s[1])) )
        
        data_day[city]=sorted(series, key=lambda sample: sample[0])

    return data_day
