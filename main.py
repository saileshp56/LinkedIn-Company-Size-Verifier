import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Firefox driver
driver = webdriver.Chrome('/path/to/your/chromedriver')

# LOGIN ONCE
driver.get('https://www.linkedin.com/company/l3harris-technologies/about/')

emailStr = "" #linkedIn account email
passwordStr = "" #linekedIn account password
time.sleep(2)

username = driver.find_element('id', 'username')
username.send_keys(emailStr)
password = driver.find_element('id', 'password')
password.send_keys(passwordStr)
log_in_button = driver.find_element(By.CLASS_NAME, 'from__button--floating')
log_in_button.click()
# LOGIN ONCE DONE
#You will probably need to confirm you're a human by doing a Captcha here

# Wait for page to load
time.sleep(10)

header = ["Name", "Company Size", "Organization Type","Link", "Successful Scrape?", "Extra Company Size Information"]

links_list = ["Zwick USA, L.P.","11022903 Canada Inc.","101199652 Saskatchewan Ltd","10884235 CANADA INC.","Wood Mackenzie Limited","101110516 Saskatchewan Ltd","10551554 CANADA INC.","10x Genomics, Inc","101209983 Saskatchewan Ltd",]
to_append = " LinkedIn"

# Open output.txt file and CSV file
with open('final_output.txt', 'a') as f, open('final_csv_outputs.csv', 'a', encoding='UTF8', newline='') as csv_file:
    # Create CSV writer
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(header)

    for i in range(0, len(links_list)): #0 is the first index. If you have to stop and start again, you can adjust the 0 as needed
        lookup = links_list[i]
        data = [lookup, "", "Unknown", "Bad Link", "Yes", ""]
        try:
            search_term = lookup + to_append
            driver.get("https://www.google.com/search?q=" + search_term)

            # Wait for page to load
            time.sleep(2)

            first_link = driver.find_element(By.CSS_SELECTOR, 'div.yuRUbf > a')
            url = first_link.get_attribute('href')

            if 'linkedin.com' in url and "company" in url:
                about_url = url + '/about'
                data[3] = about_url
                driver.get(about_url)
                time.sleep(2)

                unclaimed_check = driver.find_elements(By.CSS_SELECTOR, 'h2.t-16')
                is_unclaimed = any('is an unclaimed page' in header.text for header in unclaimed_check)

                if is_unclaimed:
                    f.write(f'{lookup} at {driver.current_url}: This is an unclaimed page.\n')
                    data[4] = "Unclaimed page"
                else:
                    try:
                        non_profit_check = driver.find_element(By.XPATH, '//dd[text()="Non-profit Organizations"]')
                        f.write('Non-profit\n')
                        data[2] = "Non-Profit"
                    except:
                        f.write('Probably For-profit\n')
                        data[2] = "Probably For-Profit"

                    elements = driver.find_elements(By.TAG_NAME, 'dd')
                    f.write(f'{lookup} at {driver.current_url}:\n')
                    extra = False
                    for element in elements:
                        if 'employees' in element.text and extra:
                            data[5] += element.text
                            f.write(f'{element.text}\n')
                        elif 'employees' in element.text:
                            data[1] += element.text
                            extra = True
                            f.write(f'{element.text}\n')
            elif "company" not in driver.current_url:
                f.write(f'Could not find an about page for {lookup} from the original URL of {url}\n')
                data[3] = driver.current_url
                data[4] = "Not a company page"
            else:
                f.write(f'Could not find a LinkedIn page for {lookup}\n')
                data[4] = "No"

            f.write('---\n')
        except Exception as e:
            f.write(f'{lookup} at {driver.current_url}: NULL\n')
            f.write(f'Error: {e}\n')
            data[4] = "No"
            f.write('---\n')
        finally:
            # Write data to CSV file
            writer.writerow(data)

driver.quit()
