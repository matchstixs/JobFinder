# CHROME BROWSER
## REACT requires new wait function for things to be loaded
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
# RANDOM SLEEPER TIME
from random import randint;
from time import sleep;
# IMPORT GOOGLE 
import gspread;
from oauth2client.service_account import ServiceAccountCredentials;
# pretty print
from pprint import pprint;

#google spreadsheet api 
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"];
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope);
client = gspread.authorize(creds);
# grab spreadsheet document
sheet = client.open("job").sheet1;

## parse document from spreadsheet
data = sheet.get_all_records();
# pprint(data);

# create/remove data
# insertRow = ["Hello", 5, "red"]
# insert row into document (data = const row , insert line 4)
# sheet.insert_row(insertRow, 4)
# sheet.delete_row(4)

class JobFinder:    
    bot = webdriver.Chrome();
    bot.get("https://www.indeed.com/jobs?q=remote+react+developer&l=New+York%2C+NY");
    sleep(randint(1, 4));
    
    # find jobs
    jobs = bot.find_elements_by_class_name("jobtitle")
    for i in range (len(jobs)):
        # print(jobs[i].text)

    # links for jobs
        job_links = [elem.get_attribute("href") for elem in jobs]
        # print(job_links)

        # get individual link elements; loop over links (enumeration)
        for i, link in enumerate(job_links):
            # goes to link
            bot.get(link)
            # adds link to second column of sheet
            sheet.update_cell(i + 2, 1, link)

            sleep(randint(1, 4));
            # grab data from link
            jobName = bot.find_element_by_class_name("jobsearch-JobInfoHeader-title").text
            jobCompany = bot.find_element_by_css_selector(".jobsearch-InlineCompanyRating > div:first-of-type").text

            sleep(randint(1, 4));
            # append to columns in sheets
            sheet.update_cell(i + 2, 2, jobName)
            sheet.update_cell(i + 2, 3, jobCompany)



JobFinder()