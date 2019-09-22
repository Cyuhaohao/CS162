import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///bank.db')
engine.connect()
Base = declarative_base()

class Clients(Base):
    __table__ = 'clients'
    clientnumber = Column(Integer, primary_key = True)
    name = Column(String)
    email=Column(String)
    phone = Column(String)

class Loans(Base):
    __table__ = 'loans'
    acountnumber = Column(Integer, primary_key=True)
    clientnumber = Column(Integer, ForeignKey('clients.clientnumber'))
    balance = Column(Integer)
    status = Column(String)

Base.metadata.create_all(engine)
client=Clients(clientnumber=1,name="yuhao",email="yuhao@minerva.kgi.edu",phone="9346474873")
Session = sessionmaker(bind=engine)
session = Session()
session.add(client)
session.commit()

print(session.query(Clients).filter_by(name='yuhao').first())


