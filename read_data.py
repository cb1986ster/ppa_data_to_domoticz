from session import session
from model import City, Radiation
from ppa_data import ppa_data_day
from domoticz import raw_domoticz_put

domoticz_data = []

for city_name, data in ppa_data_day().items():
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        if city.idx:
            for sample in data:
                if session.query(Radiation).filter_by(city=city, datetime=sample[0]).first() == None:
                    s = Radiation(city=city, background=sample[1], datetime=sample[0])
                    domoticz_data.append( (city.idx,sample[1],sample[0])  )
                    session.add(s)
    else:
        print('{} - Unknown city! Run `init_base`!',city_name)

if raw_domoticz_put(domoticz_data):
    session.commit()
