# import required dependencies
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.button import MDRaisedButton

# KV String
KV = '''
ScreenManager:
    HomeScreen:
    BinaryToDecimalScreen:
    DecimalToBinaryScreen:
    BinaryToOctalScreen:
    OctalToBinaryScreen:
    BinaryToHexadecimalScreen:
    HexadecimalToBinaryScreen:
    OctalToDecimalScreen:
    DecimalToOctalScreen:
    DecimalToHexadecimalScreen:
    HexadecimalToDecimalScreen:
    OctalToHexadecimalScreen:
    HexadecimalToOctalScreen:
    

<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: "Number Systems Converter App"
                halign: 'center'
                font_size: '24sp'
        GridLayout:
            cols: 1  # One columns
            padding: "10dp"
            spacing: "10dp"
            Button:
                text: "Binary to Decimal"
                on_release: root.manager.current = 'binary_to_decimal'
            Button:
                text: "Decimal to Binary"
                on_release: root.manager.current = 'decimal_to_binary'
            Button:
                text: "Binary to Octal"
                on_release: root.manager.current = 'binary_to_octal'
            Button:
                text: "Octal to Binary"
                on_release: root.manager.current = 'octal_to_binary'
            Button:
                text: "Binary to Hexadecimal"
                on_release: root.manager.current = 'binary_to_hexadecimal'
            Button:
                text: "Hexadecimal to Binary"
                on_release: root.manager.current = 'hexadecimal_to_binary'
            Button:
                text: "Octal to Decimal"
                on_release: root.manager.current = 'octal_to_decimal'
            Button:
                text: "Decimal to Octal"
                on_release: root.manager.current = 'decimal_to_octal'
            Button:
                text: "Decimal to Hexadecimal"
                on_release: root.manager.current = 'decimal_to_hexadecimal'
            Button:
                text: "Hexadecimal to Decimal"
                on_release: root.manager.current = 'hexadecimal_to_decimal'
            Button:
                text: "Octal to Hexadecimal"
                on_release: root.manager.current = 'octal_to_hexadecimal'
            Button:
                text: "Hexadecimal to Octal"
                on_release: root.manager.current = 'hexadecimal_to_octal'


<BinaryToDecimalScreen>:
    name: 'binary_to_decimal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Binary to Decimal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: binary_input
                hint_text: "Enter Binary Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_binary_to_decimal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: binary_to_decimal_result

<DecimalToBinaryScreen>:
    name: 'decimal_to_binary'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Decimal to Binary Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: decimal_input
                hint_text: "Enter Decimal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_decimal_to_binary()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: decimal_to_binary_result

<BinaryToOctalScreen>:
    name: 'binary_to_octal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Binary to Octal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: binary_input
                hint_text: "Enter Binary Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_binary_to_octal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: binary_to_octal_result

<OctalToBinaryScreen>:
    name: 'octal_to_binary'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Octal to Binary Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: octal_input
                hint_text: "Enter Octal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_octal_to_binary()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: octal_to_binary_result

<BinaryToHexadecimalScreen>:
    name: 'binary_to_hexadecimal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Binary to Hexadecimal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: binary_input
                hint_text: "Enter Binary Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_binary_to_hexadecimal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: binary_to_hexadecimal_result

<HexadecimalToBinaryScreen>:
    name: 'hexadecimal_to_binary'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Hexadecimal to Binary Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: hexadecimal_input
                hint_text: "Enter Hexadecimal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_hexadecimal_to_binary()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: hexadecimal_to_binary_result

<OctalToDecimalScreen>:
    name: 'octal_to_decimal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Octal to Decimal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: octal_input
                hint_text: "Enter Octal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_octal_to_decimal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: octal_to_decimal_result

<DecimalToOctalScreen>:
    name: 'decimal_to_octal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Decimal to Octal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: decimal_input
                hint_text: "Enter Decimal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_decimal_to_octal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: decimal_to_octal_result

<DecimalToHexadecimalScreen>:
    name: 'decimal_to_hexadecimal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Decimal to Hexadecimal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: decimal_input
                hint_text: "Enter Decimal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_decimal_to_hexadecimal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: decimal_to_hexadecimal_result

<HexadecimalToDecimalScreen>:
    name: 'hexadecimal_to_decimal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Hexadecimal to Decimal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: hexadecimal_input
                hint_text: "Enter hexadecimal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_hexadecimal_to_decimal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: hexadecimal_to_decimal_result
            
<OctalToHexadecimalScreen>:
    name: 'octal_to_hexadecimal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Octal to Hexadecimal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: octal_input
                hint_text: "Enter octal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_octal_to_hexadecimal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: octal_to_hexadecimal_result

<HexadecimalToOctalScreen>:
    name: 'hexadecimal_to_octal'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            canvas:
                Color:
                    rgba: 0, 0, 1, 1  # Blue background color (RGBA values)
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDIconButton:
                icon:"backspace"
                on_release: root.manager.current = 'home'
                theme_text_color: "Secondary"
            Label:
                text: "Hexadecimal to Octal Conversion"
                halign: 'center'
                font_size: '24sp'
        BoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"
            MDTextField:
                id: hexadecimal_input
                hint_text: "Enter hexadecimal Number"
                mode: "rectangle"
            MDRaisedButton:
                text: "Convert"
                on_release: root.convert_hexadecimal_to_octal()
            MDRaisedButton:
                text: "Clear"
                on_release: root.clear_input()
            MDLabel:
                id: hexadecimal_to_octal_result     

'''


