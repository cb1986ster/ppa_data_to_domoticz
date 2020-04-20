from session import session
from model import City
import sys

city_name = sys.argv[1]
city_idx = int(sys.argv[2])

city = session.query(City).filter_by(name=city_name).first()
city.idx = city_idx

print('Setting {} idx {}...'.format(city_name,city_idx))

session.commit()

print('Done.')
