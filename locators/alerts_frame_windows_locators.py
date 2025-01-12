from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.ID, 'tabButton')
    TITLE_NEW_TAB = (By.ID, 'sampleHeading')

    NEW_WINDOW_BUTTON = (By.ID, 'windowButton')
    NEW_WINDOW_MESSAGE_BUTTON = (By.ID, 'messageWindowButton')

class AlertPageLocators:
    SEE_ALERT_BUTTON = (By.ID, 'alertButton')

    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.ID, 'timerAlertButton')

    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.ID, 'confirmResult')

    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_RESULT = (By.ID, 'promptResult')

class FramePageLocators:
    FIRST_FRAME = (By.ID, 'frame1')
    TEXT_FIRST_FRAME = (By.ID, 'sampleHeading')
    SECOND_FRAME = (By.ID, 'frame2')
    TEXT_SECOND_FRAME = (By.ID, 'sampleHeading')

class NestedFramesPageLocators:
    PARENT_FRAME = (By.ID, 'frame1')
    PARENT_TEXT = (By.XPATH, "//body[contains(text(), 'Parent frame')]")
    CHILD_FRAME = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.XPATH, "//p[contains(text(), 'Child Iframe')]")

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.ID, "showSmallModal")
    SMALL_MODAL_TITLE = (By.ID, "example-modal-sizes-title-sm")
    SMALL_MODAL_BODY = (By.XPATH, "//div[@class='modal-body']")
    OVERLAY = (By.XPATH, "//div[@role='dialog']")
    SMALL_MODAL_EXIT_BUTTON = (By.XPATH, "//span[contains(text(), '×')]")
    SMALL_MODAL_CLOSE_BUTTON = (By.ID, "closeSmallModal")

    LARGE_MODAL_BUTTON = (By.ID, "showLargeModal")
    LARGE_MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    LARGE_MODAL_BODY = (By.XPATH, "//p[contains(text(), 'Lorem Ipsum')]")
    LARGE_MODAL_EXIT_BUTTON = (By.XPATH, "//span[contains(text(), '×')]")
    LARGE_MODAL_CLOSE_BUTTON = (By.ID, "closeLargeModal")


