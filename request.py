import requests

url = 'http://127.0.0.1:5000/predict_api'
r = requests.post(url,json={
                            "having_IP_Address":-1, 
                             "URL_Length":1,
                             "Shortining_Service":1,
                             "double_slash_redirecting":-1,
                             "Prefix_Suffix":-1,
                             "having_Sub_Domain":-1,
                             "SSLfinal_State":-1,
                             "Domain_registeration_length":-1,
                             "Request_URL":1,
                             "URL_of_Anchor":-1,
                             "Links_in_tags":1,
                             "SFH":-1,
                             "Abnormal_URL":-1,
                             "Redirect":0,
                             "RightClick":1,
                             "age_of_domain":-1,
                             "DNSRecord":-1,
                             "web_traffic":-1,
                             "Page_Rank":-1,
                             "Google_Index":1,
                             "Links_pointing_to_page":1
                             })

                             

print(r.json())