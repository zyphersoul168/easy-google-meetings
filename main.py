import time
from meet import Meet

# lesson details
lesson_mail = 'jenesuirien@gmail.com'  # write your email
lesson_password = '12345'  # write your password
meeting_url = 'your_meeting_url.com'  # meeting url
lesson_day = 3  # Enter your lesson day in integer => 0-Tuesday, 1-Wednesday ... 5-Sunday 6-Monday
lesson_time = '15:05'  # Enter the time in 24 hour format. Example => 15:05
lesson_delay = 0  # Write a delay to enter to meeting in minutes. If you don't want a delay, just write 0

# Write your chromium-based browser path
browser_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

# chromedriver file must be in project root folder
chromedriver_path = 'chromedriver.exe'

# open browser
lesson = Meet(meeting_url, lesson_mail, lesson_password, browser_path, chromedriver_path)

print('Browser started')

# enter to meeting
time.sleep(lesson_delay * 3600)

lesson.log_into_gmail()
lesson.login_into_meeting()

print('Have a good time... :)')
