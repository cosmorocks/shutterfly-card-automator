from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.shutterfly.com/creationpath/bundle/views/projects/1b096ef8-71ef-11ef-8fce-ed6ba242058c?brand=SFLY&productCode=1229294&bundleId=3&sizeIds=27&occasionIds=118&styleIds=10829&qty=1&sizeId=undefined&bundleTypeName=ENVELOPE&groupId=3")
driver.quit()