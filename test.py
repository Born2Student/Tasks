import csv

from dateutil.parser import parse

from sqlalchemy import Column, Date, Float, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


Base = declarative_base()



""" Now we will define the user class """
class Tasks(Base):
    # Tasks_ID, Description, User_ID

    __tablename__ = "tasks"      # This is User class database table name attribute

    # task_id
    Tasks_ID = Column(Integer, primary_key = True)        # This the primary key attribute

    # description
    Description = Column(String(30))

    # User_ID
    User_ID = Column(Integer)

    # Sprint_ID
    Sprint_ID = Column(Integer)

    # Team_ID
    Team_ID = Column(Integer)

    # Story_Points
    Story_Points = Column(Integer, nullable=True)

    Current_State = Column(String(30))


    # Sprint_ID , Team_ID, Story_Points, Current_State 




from sqlalchemy import create_engine

engine = create_engine("sqlite:///tasks.sqlite3", echo=True)

""" IMPORT THE SQALCHEMY ORM MODULE SESSIONMAKER METHOD  """
from sqlalchemy.orm import sessionmaker


""" We will create a user object which is an instance of the User class and which will take keyword arguments.  """
# tasks = Tasks(description = 'Chris', user_id = 5, sprint_id = 1, team_id = 8, story_points = 23, current_state = 'done')


""" IMPORT THE SQALCHEMY ORM MODULE SESSIONMAKER METHOD  """
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)


def parse_none(dt):
    """Trys to parse a string date and returns None if unable to."""

    try:
        return parse(dt)
    except:
        return None


def prepare_listing(row):
    """Takes a row from CSV file and returns a Listing object from it."""

    row["Story_Points"] = parse_none(row["Story_Points"])
    return Tasks(**row)



with open("new_tasks.csv", encoding="utf-8", newline="") as csv_file:
    csvreader = csv.DictReader(csv_file, quotechar='"')

    listings = [prepare_listing(row) for row in csvreader]

    session = Session()
    session.add_all(listings)
    session.commit()
