import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Create a DataFrame to store results
results = []

data = pd.read_csv("input_postal_code_data.csv")
postal_codes = data['Postal_Code'].tolist()
output_file = "output_coordinates_data.csv"
sleep_time = 0.75 # Change this depending on your internet conection

try:
    for idx, postal_code in enumerate(postal_codes):
        # Open Google
        driver.get("https://www.google.com")
        time.sleep(sleep_time)

        # Search for the postal code with "latitude longitude"
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(f"{postal_code} latitude and longitude canada")
        search_box.send_keys(Keys.RETURN)
        time.sleep(sleep_time)

        # Initialize flags
        latitude = longitude = None

        # Try to extract latitude and longitude from search results
        try:
            result_divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'wvKXQ') or contains(@class, 'ky4hfd')]")
            for div in result_divs:
                text = div.text.strip()
                if "° N" in text and "° W" in text:
                    coords = text.split(",")
                    latitude = coords[0].strip().replace("° N", "").strip()  # Remove '° N'
                    longitude = coords[1].strip().replace("° W", "").strip()  # Remove '° W'
                    break  # Exit loop if valid coordinates are found

        except Exception as e:
            print(f"Error searching in divs for {postal_code}: {e}")

        # Fallback: Check for structured span data
        if not latitude or not longitude:
            try:
                spans = driver.find_elements(By.XPATH, "//span")
                for span in spans:
                    text = span.text
                    # Look for a pattern matching the coordinates in the span text
                    match = re.search(r"Latitude\s*:\s*([-+]?\d+\.\d+).+Longitude\s*:\s*([-+]?\d+\.\d+)", text, re.IGNORECASE)
                    if match:
                        latitude, longitude = match.groups()
                        break

            except Exception as e:
                print(f"Error searching in spans for {postal_code}: {e}")

        # Append results
        if latitude and longitude:
            results.append({"Postal Code": postal_code, "Latitude": latitude, "Longitude": longitude})
        else:
            results.append({"Postal Code": postal_code, "Latitude": "Not Found", "Longitude": "Not Found"})

        # Save results after each postal code to prevent data loss
        output_df = pd.DataFrame(results)
        output_df.to_csv(output_file, index=False)

        # Print progress (percentage)
        progress = (idx + 1) / len(postal_codes) * 100
        print(f"Progress: {progress:.2f}% - Processed {idx + 1}/{len(postal_codes)} postal codes")

finally:
    driver.quit()