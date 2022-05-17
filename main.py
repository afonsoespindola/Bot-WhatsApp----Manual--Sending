import email.message
import webbrowser
import time
import pyautogui



def whatsapp():
    arquivo= open('contatos.txt', 'r')
    site = []
    email_empresa= []
    nome = []
    categoria = []
    fone = []
    count_enter = 0

    for pedacos in arquivo:
        teste=pedacos.split(':')
        site.append(teste[1].replace('//','http://'))
        email_empresa.append(teste[2])
        nome.append(teste[3])
        categoria.append(teste[4].replace('\n',''))
        fone.append(teste[5].replace('\n',''))

    for n in range(len(site)):
        if (len(fone[n]) > 1):
            textowhats = "Olá "+str(nome[n])+"Tudo bem?, Consegui seu contato no "+str(site[n])
            url = "https://wa.me/55"+str(fone[n])+"?text="+textowhats
            webbrowser.open_new_tab(url)
            time.sleep(10)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            pyautogui.press('enter')
            count_enter = count_enter +1



whatsapp()
time.sleep(10)

