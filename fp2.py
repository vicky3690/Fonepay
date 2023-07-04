import uiautomator2 as u2

# connect the device
d = u2.connect()

# Launch the app (e.g., Twitter)
d.app_start("com.esewa.android")

# Wait for the app to load
d.wait_activity("com.esewa.android.app.main.MainActivity", timeout=20)

# Perform automated actions
# Example: Click on the search button
d(resourceId="com.esewa.android:id/toolbar_login/register").click()

# Wait for some time to allow for manual interaction
input("Perform manual actions and press Enter when ready...")

# Continue with automated actions
# Example: Enter a search query
Mobile Number_box = d(resourceId="com.esewa.android:id/toolbar_login/register_edittext")
search_box.set_text("OpenAI")

# Close the app
d.app_stop("com.esewa.android")