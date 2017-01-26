import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_first():
    wd = webdriver.Chrome()
    wd.get("http://www.google.com/")
    wait = WebDriverWait(wd, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'sb_ifc0')))
    wd.quit
    print("the end.")


def test_login(app):
    print("the end.")

