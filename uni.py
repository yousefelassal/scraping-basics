import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get('TEST'))