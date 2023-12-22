
import json
import os
import shutil
import time
from typing import Tuple
from concurrent.futures import ProcessPoolExecutor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from app.tools import utility as ut
from app.tools.config import config
from app.tools.logger import get_logger


logger = get_logger(__name__)

MAX_PROCESS = config.BANYAK_PROSES


def main():
    starttime = time.perf_counter()
    ut.starting_text()
    
    params_case_01 = [("sampling"), ("sampling_1"), ("sampling_2")]
    
    print()
    with ProcessPoolExecutor(max_workers=MAX_PROCESS) as executor:
        results = executor.map(case_01, params_case_01)
    endtime = time.perf_counter()
    
    total_time = int(endtime - starttime)
    total_time = ut.convert_seconds_to_time(total_time)


def case_01(param):
    
    #sample code
    pass

