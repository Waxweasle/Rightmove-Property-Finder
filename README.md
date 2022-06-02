# Rightmove-Property-Finder
A program using Selenium to automate the finding and saving of desired properties listed on the real estate listing site, Rightmove.

## Prerequisites
1. Python 3.0+
2. A rightmove link of desired search conditions to supply to Selenium.
3. A Google form for data collection

## Usage
The program allows the user to collect a selection of listings from Rightmove that are set by the users set qualities/ parameters. Once the parameters are set, Selenium connects to Rightmove and pulls property listing info (address, cost and a link to the individual property ) and then uses Google Forms to submit and save the search results for the user for later access. If desired, the program can be automated and includes a function to email the user an alert that new properties have been added.

## Set-up
### Property search link
1. To obtain a link that will provide your desired properties, head over to https://www.rightmove.co.uk/
2. Enter your desired property requirements, add any additional filters/ page sorting and hit search
3. Once your results are visable, copy the url and paste it into
> RENTAL_PROPERTIES =

### Google form


### Selenium webdriver
1. Install selenium
```
pip install selenium
```
2. Go to https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ to install the driver for your system
3. Copy the file path from wherever you have the driver on your machine into 
> DRIVER_PATH =

## How to
Once your rightmove link is pasted in, Selenium will open your web browser and direct you to the search results and will the add them to your Google Form.
Results can be viewed by clicking the "Sheets icon" shortcut from the "Responses" page.
If you wish to automate the program, attach the send_email() function onto the end to be notified by email when new properties that match your search have been listed on Rightmove.
