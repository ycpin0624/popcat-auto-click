# popcat-auto-clicker 

```python=
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

chrome.get("https://popcat.click/")
target = chrome.find_element_by_xpath('//*[@id="app"]/div')

while(True):
    target.click()
```
[Here is my Medium artical.](https://medium.com/@yangpokemonpin/%E5%BE%9E-popcat-%E7%86%B1%E6%BD%AE%E4%B8%AD%E5%AD%B8%E7%BF%92-selenium-python-%E8%88%87%E7%B6%B2%E9%A0%81%E8%87%AA%E5%8B%95%E5%8C%96-4df2619a228b)
