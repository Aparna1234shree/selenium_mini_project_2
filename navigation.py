from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests


class CoWin:
    def __init__(self):
        """Initializes the WebDriver and opens the CoWIN website"""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://www.cowin.gov.in/")

    def click_anchor_tags(self):
        """Clicks on the FAQ and Partners links and opens them in new windows"""
        faq_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/faq']"))
        )
        faq_link.click()
        partners_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/our-partner']"))
        )
        partners_link.click()

    def get_window_handles(self):
        """Fetch and return window handles for FAQ and Partners"""
        window_handles = self.driver.window_handles
        return window_handles

    def switch_to_window(self, window_handle):
        """Switches to a window using its handle"""
        self.driver.switch_to.window(window_handle)

    def close_new_windows(self):
        """Closes all windows except the main window and switches back"""
        main_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)
                self.driver.close()
        self.driver.switch_to.window(main_window)

    def quit(self):
        """Quits the WebDriver and closes the browser"""
        self.driver.quit()


class Labour:
    def __init__(self):
        """Initializes the WebDriver and opens the Labour Ministry website"""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://labour.gov.in/")

    def close_popup(self):
        """Closes any popup that appears"""
        try:
            popup_close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='close']"))
            )
            popup_close_button.click()
            print("Popup closed.")
        except Exception as e:
            print(f"Error closing popup: {e}")

    def download_images(self):
        """Downloads images from the Labour Photo Gallery"""
        self.close_popup()

        # Navigate to the photo gallery
        self.driver.get("https://labour.gov.in/photo-gallery")

        image_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
        )

        os.makedirs("downloaded_photos", exist_ok=True)  # Create a directory to store images

        for index, img in enumerate(image_elements[:10]):  # Limit to first 10 images
            img_url = img.get_attribute("src")
            img_data = requests.get(img_url).content
            with open(f"downloaded_photos/photo_{index + 1}.jpg", 'wb') as handler:
                handler.write(img_data)
                print(f"Downloaded: photo_{index + 1}.jpg")

    def download_pdf(self, report_name):
        """Downloads a specific PDF report from the Labour website"""
        self.close_popup()

        # Navigate to the monthly progress report page
        self.driver.get("https://labour.gov.in/monthly-progress-report")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '{report_name}')]"))
        )

        # Retrieve the PDF URL
        pdf_link = self.driver.find_element(By.XPATH, f"//a[contains(@href, '{report_name}')]")
        pdf_url = pdf_link.get_attribute("href")

        print(f"Direct PDF URL: {pdf_url}")

        # Download the PDF using requests
        response = requests.get(pdf_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Save the PDF to the specified folder
        os.makedirs("downloaded_pdfs", exist_ok=True)  # Create a directory to store PDFs
        pdf_filename = os.path.join("downloaded_pdfs", report_name)
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(response.content)

        print(f"PDF downloaded successfully to: {pdf_filename}")

    def quit(self):
        """Quits the WebDriver and closes the browser"""
        self.driver.quit()


# Example usage
if __name__ == "__main__":
    cowin = CoWin()
    cowin.click_anchor_tags()
    cowin.quit()

    labour = Labour()
    labour.download_images()
    labour.download_pdf("mpr_july_2024.pdf")  # Change this as necessary
    labour.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import os
# import requests
#
#
# class CoWin:
#     def __init__(self):
#         """Initializes the WebDriver and opens the CoWIN website"""
#         service = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=service)
#         self.driver.maximize_window()
#         self.driver.get("https://www.cowin.gov.in/")
#
#     def click_anchor_tags(self):
#         """Clicks on the FAQ and Partners links and opens them in new windows"""
#         faq_link = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[@href='/faq']"))
#         )
#         faq_link.click()
#         partners_link = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[@href='/our-partner']"))
#         )
#         partners_link.click()
#
#     def get_window_handles(self):
#         """Fetch and return window handles for FAQ and Partners"""
#         window_handles = self.driver.window_handles
#         return window_handles
#
#     def switch_to_window(self, window_handle):
#         """Switches to a window using its handle"""
#         self.driver.switch_to.window(window_handle)
#
#     def close_new_windows(self):
#         """Closes all windows except the main window and switches back"""
#         main_window = self.driver.current_window_handle
#         for window_handle in self.driver.window_handles:
#             if window_handle != main_window:
#                 self.driver.switch_to.window(window_handle)
#                 self.driver.close()
#         self.driver.switch_to.window(main_window)
#
#     def quit(self):
#         """Quits the WebDriver and closes the browser"""
#         self.driver.quit()
#
#
# class Labour:
#     def __init__(self):
#         """Initializes the WebDriver and opens the Labour Ministry website"""
#         service = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=service)
#         self.driver.maximize_window()
#         self.driver.get("https://labour.gov.in/")
#
#     def close_popup(self):
#         """Closes any popup that appears"""
#         try:
#             popup_close_button = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[@class='close']"))
#             )
#             popup_close_button.click()
#             print("Popup closed.")
#         except Exception as e:
#             print(f"Error closing popup: {e}")
#
#     def download_images(self):
#         """Downloads images from the Labour Photo Gallery"""
#         self.close_popup()
#
#         # Navigate to the photo gallery
#         self.driver.get("https://labour.gov.in/photo-gallery")
#
#         image_elements = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
#         )
#
#         os.makedirs("downloaded_photos", exist_ok=True)  # Create a directory to store images
#
#         for index, img in enumerate(image_elements[:10]):  # Limit to first 10 images
#             img_url = img.get_attribute("src")
#             img_data = requests.get(img_url).content
#             with open(f"downloaded_photos/photo_{index + 1}.jpg", 'wb') as handler:
#                 handler.write(img_data)
#                 print(f"Downloaded: photo_{index + 1}.jpg")
#
#     def quit(self):
#         """Quits the WebDriver and closes the browser"""
#         self.driver.quit()
#
#
# # Example usage
# if __name__ == "__main__":
#     cowin = CoWin()
#     cowin.click_anchor_tags()
#     cowin.quit()
#
#     labour = Labour()
#     labour.download_images()
#     labour.quit()
