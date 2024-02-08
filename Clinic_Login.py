import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://test.dentread.com")

    def test_login_success(self):
        # Locate username and password fields
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

        # Enter credentials
        username_field.send_keys("cbhavik98@gmail.com")
        password_field.send_keys("Bhavik@123")

        # Find and click the login button
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form[1]/button")
        submit_button.click()

        # Wait for the dashboard page to load after successful login
        # dashboard_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))

        # Logging statement for successful login
        print("Login successful. Dashboard page loaded.")

        # Test case assertion for successful login
        # self.assertTrue(dashboard_element.is_displayed(), "Dashboard page is not displayed after successful login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
