#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

company1 = Company(name="Cisco", founding_year=1984)
company2 = Company(name="Apple", founding_year=1976)
company3 = Company(name="Amazon", founding_year=1994)

dev1 = Dev(name="Helen")
dev2 = Dev(name="Rose")
dev3 = Dev(name="Anthony")

freebie1 = Freebie(item_name="Backpack", value=50, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-shirt", value=12, dev=dev2, company=company2)
freebie3 = Freebie(item_name="Stickers", value=5, dev=dev3, company=company3)
freebie4 = Freebie(item_name="Hoodie", value=10, dev=dev1, company=company3)
freebie5 = Freebie(item_name="Notebook", value=15, dev=dev2, company=company1)

session.add_all([company1, company2, company3, dev1, dev2, dev3, freebie1, freebie2, freebie3, freebie4, freebie5])
session.commit()

print("Successful Database Seeding!")

session.close()
