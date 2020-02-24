import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from database import Database
database = Database()

base_url = "https://www.abc-mart.net"