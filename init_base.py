from session import session, Base, engine
from model import City
from ppa_data import ppa_data_locations

Base.metadata.create_all(engine)

for city, info in ppa_data_locations().items():
    current = session.query(City).filter_by(name=city).first()
    if current:
        current.lon = info['lon']
        current.lat = info['lat']
    else:
        new_city = City(name=city,lon=info['lon'],lat=info['lat'])
        session.add(new_city)

session.commit()
