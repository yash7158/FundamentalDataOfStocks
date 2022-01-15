# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
import csv
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup as soup

def web(y):
    
    """directing browser to stock page"""
    browser = webdriver.Chrome(
        executable_path='/Users/yashrajsingh/Desktop/desktop old/didi marks project app/chromedriver')
    browser.get('https://www.tickertape.in/screener')
    stock = browser.find_element_by_id("search-stock-input")
    stock.send_keys(y)
    time.sleep(7)
    stock.send_keys(Keys.ENTER)
    newUrl = browser.current_url
    url = str(newUrl)
    if "?" in url:
        i = url.index("?")
        url = url[0:i]
    print(url[33:])
    Url = str(url)
    
    
    
    """total revenue"""
    url = url+"/financials?checklist=basic&period=annual&statement=income&view=normal"
    browser.get(url)
    res = requests.get(url)
    page_html = res.text
    page_soup = soup(page_html, 'html.parser')
    re=page_soup.findAll('div', {"data-row":"incTrev"})
    trev = []
    for i in range(1,len(re)):
        a = str(re[i])
        a_Rev = a[::-1]
        n = ""
        for i in range(len(a_Rev)):
            if i>=20:
                if a_Rev[i]==">":
                    break
                else:
                    n = n+a_Rev[i]
        trev.append(n[::-1])
    trev.pop(len(trev)-1) 
    
    
    
    """net Income"""
    re=page_soup.findAll('div', {"data-row":"incNinc"})
    Ninc = []
    for i in range(1,len(re)):
        a = str(re[i])
        a_Rev = a[::-1]
        n = ""
        for i in range(len(a_Rev)):
            if i>=20:
                if a_Rev[i]==">":
                    break
                else:
                    n = n+a_Rev[i]
        Ninc.append(n[::-1])
    Ninc.pop(len(Ninc)-1) 
    
    """balence sheet total assets"""
    balUrl  = Url +"/financials?checklist=basic&period=annual&statement=balancesheet&view=normal"

    res = requests.get(balUrl)
    page_html = res.text
    page_soup = soup(page_html, 'html.parser')
    re=page_soup.findAll('div', {"data-row":"balTota"})
    ta = []
    for i in range(1,len(re)):
        a = str(re[i])
        a_Rev = a[::-1]
        n = ""
        for i in range(len(a_Rev)):
            if i>=20:
                if a_Rev[i]==">":
                    break
                else:
                    n = n+a_Rev[i]
        ta.append(n[::-1])
    ta.pop(len(ta)-1) 
    
    
    
    """total libilty"""
    re=page_soup.findAll('div', {"data-row":"balTotl"})
    tl = []
    for i in range(1,len(re)):
        a = str(re[i])
        a_Rev = a[::-1]
        n = ""
        for i in range(len(a_Rev)):
            if i>=20:
                if a_Rev[i]==">":
                    break
                else:
                    n = n+a_Rev[i]
        tl.append(n[::-1])
    tl.pop(len(tl)-1) 
    
    
    
    
    """total equity"""
    re=page_soup.findAll('div', {"data-row":"balTeq"})
    te = []
    for i in range(1,len(re)):
        a = str(re[i])
        a_Rev = a[::-1]
        n = ""
        for i in range(len(a_Rev)):
            if i>=20:
                if a_Rev[i]==">":
                    break
                else:
                    n = n+a_Rev[i]
        te.append(n[::-1])
    te.pop(len(te)-1) 
    
    """cash Flow"""
    
    cashFUrl = Url +"/financials?checklist=basic&period=annual&statement=cashflow"
    res = requests.get(cashFUrl)
    page_html = res.text
    page_soup = soup(page_html, 'html.parser')
    re=page_soup.findAll('div', {"data-row":"cafFcf"})
    cf = []
    for i in range(1,len(re)):
        a = str(re[i])
        a_Rev = a[::-1]
        n = ""
        for i in range(len(a_Rev)):
            if i>=20:
                if a_Rev[i]==">":
                    break
                else:
                    n = n+a_Rev[i]
        cf.append(n[::-1])
    cf.pop(len(cf)-1) 

    
    from prettytable import PrettyTable
    x = PrettyTable()
    x.field_names = ["S.No", "Name", "2016", "2017","2018","2019","2020","2021"]
    x.add_row([1,"Total Revenue",str(trev[len(trev)-6]),str(trev[len(trev)-5]),str(trev[len(trev)-4]),str(trev[len(trev)-3]),str(trev[len(trev)-2]),str(trev[len(trev)-1])])
    x.add_row([2,"Net Income",str(Ninc[len(Ninc)-6]),str(Ninc[len(Ninc)-5]),str(Ninc[len(Ninc)-4]),str(Ninc[len(Ninc)-3]),str(Ninc[len(Ninc)-2]),str(Ninc[len(Ninc)-1])])
    x.add_row([3,"Total Assits",str(ta[len(ta)-6]),str(ta[len(ta)-5]),str(ta[len(ta)-4]),str(ta[len(ta)-3]),str(ta[len(ta)-2]),str(ta[len(ta)-1])])
    x.add_row([4,"Total Libility",str(tl[len(tl)-6]),str(tl[len(tl)-5]),str(tl[len(tl)-4]),str(tl[len(tl)-3]),str(tl[len(tl)-2]),str(tl[len(tl)-1])])
    x.add_row([5,"Total Equity",str(te[len(te)-6]),str(te[len(te)-5]),str(te[len(te)-4]),str(te[len(te)-3]),str(te[len(te)-2]),str(te[len(te)-1])])
    x.add_row([6,"Free Cashflow",str(cf[len(cf)-6]),str(cf[len(cf)-5]),str(cf[len(cf)-4]),str(cf[len(cf)-3]),str(cf[len(cf)-2]),str(cf[len(cf)-1])])
    print(x)    


a = input()
web(a)
"""<span class="jsx-3755978062 value-cell-content typography-body-regular-s text-secondary undefined">1,50,774.00</span>
   <span class="jsx-3755978062 value-cell-content typography-body-regular-s text-secondary undefined">1,26,746.00</span>
"""