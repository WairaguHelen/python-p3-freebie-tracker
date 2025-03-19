from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer(), nullable=False)

    freebies = relationship("Freebie", back_populates="company")

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, dev, item_name, value):
        """Creates a new Freebie instance and associates it with a Dev and this Company."""
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        return new_freebie
        

    @classmethod
    def oldest_company(cls, session):
        """Returns the oldest company based on founding year."""
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)

    freebies = relationship("Freebie", back_populates="dev")

    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name):
        """Returns True if the dev has received a freebie with the given name."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        """Transfers a freebie to another dev, if this dev owns it."""
        if freebie in self.freebies:
            freebie.dev = dev
            return True
        return False

class Freebie(Base):

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
    
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)

    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def __repr__(self):
        return f'<Freebie {self.item_name} (Value: {self.value})>'
