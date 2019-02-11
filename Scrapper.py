from MechanicalSoup import mechanicalsoup

# init and open connection to webpage
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://SCHOOL.fireflycloud.net.au/planner")

# Find and complete the login inputs
browser.select_form()
browser["username"] = "USERNAME"
browser["password"] = "PASSWORD"
browser.submit_selected()

# return html as soup
def getRaw():
    return browser.get_current_page().find_all("script")
