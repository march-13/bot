#python 2.7.15
import requests as req
nom = int(input('Nomer : '))
wa = req.get('https://passport.pedulisehat.id/v2/sms/captcha?mobile='+str(nom)+'&mobile_country_code=62&channel=Whatsapp&_=1591017456479').text
print wa