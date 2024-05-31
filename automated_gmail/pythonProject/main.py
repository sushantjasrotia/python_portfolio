from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()   #with capital first letter it means we initalize new object here
driver.get("https://keep.google.com/#home")
# driver.get("https://www.amazon.in/Samsung-Galaxy-Green-256GB-Storage/dp/B0BTYX1RP4/ref=sr_1_8?crid=37LKQTKYVJG21&dib=eyJ2IjoiMSJ9.H7DO_zWJTPmVY_saHBeX4WkVEYh3kW1SOxe_UnqMWzEHqcbU4wxMZyXnpx264ezQSp6oiPF1vMfU1HridIKx2RYYv7ZG61Zn5dGDzI0jGZhDIy3TynMGU-z2RzDcF9hMhJXgZLZJMi-H5sYvb_FYlg0R0OtIj7ZV0fU5F7bhUV6AN2F1GvDUF9mkhtKHXHujEp0hm4WqrqstbZPcraCMpCULWYK7WNydkKcgANt0ZsU.QJgYHYRPTDZO_IONiLKGXv-QFSJXXablnH2zdGQUKtM&dib_tag=se&keywords=s23&qid=1714670555&sprefix=s23%2Caps%2C252&sr=8-8")
# driver.get("https://www.google.com/search?q=ipl&rlz=1C1VDKB_enIN1071IN1071&oq=ipl&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDsyBggCEEUYQDIGCAMQRRg7MgYIBBBFGDwyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgyNTU1ajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8")
# price_of_phone = driver.find_element(By.CLASS_NAME, value="imspo_mh_cricket__score-major")
# print(f"The price is {price_of_phone.text}")
# phone_price = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
# print(f"the price is {phone_price.text}")
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_name[n].text,
#     }
# print(events)
# driver.quit()