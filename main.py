import kivy 

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<MyLayout>
    BoxLayout:
        orientation: "vertical"
        size: self.size
        pos: self.pos
        TextInput:
            id: calc_input
            text: "0"
            halign: "right"
            font_size: 50
            size_hint: (1, .15)
        
        GridLayout:
            cols: 4
            rows: 5
            spacing: 1,1

            # строка 1
            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "%"
                background_color: "#036900"
                background_normal: ""
                on_press: root.proc()
            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: u"\u00AB"
                background_color: "#036900"
                background_normal: ""
                on_press: root.remove()

            Button: 
                id: clear
                size_hint: (.2, .2)
                font_size: 32
                text: "C"
                background_color: "#036900"
                background_normal: ""
                on_press: root.clear()

                
            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "/"
                background_color: "#036900"
                background_normal: ""
                on_press: root.delenie()

            # строка 2
            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "7"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(7)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "8"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(8)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "9"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(9)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "*"
                background_color: "#036900"
                background_normal: ""
                on_press: root.multiply()
            
            # строка 3
            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "4"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(4)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "5"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(5)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "6"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(6)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "-"
                background_color: "#036900"
                background_normal: ""
                on_press: root.minus()
            
            # строка 4
            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "1"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(1)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "2"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(2)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "3"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(3)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "+"
                background_color: "#036900"
                background_normal: ""
                on_press: root.add()
            
            # строка 5
            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "+/-"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.pos_neg()

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "0"
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.button_press(0)

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "."
                background_color: '#6ec98d'
                background_normal: ""
                on_press: root.dot()

            Button: 
                size_hint: (.2, .2)
                font_size: 32
                text: "="
                background_color: "#036900"
                background_normal: ""
                on_press: root.equals()
                

''')

class MyLayout(BoxLayout):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ""

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f"{prior}{button}"
    
    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'

    def delenie(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'

    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}*'

    def minus(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'
    
    def proc(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}%'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]

        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text

        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
          
    def equals(self):
        prior = self.ids.calc_input.text

        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            for num in num_list:
                answer = answer + float(num)
            self.ids.calc_input.text = str(answer)
                        

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()