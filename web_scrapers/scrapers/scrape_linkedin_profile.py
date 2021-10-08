import json
import os
import subprocess
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# Attribution: https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/
# Prerequisite: brew install chromedriver
# Usage: OTP=123... EMAIL=example@example.com PASSWORD=123... USER=jack-sparrow venv/bin/python scrape_linkedin_profile.py > resume.md  # noqa
# OnePass Usage: ONEPASS_PASSWORD='123...' USER='jack-sparrow' venv/bin/python scrape_linkedin_profile.py > resume.md

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
OTP = os.getenv('OTP')
USER = os.getenv('USER')  # the user's url you want to scrape (eg: jack-sparrow)
ONEPASS_PASSWORD = os.getenv('ONEPASS_PASSWORD')
SLEEP_TIMER = 1.2  # The time between selenium clicks/entries etc. May need to be adjusted based on internet speed


def main():
    # global driver  # Keeps Chrome open after use
    # TODO: Allow this script to run in headless mode for automated CLI goodness
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # , options=options)

    login_to_linkedin(driver)

    page_content = navigate_to_profile(driver)

    scrape_profile_details(page_content)
    scrape_job_details(page_content)


def login_to_linkedin(driver):
    """This requires the user to pass in creds every time or use OnePass to
    retrieve credentials from 1Password automatically.
    """
    driver.get('https://www.linkedin.com/login')

    if ONEPASS_PASSWORD:
        creds = get_onepass_creds()

    username = driver.find_element_by_id('username')
    username_cred = creds['username'] if ONEPASS_PASSWORD else EMAIL
    username.send_keys(username_cred)

    password = driver.find_element_by_id('password')
    password_cred = creds['password'] if ONEPASS_PASSWORD else PASSWORD
    password.send_keys(password_cred)

    submit = driver.find_element_by_class_name('btn__primary--large')
    submit.click()

    time.sleep(SLEEP_TIMER)

    one_time_password = driver.find_element_by_class_name('input_verification_pin')
    otp_cred = creds['otp'] if ONEPASS_PASSWORD else OTP
    one_time_password.send_keys(otp_cred)

    submit_otp = driver.find_element_by_id('two-step-submit-button')
    submit_otp.click()


def get_onepass_creds():
    """Use OnePass to automate credential retrieval
    Reference: https://github.com/Justintime50/onepass
    """
    creds = subprocess.check_output(
        f'echo "{ONEPASS_PASSWORD}" | onepass list_item_login LinkedIn',
        stdin=None,
        stderr=None,
        shell=True
    )

    json_creds = json.loads(creds)

    return json_creds


def navigate_to_profile(driver):
    time.sleep(SLEEP_TIMER)
    driver.get(f'https://www.linkedin.com/in/{USER}')
    time.sleep(SLEEP_TIMER)

    return driver.page_source


def scrape_profile_details(page_content):
    """Scrapes a LinkedIn profile for things like name, tagline, etc
    """
    soup = BeautifulSoup(page_content, 'html.parser')

    profile_intro = soup.find('section', {'class': 'pv-top-card'})

    name = profile_intro.find('ul', {'class': 'pv-top-card--list'}).find('li').text.strip()
    tagline = profile_intro.find('h2').text.strip()

    print('# ' + name + '\n')
    print('## ' + tagline + '\n')

    # profile_details = {
    #     'name': name,
    #     'tagline': tagline,
    # }

    # return profile_details


def scrape_job_details(page_content):
    """Scrapes a LinkedIn profile for job details including
    company, title, description
    """
    # jobs = []
    soup = BeautifulSoup(page_content, 'html.parser')

    experience_section = soup.find('section', {'id': 'experience-section'})

    company_records = experience_section.find_all(
        'section', {'class': 'pv-profile-section__card-item-v2'}
    )

    for item in company_records:
        # Company entries with a single job
        if item.find('div', {'class', 'pv-entity__summary-info'}):
            company_name = item.find('p', {'class': 'pv-entity__secondary-title'})
            job_title = item.find('h3')
            date_range = item.find('h4').find_all('span')[1]
            job_description = item.find('div', {'class': 'pv-entity__extra-details'})
            strip_see_more = job_description.find(
                'span', {'class', 'inline-show-more-text__link-container-collapsed'}
            )
            if strip_see_more:
                strip_see_more.extract()
            # Remove stuff like "self-employed" from company name
            company_name_only = company_name.find('span', {'class': 'separator'})
            if company_name_only:
                company_name_only.extract()
            print(f'\n## {company_name.text.strip()}')
            print(f'\n### {job_title.text.strip()}')
            print(f'\n**{date_range.text.strip()}**')
            print(job_description.find('p').text.replace('*', '\n*').strip())
        # Company entries with multiple jobs
        elif item.find('div', {'class', 'pv-entity__company-details'}):
            company_name = item.find('h3').find_all('span')[1]
            print('\n##', company_name.text.strip())
            job_section = item.find_all('div', {'class', 'pv-entity__role-details'})

            for job in job_section:
                job_intro_section = job.find('div', {'class', 'pv-entity__summary-info-v2'})
                job_description_section = job.find('div', {'class', 'pv-entity__extra-details'})
                job_title = job_intro_section.find('h3').find_all('span')[1]
                date_range = job_intro_section.find('h4', {'class', 'pv-entity__date-range'}).find_all('span')[1]
                job_description = job_description_section.find('p', {'class', 'pv-entity__description'})
                strip_see_more = job_description.find(
                    'span', {'class', 'inline-show-more-text__link-container-collapsed'}
                )
                if strip_see_more:
                    strip_see_more.extract()
                print(f'\n### {job_title.text.strip()}')
                print(f'\n**{date_range.text.strip()}**')
                print(job_description.text.replace('*', '\n*').strip())

        # job_entry = {
        #     'company': company_name,
        #     'title': job_title,
        #     'date_range': date_range,
        #     'description': job_description,
        # }

        # jobs.append(job_entry)

        # return jobs


if __name__ == '__main__':
    main()
