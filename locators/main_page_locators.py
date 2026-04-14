from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, ".accordion__button")
    FAQ_ANSWERS = (By.CSS_SELECTOR, ".accordion__panel")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")