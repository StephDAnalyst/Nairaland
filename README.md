# Nairaland Scraper using Selenium and Python

This Python script demonstrates how to scrape data from [Nairaland](https://www.nairaland.com/) using Selenium.

## Prerequisites

- Python installed
- Selenium WebDriver for Chrome ([Download here](https://sites.google.com/a/chromium.org/chromedriver/))

## Installation

It's a good practice to install the necessary packages within a virtual environment to keep your project dependencies isolated.

1. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv myenv
   ```
2.  **Activate the virtual environment:**

      -On Windows:
    ```bash
    .\myenv\Scripts\activate
    ```
      -On macOS and Linux:
   ```bash
 source myenv/bin/activate
   ```
3. **Install the required packages within the virtual environment:**
    ```bash
   pip install Selenium
   ```
## How to Use
1. Download and install the Chrome WebDriver, and specify the correct path in the script (executable_path).

2. Run the script Nairaland_Scraper.py.

3. The script will scrape data from Nairaland's URLs and save the results to a CSV file (Nairaland_data.csv).

## Script Overview
- The script uses Selenium to automate the web scraping process on Nairaland.

- It opens the Nairaland website, clikcs specific URLs, and extracts information from each page.

- The extracted data includes the post title, number of views, active users, and guests.

- The data is then saved to a CSV file for further analysis.
