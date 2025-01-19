
class Urls:
    class Web:
        BASE = "https://demoqa.com"

        # Elements
        TEXT_BOX = f"{BASE}/text-box"
        CHECK_BOX = f"{BASE}/checkbox"
        RADIO_BUTTON = f"{BASE}/radio-button"
        WEBTABLES = f"{BASE}/webtables"
        BUTTONS = f"{BASE}/buttons"
        LINKS = f"{BASE}/links"
        CREATED = f"{BASE}/created"
        BAD_REQUEST = f"{BASE}/bad-request"
        UPLOAD_DOWNLOAD = f"{BASE}/upload-download"
        DYNAMIC_PROPERTIES = f"{BASE}/dynamic-properties"

        # Forms

        # Alert, Frame,  Windows
        BROWSER_WINDOWS = f"{BASE}/browser-windows"
        ALERTS = f"{BASE}/alerts"
        FRAMES = f"{BASE}/frames"
        NESTED_FRAMES = f"{BASE}/nestedframes"
        MODAL_DIALOGS = f"{BASE}/modal-dialogs"



        # Widgets

        ACCORDIAN = f"{BASE}/accordian"
        AUTO_COMPLETE = f"{BASE}/auto-complete"



    class API:
        BASE = "https://demoqa.com/Account/v1"
        AUTHORIZED = f"{BASE}/Authorized"






# print(Urls.Web.ACCORDIAN)
# print(Urls.API.POST_ACCOUNT)