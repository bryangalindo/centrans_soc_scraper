DRIVERPATH = "/Users/bryangalindo/PycharmProjects/centrans/soc/chromedriver"

# Textainer
csv_base_url = 'http://tex.textainer.com/Reserved.ReportViewerWebControl.axd?ReportSession={}1033&UICulture=1033&ReportStack=1&OpType=Export&FileName=Hello&ContentDisposition=OnlyHtmlInline&Format=CSV'
textainer_search_url = 'http://tex.textainer.com/Equipment/StatusAndSpecificationsInquiry.aspx'
textainer_data = {
    'ctl00_ScriptManager1_HiddenField' : '',
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATEGUID': '',
    '__VIEWSTATE': '',
    'express_form_id': '',
    'ccm_token': '',
    'ctl00$bodyContent$ucEqpIds$txtEqpId': '{}',
    'ctl00$bodyContent$btnSubmit': 'Preview',
}

# UES
UESURL = 'http://www.ueshk.com/tools/www_ajax.ashx'
ues_data = dict(action='getinquir', seach='')

# Interport
INTERPORTURL = 'https://idsng.iport.com/public/equipment_inquiry?utf8=%E2%9C%9' \
               '3&inquiry%5Bequipment_numbers%5D={}&commit=Look+up+unit'

# Conglobal Industries
CGIURL = 'http://cgi-dms.com/EirViewer/'

cgi_cookies = {
    'ASP.NET_SessionId': '',
    '__AntiXsrfToken': '',
}

cgi_data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    'ctl00$MainContent$gEirTxt': '',
    '__VIEWSTATE': '',
    '__VIEWSTATEGENERATOR': '',
    '__EVENTVALIDATION': '',
    'ctl00$MainContent$gUnitTxt': '',
    'ctl00$MainContent$EirButton': 'Get EIR',
}

# EMS
EMSURL = 'http://www.eaglemarineservices.com/tmsweb/unsecure/UNSCTRINQSRCH.tms?txtcntrsearch={}#ctrdata'

# Caru
CARUURL = 'https://portal.carucontainers.com/scripts/cgiip.exe/WService=caru/system/web/' \
          'sp-web-menu.r?program=DP.WEB-UNIT_INQUIRY&containernumber={}&Submit=Open'

# Miscellaneous
MONTHTONUMDICT = {'JAN': '1', 'FEB': '2', 'MAR': '3', 'APR': '4', 'MAY': '5', 'JUN': '6',
                  'JUL': '7', 'AUG': '8', 'SEP': '9', 'OCT': '10', 'NOV': '11', 'DEC': '12'}

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 '
                         '(KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
