from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lon =  Column(Float, nullable=True)
    lat =  Column(Float, nullable=True)
    idx = Column(Integer, nullable=True)

    def __init__(self, name, lon=None,lat=None, idx=None):
        self.name = name
        self.lon = lon
        self.lat = lat
        self.idx = idx

    def __repr__(self):
        return self.name

#
class Radiation(Base):
    __tablename__ = 'radiation'

    id = Column(Integer, primary_key=True)
    background = Column(Float)
    datetime = Column(DateTime)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship("City", backref=backref('radiation', order_by=datetime))

    def __init__(self, city, background, datetime):
        self.city = city
        self.background = background
        self.datetime = datetime

    def __repr__(self):
        return "<Radiation('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
