from kivy.app import App   
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



block_list= {
    "0":"0",
    1:"",
    2:"",
    3:"",
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
    9:"9",
    "10":"10",
    "11":"11",

    }

data_list= {
    "0":"0",
    1:"",
    2:"",
    3:"",
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
    9:"9",
    "10":"10",
    "11":"11",

    }




class MyLayout_W(Widget):
    pass
class FirstScrren(Screen):
    pass
class BarGraph(Screen):
	pass
class Pulse(Screen):
    i = str('15')
    pass
class Breese(Screen):
    pass
class Resalt(Screen):
    pass
class SecondScreen(Screen):
	pass

class ImageButton(ButtonBehavior, Image):

	pass

class ThirdScreen(Screen):
	pass


GUI = Builder.load_file("main.kv")

GUI1 = Builder.load_file("kv\\pulse.kv")

class MainApp(App):
    i = f"resalt"
    h="SoME STRING IS HERE "

    def build(self):
        try:
            global block_list
            read_lines = open("data.txt", "r",encoding = 'utf-8')
            data= read_lines.readlines()
            counter= 0

            name_data = data[1].split("\n")
            if name_data[0] != '':
                first_line=name_data[0]
                counter += 1
                block_list[1] = first_line

            name_data = data[2].split("\n")
            if name_data[0] != '':
                second_line=name_data[0]
                block_list[2] = second_line
                counter += 1

            name_data = data[3].split("\n")
            if name_data[0] != '':
                second_line1=name_data[0]
                block_list[3] = second_line1

            name_data = data[4].split("\n")    
            if name_data[0] != '':
                second_line2=name_data[0]
                block_list[4] = second_line2
            name_data = data[5].split("\n")    
            if name_data[0] != '':
                second_line2=name_data[0]
                block_list[5] = second_line2
            name_data = data[6].split("\n")    
            if name_data[0] != '':
                second_line2=name_data[0]
                block_list[6] = second_line2
            name_data = data[7].split("\n")    
            if name_data[0] != '':
                second_line2=name_data[0]
                block_list[7] = second_line2
            name_data = data[8].split("\n")  
            if name_data[0] != '':
                second_line2=name_data[0]
                block_list[8] = second_line2


            if counter == 2: 
                text_button1 = self.root.ids.screen1.ids.text_button1
                text_button1.text = f'{block_list[1]}/{block_list[2]}'

        except:
            print ("eee")

        return GUI and GUI1

    def change_screen(self, screen_name):
    	# Get the screen

    	screen_manager = self.root.ids['screen_manager']


    	screen_manager.current =screen_name



    def change_screen1(self, screen_name1):
        # Get the screen

        screen_manager = self.root.ids.pulse.ids['screen_manager1']
        screen_manager.current =screen_name1

    def animation_button(self, widget, *args):
            anim = Animation(background_color=(0,0,1,1), duration= 0.5)
            anim.start(widget)
    def animation_button_back(self, widget, *args):
            anim = Animation(background_color=(1,0,0,1), duration= 0.5)
            anim.start(widget)
    def base_breese(self, widget, *args):
        pass
    def color_pi(self, color):
        return '"F3CACA"'




    def first_screen1(self):
        read_lines = open("data.txt", "r",encoding = 'utf-8')
        data= read_lines.readlines()
        counter= 0
        try:

            data1 = data[1].split("\n")
            if data1[0] != '':
                first_line=data1[0]
                counter += 1
            data1 = data[2].split("\n")
            if data1[0] != '':
                second_line=data1[0]
                counter += 1
            if counter == 2: 
                text_button1 = self.root.ids.screen1.ids.text_button1
                text_button1.text = f"{first_line} / {second_line}"  
        except:  
            print(block_list)
        pass


