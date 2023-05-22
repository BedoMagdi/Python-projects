from deta import Deta
import os
from dotenv import load_dotenv



load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

deta = Deta(DETA_KEY)

db = deta.Base("monthly_report")


def insert_period(period, incomes, expenses, comment):
    """ Returns a report on a successful period insertion. """
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment":comment})


def fetch_all_periods():
    """ Return a dict of all periods. """
    res = db.fetch()
    return res.items


def get_period(period):
    """ get a report on a period. """
    return db.get(period)

