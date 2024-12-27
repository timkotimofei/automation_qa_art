
class Urls:
    class Web:
        BASE = "https://demoqa.com"

        TEXT_BOX = f"{BASE}/text-box"
        CHECK_BOX = f"{BASE}/checkbox"
        RADIO_BUTTON = f"{BASE}/radio-button"
        WEBTABLES = f"{BASE}/webtables"
        BUTTONS = f"{BASE}/buttons"
        LINKS = f"{BASE}/links"
        CREATED = f"{BASE}/created"
        BAD_REQUEST = f"{BASE}/bad-request"
        UPLOAD_DOWNLOAD = f"{BASE}/upload-download"
        DYNAMIC_PROPERTIES = f'{BASE}/dynamic-properties'







    class API:
        BASE = "https://demoqa.com/swagger"
        GET_USER = f"{BASE}/user"




# print(Urls.Web.LOGIN)
# print(Urls.API.GET_USER)