#---------------------------------------------------------------------------------

    def self_data_read(self):

        try:
            read_lines = open("data_mail.txt", "r",encoding = 'utf-8')
            data_mail= read_lines.readlines()
            first_name = self.root.ids.screen3.ids.first_name
            birthday = self.root.ids.screen3.ids.birthday
            sex = self.root.ids.screen3.ids.sex
            growth = self.root.ids.screen3.ids.growth
            number_self = self.root.ids.screen3.ids.number_self
            number_doc = self.root.ids.screen3.ids.number_doc
            number_doc2 = self.root.ids.screen3.ids.number_doc2
            mail_to = self.root.ids.screen3.ids.mail_to

            global data_list
            
            
            

            name = data_mail[1].split("\n")
            if name[0] != '':
                first_name.text=name[0]
                data_list[1] = name[0]

            name = data_mail[2].split("\n")
            if name[0] != '':
                birthday.text=name[0]
                data_list[2] = name[0]

            name = data_mail[3].split("\n")
            if name[0] != '':
                sex.text=name[0]
                data_list[3] = name[0]

            name = data_mail[4].split("\n")
            if name[0] != '':
                growth.text=name[0]
                data_list[4] = name[0]

            name = data_mail[5].split("\n")
            if name[0] != '':
                number_self.text=name[0]
                data_list[5] = name[0]

            name = data_mail[6].split("\n")
            if name[0] != '':
                number_doc.text=name[0]
                data_list[6] = name[0]

            name = data_mail[7].split("\n")
            if name[0] != '':
                number_doc2.text=name[0]
                data_list[7] = name[0]

            name = data_mail[8].split("\n")
            if name[0] != '':
                mail_to.text=name[0]
                data_list[8] = name[0]

        except:
            print ("error")
        pass

    def self_data_seve(self, line, data):
        my_file1 = open("data_mail.txt", 'a',encoding = 'utf-8')
        if line == 1:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 2:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 3:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 4:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 5:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 6:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 7:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 8:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        my_file1.close()  
        pass
    def starter(self):
        my_file = open("data_mail.txt", 'w',encoding = 'utf-8')
        my_file.write(f'data_mail\n')
        my_file.close()
    def starter2(self):
        my_file = open("data.txt", 'w',encoding = 'utf-8')
        my_file.write(f'data\n')
        my_file.close()
        pass
    def data_base(self, line, data):
        global block_list
        block_list[line]= data

    def base_data(self):
        my_file1 = open("data.txt", 'a',encoding = 'utf-8')
        global block_list
        for i in range(1, 10):
            if block_list[i] == "":

                name = my_file1.write(f'\n')
                
            else:
                name = my_file1.write(f'{block_list[i]}\n')
        my_file1.close()
        pass    
    def bar_state_secondscreen(self):
        global block_list
        bar_size_1 = block_list[1]
        bar_size_2 = block_list[2]
        try:     
            bar_size_1 = f".{int(bar_size_1) // 3}"
            bar_size_2 = f".{int(bar_size_2) // 3}"
            bar1 = self.root.ids.screen2.ids.bargraph.ids.bar1
            bar2 = self.root.ids.screen2.ids.bargraph.ids.bar2
            bar1.size_hint = (.2 , bar_size_1)
            bar2.size_hint = (.2 , bar_size_2)
            mass1 = self.root.ids.screen2.ids.mass1
            if block_list[8] != '':
                mass1.text=block_list[8]


        except:
            print("bar_state_secondscreen")
        pass
    def bar_state_pulse(self, bar12, bar22):
        global block_list
        bar_size_1 = block_list[1]
        bar_size_2 = block_list[2]
        try:       
            bar_size_1 = f".{int(bar_size_1) // 3}"
            bar1 = self.root.ids.pulse.ids.bargraph.ids.bar1
            bar1.size_hint = (.2 , bar_size_1)
            bar_size_2 = f".{int(bar_size_2) // 3}"
            bar2 = self.root.ids.pulse.ids.bargraph.ids.bar2
            bar2.size_hint = (.2 , bar_size_2)
        except:
            print("bar_state_pulse")

        try:
            pulse_up = self.root.ids.pulse.ids.pulse_up
            pulse_down = self.root.ids.pulse.ids.pulse_down
            pulse_self = self.root.ids.pulse.ids.pulse_self
            mass = self.root.ids.pulse.ids.mass   

            if block_list[1] != '':
                pulse_up.text=block_list[1]


            if block_list[2] != '':
                pulse_down.text=block_list[2]


            if block_list[3] != '':
                pulse_self.text=block_list[3]


            if block_list[4] != '':
                mass.text=block_list[4]

        except:
            print("bar_state_pulse2")
        try:

            bar1 = self.root.ids.breese.ids.bargraph.ids.bar1
            bar1.size_hint = (.2 , bar_size_1)
            bar2 = self.root.ids.breese.ids.bargraph.ids.bar2
            bar2.size_hint = (.2 , bar_size_2)
        except:
            print("bar_state_pulse3")

        pass


  
    def update_case(self):

        try:
            print(block_list)
        except:
            print("error")


    def mail_senter(self):
        try:
            my_file = open("DOC.docx", 'w',encoding = 'utf-8')
            my_file.write(f'data_mail\n')
            my_file.write(f'{data_list}\n')
            my_file.write(f'{block_list}\n')
            my_file.close()

            label_mail = self.root.ids.screen3.ids.label_mail
            label_mail.text = "ЧТО-ТО НЕ ТАК"

            mail_content = '''Hello,
            This is a test mail.
            In this mail we are sending some attachments.
            The mail is sent using Python SMTP library.
            Thank You
            '''
            sender_address = '*******'
            sender = '*********'
            receiver_address = 'ascemmephone@gmail.com'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'A test mail sent by Python. It has an attachment.'
            message.attach(MIMEText(mail_content, 'plain'))
            attach_file_name = 'DOC.docx'
            attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)
            session = smtplib.SMTP_SSL('smtp.mail.ru', 465) 
            session.login(sender_address, sender)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            label_mail.text = "МАЙЛ ОТПРАВЛЕН"
            print('Mail Sent')
        except:
            print("mail error")
            
MainApp().run()