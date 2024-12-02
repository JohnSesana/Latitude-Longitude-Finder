
# Postal Code Latitude and Longitude Scraper

This repository contains a Python script that scrapes latitude and longitude coordinates for a list of postal codes from Google search results using Selenium.

## Features

- Scrapes latitude and longitude data for Canadian postal codes.
- Uses Google search results to extract coordinates.
- Saves the extracted data into a CSV file (`output_coordinates_data.csv`).
- Includes real-time progress updates and periodic saves to prevent data loss.

## Prerequisites

- Python 3.x
- Google Chrome Browser
- ChromeDriver (compatible with your Chrome version)
- Required Python libraries: `selenium`, `pandas`

## Setup Instructions

1. **Install Required Libraries**:

   ```bash
   pip install selenium pandas
   ```

2. **Download ChromeDriver**:

   - Ensure you have Google Chrome installed on your system.
   - Download the correct version of ChromeDriver from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).

3. **Prepare Input Data**:

   - Create a CSV file named `input_postal_code_data.csv` with a column named `Postal_Code` containing the postal codes to process.

## How to Run

1. Place the input file (`input_postal_code_data.csv`) in the same directory as the script.
2. Adjust the `sleep_time` variable in the script if necessary to accommodate your internet speed.
3. Run the script:

   ```bash
   python main.py
   ```

4. The results will be saved to `output_coordinates_data.csv` in the same directory.

## Notes

- **Search Time**: Adjust the `sleep_time` variable based on your internet connection speed and system performance.
- **Google Search Limits**: Be mindful of search rate limits and CAPTCHA challenges from Google.

## Example Input File

`input_postal_code_data.csv`:

```
Postal_Code
A1A1A1
B2B2B2
C3C3C3
```

## Example Output File

`output_coordinates_data.csv`:

```
Postal Code,Latitude,Longitude
A1A1A1,53.534,-113.4909
B2B2B2,44.6488,-63.5752
C3C3C3,47.5615,-52.7126
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This script is intended for educational and personal use. Be cautious when scraping data to ensure compliance with Google’s Terms of Service.