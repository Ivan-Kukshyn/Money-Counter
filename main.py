from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Money Counter App
class MoneyApp(App):
    def build(self):
        # Osnovnoi maket 
        layout = BoxLayout(orientation='vertical', padding=1, spacing=0)

        # Vidget  dlya voda chisla
        cashLabel = Label(text='Наличные', font_size='32sp')
        self.cashInput = TextInput(hint_text='', input_filter = 'float', multiline=False, write_tab=False, font_size='32sp')
        self.cashInput.bind(text=self.allMoney)
        layout.add_widget(cashLabel)
        layout.add_widget(self.cashInput)

        kursEvroGrivna = Label(text='Курс Евро/Гривна', font_size='32sp')    
        self.kursEvroGrivna = TextInput(hint_text='', input_filter = 'float', multiline=False, write_tab=False, font_size='32sp')
        self.kursEvroGrivna.bind(text=self.allMoney)
        layout.add_widget(kursEvroGrivna)
        layout.add_widget(self.kursEvroGrivna)

        ukrCardLabel = Label(text='Украинская карта', font_size='32sp')    
        self.ukrCardInput = TextInput(hint_text='', input_filter = 'float', multiline=False, write_tab=False, font_size='32sp')
        self.ukrCardInput.bind(text=self.allMoney)
        layout.add_widget(ukrCardLabel)
        layout.add_widget(self.ukrCardInput)

        frCardLabel = Label(text='Французская карта', font_size='32sp')  
        self.frCardInput = TextInput(hint_text='', input_filter = 'float', multiline=False, write_tab=False, font_size='32sp') 
        self.frCardInput.bind(text=self.allMoney)
        layout.add_widget(frCardLabel)
        layout.add_widget(self.frCardInput)

        # Vidget dlya pokaza summy deneg
        self.sum_label = Label(text='', font_size='32sp')
        layout.add_widget(self.sum_label)


        self.percent50_label = Label(text='', font_size='32sp')
        layout.add_widget(self.percent50_label)


        self.percent30_label = Label(text='', font_size='32sp')
        layout.add_widget(self.percent30_label)


        self.percent20_label = Label(text='', font_size='32sp')
        layout.add_widget(self.percent20_label)

        return layout
    
    def allMoney(self, instance, value):
        # Obrabotchik izmenenii texta v TextInput
        try:
            cash = float(self.cashInput.text)
            kursEvroGrivna = float(self.kursEvroGrivna.text)
            ukrCard = float(self.ukrCardInput.text)
            frCard = float(self.frCardInput.text)
            # Сумма
            allNumbers = cash + ukrCard/kursEvroGrivna + frCard
            self.sum_label.text = f"Всего денег: {allNumbers:.2f} евро"

            # 50% от суммы
            percent_important = allNumbers * 0.5 
            self.percent50_label.text = f"50% от суммы: {percent_important:.2f} евро"

            # 30% от суммы
            percent_wishes = allNumbers * 0.3 
            self.percent30_label.text = f"30% от суммы: {percent_wishes:.2f} евро"

            # 20% от суммы
            percent_savings = allNumbers * 0.2 
            self.percent20_label.text = f"20% от суммы: {percent_savings:.2f} евро"
        except ValueError:
            self.sum_label.text = ""
            self.percent50_label.text = ""
            self.percent30_label.text = ""
            self.percent20_label.text = ""

if __name__ == '__main__':
    MoneyApp().run()