from selenium import webdriver
import time

chrome_driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

short_delay = 5
short_delay_close_time = time.time() + short_delay

long_delay = 60 * 5
long_delay_close_time = time.time() + long_delay

while True:
    cookie.click()

    if time.time() > short_delay_close_time:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, _ in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = _

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        short_delay_close_time += short_delay

    if time.time() > long_delay_close_time:
        print(f"cookies/second: {driver.find_element_by_id('cps').text}")
        break

driver.quit()
