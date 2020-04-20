from model import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

d = os.path.dirname(os.path.realpath(__file__))
engine = create_engine('sqlite:///{}/data.db'.format(d), echo=False)
Session = sessionmaker(bind=engine)
session = Session()