class HomeScreen(Screen):
    pass

class BinaryToDecimalScreen(Screen):
    # converting binary to decimal function
    def convert_binary_to_decimal(self):
        binary_input = self.ids.binary_input.text
        try:
            decimal_result = str(int(binary_input, 2))
            self.ids.binary_to_decimal_result.text = (
                "Decimal Equivalent: " + decimal_result
            )
        except ValueError:
            self.ids.binary_to_decimal_result.text = "Invalid Binary Number"

    # clear inputs function
    def clear_input(self):
        self.ids.binary_input.text = ""
        self.ids.binary_to_decimal_result.text = ""

class DecimalToBinaryScreen(Screen):
    # converting binary to decimal function
    def convert_decimal_to_binary(self):
        decimal_input = self.ids.decimal_input.text
        try:
            binary_result = bin(int(decimal_input))[2:]
            self.ids.decimal_to_binary_result.text = (
                "Binary Equivalent: " + binary_result
            )
        except ValueError:
            self.ids.decimal_to_binary_result.text = "Invalid Decimal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.decimal_input.text = ""
        self.ids.decimal_to_binary_result.text = ""

class BinaryToOctalScreen(Screen):
    # converting binary to octal function
    def convert_binary_to_octal(self):
        binary_input = self.ids.binary_input.text
        try:
            octal_result = oct(int(binary_input, 2))[2:]
            self.ids.binary_to_octal_result.text = (
                "Octal Equivalent: " + octal_result
            )
        except ValueError:
            self.ids.binary_to_octal_result.text = "Invalid Binary Number"

    # clear inputs function
    def clear_input(self):
        self.ids.binary_input.text = ""
        self.ids.binary_to_octal_result.text = ""

class OctalToBinaryScreen(Screen):
    # converting octal to binary function
    def convert_octal_to_binary(self):
        octal_input = self.ids.octal_input.text
        try:
            binary_result = bin(int(octal_input, 8))[2:]
            self.ids.octal_to_binary_result.text = (
                "Binary Equivalent: " + binary_result
            )
        except ValueError:
            self.ids.octal_to_binary_result.text = "Invalid Octal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.octal_input.text = ""
        self.ids.octal_to_binary_result.text = ""

class BinaryToHexadecimalScreen(Screen):
    # converting binary to hexadecimal function
    def convert_binary_to_hexadecimal(self):
        binary_input = self.ids.binary_input.text
        try:
            hexadecimal_result = hex(int(binary_input, 2))[2:]
            self.ids.binary_to_hexadecimal_result.text = (
                "Hexadecimal Equivalent: " + hexadecimal_result
            )
        except ValueError:
            self.ids.binary_to_hexadecimal_result.text = "Invalid Binary Number"

    # clear inputs function
    def clear_input(self):
        self.ids.binary_input.text = ""
        self.ids.binary_to_hexadecimal_result.text = ""

