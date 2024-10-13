# import os
# import requests
# import pytest
# from navigation import CoWin
# from navigation import Labour
#
# @pytest.fixture
# def cowin():
#     instance = CoWin()
#     yield instance
#     instance.quit()
#
# @pytest.fixture
# def labour():
#     instance = Labour()  # Instantiate the Labour class
#     yield instance
#     instance.quit()
#
# def test_click_anchor_tags(cowin):
#     cowin.click_anchor_tags()
#     faq_window_handle, partners_window_handle, main_window_handle = cowin.get_window_handles()
#     assert faq_window_handle != partners_window_handle
#     assert main_window_handle != faq_window_handle
#     assert main_window_handle != partners_window_handle
#
# def test_switch_to_faq_window(cowin):
#     cowin.click_anchor_tags()
#     faq_window_handle, _, _ = cowin.get_window_handles()
#     cowin.switch_to_window(faq_window_handle)
#     assert cowin.driver.current_window_handle == faq_window_handle
#
# def test_switch_to_partners_window(cowin):
#     cowin.click_anchor_tags()
#     _, partners_window_handle, _ = cowin.get_window_handles()
#     cowin.switch_to_window(partners_window_handle)
#     assert cowin.driver.current_window_handle == partners_window_handle
#
# def test_close_new_windows(cowin):
#     cowin.click_anchor_tags()
#     cowin.close_new_windows()
#     assert len(cowin.driver.window_handles) == 1
#     assert cowin.driver.current_window_handle == cowin.driver.window_handles[0]
#
# def test_download_images(labour):
#     """Test case to verify downloading images from the Labour Photo Gallery."""
#     labour.download_images()  # Call the method in the Labour class
#     downloaded_images = os.listdir("downloaded_photos")
#
#     # Check if at least 10 images were downloaded
#     assert len(downloaded_images) >= 10
#
#     # Check if all downloaded images follow the expected naming pattern
#     expected_image_names = {f"photo_{i}.jpg" for i in range(1, len(downloaded_images) + 1)}
#     actual_image_names = set(downloaded_images)
#
#     assert actual_image_names == expected_image_names, f"Expected {expected_image_names} but got {actual_image_names}"
import os
import requests
import pytest
from navigation import CoWin, Labour


@pytest.fixture
def cowin():
    instance = CoWin()
    yield instance
    instance.quit()


@pytest.fixture
def labour():
    instance = Labour()  # Instantiate the Labour class
    yield instance
    instance.quit()


def test_click_anchor_tags(cowin):
    cowin.click_anchor_tags()
    faq_window_handle, partners_window_handle, main_window_handle = cowin.get_window_handles()
    assert faq_window_handle != partners_window_handle
    assert main_window_handle != faq_window_handle
    assert main_window_handle != partners_window_handle


def test_switch_to_faq_window(cowin):
    cowin.click_anchor_tags()
    faq_window_handle, _, _ = cowin.get_window_handles()
    cowin.switch_to_window(faq_window_handle)
    assert cowin.driver.current_window_handle == faq_window_handle


def test_switch_to_partners_window(cowin):
    cowin.click_anchor_tags()
    _, partners_window_handle, _ = cowin.get_window_handles()
    cowin.switch_to_window(partners_window_handle)
    assert cowin.driver.current_window_handle == partners_window_handle


def test_close_new_windows(cowin):
    cowin.click_anchor_tags()
    cowin.close_new_windows()
    assert len(cowin.driver.window_handles) == 1
    assert cowin.driver.current_window_handle == cowin.driver.window_handles[0]


def test_download_images(labour):
    """Test case to verify downloading images from the Labour Photo Gallery."""
    labour.download_images()  # Call the method in the Labour class
    downloaded_images = os.listdir("downloaded_photos")

    # Check if at least 10 images were downloaded
    assert len(downloaded_images) >= 10

    # Check if all downloaded images follow the expected naming pattern
    expected_image_names = {f"photo_{i}.jpg" for i in range(1, len(downloaded_images) + 1)}
    actual_image_names = set(downloaded_images)

    assert actual_image_names == expected_image_names, f"Expected {expected_image_names} but got {actual_image_names}"


def test_download_pdf(labour):
    """Test case to verify downloading the PDF report."""
    labour.download_pdf("mpr_july_2024.pdf")  # You may want to pass a variable for the report name
    downloaded_pdfs = os.listdir("downloaded_pdfs")

    # Check if the PDF has been downloaded
    assert "mpr_july_2024.pdf" in downloaded_pdfs, f"PDF not found in downloaded folder. Available PDFs: {downloaded_pdfs}"
