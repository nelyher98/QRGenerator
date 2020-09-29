import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.button import Button
import hashlib
import qrcode
#-*-coding:utf8;-*-

with open("design.kv", encoding='utf-8') as kv_file:
    Builder.load_string(kv_file.read())

class test_screen(Screen):
    fhash = NumericProperty()
    redundancia = NumericProperty()
    formato = NumericProperty()
    texto = StringProperty('')
    hashing = StringProperty('')
    
    def llave(self):
        if(self.fhash != 0):
            if(self.fhash == 1):
                self.ids['btn1'].background_color = 1,0,0.5,1
                self.ids['btn2'].background_color = 0,0,0,1
                self.ids['btn3'].background_color = 0,0,0,1
            if(self.fhash == 2):
                self.ids['btn1'].background_color = 0,0,0,1
                self.ids['btn2'].background_color = 1,0,0.5,1
                self.ids['btn3'].background_color = 0,0,0,1
            if(self.fhash == 3):
                self.ids['btn1'].background_color = 0,0,0,1
                self.ids['btn2'].background_color = 0,0,0,1
                self.ids['btn3'].background_color = 1,0,0.5,1
        if(self.redundancia != 0):
            if(self.redundancia == 1):
                self.ids['btnB'].background_color = 1,0,0.5,1
                self.ids['btnM'].background_color = 0,0,0,1
                self.ids['btnA'].background_color = 0,0,0,1
            if(self.redundancia == 2):
                self.ids['btnB'].background_color = 0,0,0,1
                self.ids['btnM'].background_color = 1,0,0.5,1
                self.ids['btnA'].background_color = 0,0,0,1
            if(self.redundancia == 3):
                self.ids['btnB'].background_color = 0,0,0,1
                self.ids['btnM'].background_color = 0,0,0,1
                self.ids['btnA'].background_color = 1,0,0.5,1
        if(self.formato != 0):
            if(self.formato == 1):
                self.ids['btnJPG'].background_color = 1,0,0.5,1
                self.ids['btnPNG'].background_color = 0,0,0,1
            if(self.formato == 2):
                self.ids['btnJPG'].background_color = 0,0,0,1
                self.ids['btnPNG'].background_color = 1,0,0.5,1
                
    def leerTXT(self):
        if (self.ids['txtArchivo'].text != ""):
            abrir = self.ids['txtArchivo'].text + ".txt"
            with open(abrir, mode='r', encoding='utf-8') as fichero:
                self.texto = fichero.read()
            self.ids['lblTxt'].text = "Txt: " + self.texto
            fichero.close()
    
    def crearHASH(self):
        if(self.fhash != 0 and self.texto != ""):
            if(self.fhash == 1):
                h = hashlib.sha256(self.texto.encode()).hexdigest()
                self.ids['lblHASH'].text = "HASH: " + h
            if(self.fhash == 2):
                h = hashlib.sha384(self.texto.encode()).hexdigest()
                self.ids['lblHASH'].text = "HASH: " + h
            if(self.fhash == 3):
                h = hashlib.sha512(self.texto.encode()).hexdigest()
                self.ids['lblHASH'].text = "HASH: " + h
            self.hashing = h
            
    def habilitarQR(self):
        if (self.texto != "" and self.hashing != "" and self.fhash != 0 and self.formato != 0 and self.redundancia != 0):
            self.ids['btnQR'].disabled = False
        
    def crearQR(self):
        if(self.redundancia == 1):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            data = self.texto + "\n" + self.hashing
            qr.add_data(data)
            qr.make(fit=True)
        if(self.redundancia == 2):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            data = self.texto + "\n" + self.hashing
            qr.add_data(data)
            qr.make(fit=True)
        if(self.redundancia == 3):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            data = self.texto + "\n" + self.hashing
            qr.add_data(data)
            qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")    
        if(self.formato == 1):
            with open('codeqr.jpg', 'wb') as f:
                img.save(f)
        if(self.formato == 2):
            with open('codeqr.png', 'wb') as f:
                img.save(f)
        img.show()
        
class MainApp(App):
    def build(self):
        Window.clearcolor = 1,1,1,1
        return test_screen()

if __name__ == '__main__':
    MainApp().run()