class HexadecimalToBinaryScreen(Screen):
    # converting hexadecimal to binary function
    def convert_hexadecimal_to_binary(self):
        hexadecimal_input = self.ids.hexadecimal_input.text
        try:
            binary_result = bin(int(hexadecimal_input, 16))[2:]
            self.ids.hexadecimal_to_binary_result.text = (
                "Binary Equivalent: " + binary_result
            )
        except ValueError:
            self.ids.hexadecimal_to_binary_result.text = "Invalid Hexadecimal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.hexadecimal_input.text = ""
        self.ids.hexadecimal_to_binary_result.text = ""

class OctalToDecimalScreen(Screen):
    # converting octal to decimal function
    def convert_octal_to_decimal(self):
        octal_input = self.ids.octal_input.text
        try:
            decimal_result = int(octal_input, 8)
            self.ids.octal_to_decimal_result.text = (
                "Decimal Equivalent: " + str(decimal_result)
            )
        except ValueError:
            self.ids.octal_to_decimal_result.text = "Invalid Octal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.octal_input.text = ""
        self.ids.octal_to_decimal_result.text = ""

class DecimalToOctalScreen(Screen):
    # converting decimal to octal function
    def convert_decimal_to_octal(self):
        decimal_input = self.ids.decimal_input.text

        # Remove any leading "0x" if present
        decimal_input = decimal_input.lstrip('0o')
        decimal_value = int(decimal_input, 10)
        try:
            octal_result = oct(decimal_value)[2:]
            self.ids.decimal_to_octal_result.text = (
                "Octal Equivalent: " + octal_result
            )
        except ValueError:
            self.ids.decimal_to_octal_result.text = "Invalid Decimal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.decimal_input.text = ""
        self.ids.decimal_to_octal_result.text = ""

class DecimalToHexadecimalScreen(Screen):
    # converting decimal to hexadecimal function
    def convert_decimal_to_hexadecimal(self):
        decimal_input = self.ids.decimal_input.text

        # Remove any leading "0x" if present
        decimal_input = decimal_input.lstrip('0x')

        try:
            # Convert to an integer with base 10
            decimal_value = int(decimal_input, 10)

            # Convert to hexadecimal without "0x" prefix
            hexadecimal_result = hex(decimal_value)[2:]
            self.ids.decimal_to_hexadecimal_result.text = "Hexadecimal Equivalent: " + hexadecimal_result
        except ValueError:
            self.ids.decimal_to_hexadecimal_result.text = "Invalid Decimal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.decimal_input.text = ""
        self.ids.decimal_to_hexadecimal_result.text = ""

class HexadecimalToDecimalScreen(Screen):
    # converting hexadecimal to decimal function
    def convert_hexadecimal_to_decimal(self):
        hexadecimal_input = self.ids.hexadecimal_input.text
        try:
            decimal_result = int(hexadecimal_input, 16)
            self.ids.hexadecimal_to_decimal_result.text = (
                "Decimal Equivalent: " + str(decimal_result)
            )
        except ValueError:
            self.ids.hexadecimal_to_decimal_result.text = "Invalid Hexadecimal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.hexadecimal_input.text = ""
        self.ids.hexadecimal_to_decimal_result.text = ""

class OctalToHexadecimalScreen(Screen):
    # converting octal to hexadecimal function
    def convert_octal_to_hexadecimal(self):
        octal_input = self.ids.octal_input.text
        try:
            hexadecimal_result = hex(int(octal_input, 8))[2:]
            self.ids.octal_to_hexadecimal_result.text = (
                "Hexadecimal Equivalent: " + hexadecimal_result
            )
        except ValueError:
            self.ids.octal_to_hexadecimal_result.text = "Invalid Octal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.octal_input.text = ""
        self.ids.octal_to_hexadecimal_result.text = ""

class HexadecimalToOctalScreen(Screen):
    # converting hexadecimal to octal function
    def convert_hexadecimal_to_octal(self):
        hexadecimal_input = self.ids.hexadecimal_input.text
        try:
            octal_result = oct(int(hexadecimal_input, 16))[2:]
            self.ids.hexadecimal_to_octal_result.text = (
                "Octal Equivalent: " + octal_result
            )
        except ValueError:
            self.ids.hexadecimal_to_octal_result.text = "Invalid Hexadecimal Number"

    # clear inputs function
    def clear_input(self):
        self.ids.hexadecimal_input.text = ""
        self.ids.hexadecimal_to_octal_result.text = ""

# class MoreScreen(Screen):
#     pass

class NumberSystemsConverterApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    NumberSystemsConverterApp().run()
