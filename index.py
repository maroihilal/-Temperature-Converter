from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel ,QFrame ,QRadioButton,  QLineEdit, QPushButton,QMessageBox,QButtonGroup
import sys

class fenêtre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,700,900)
        self.setFixedSize(700,950)
        self.setWindowTitle("Temperature Conversion")
        self.setStyleSheet("background-color:#F59E0B;")
        
                
        self.title=QLabel("Temperature Conversion \n         Calculator",self)
        self.title.setGeometry(60,-80,600,350)
        self.title.setStyleSheet(" color:#FFF8F0;font-size:50px;font-weight:900;font-family:Arial;")
        
        #frame 1:
        
        
        self.frame1=QFrame(self)
        self.frame1.setGeometry(60, 180, 560, 800)
        self.rb1 = QRadioButton("Celsius to Fahrenheit", self.frame1)
        self.rb1.setGeometry(80, 70, 400, 60)
        self.rb1.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.rb2 = QRadioButton("Fahrenheit to Celsius", self.frame1)
        self.rb2.setGeometry(80, 150, 400, 60)
        self.rb2.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.rb3 = QRadioButton("Celsius to Kelvin", self.frame1)
        self.rb3.setGeometry(80, 230, 400, 60)
        self.rb3.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.rb4 = QRadioButton("Kelvin to Celsius", self.frame1)
        self.rb4.setGeometry(80, 310, 400, 60)
        self.rb4.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.rb5 = QRadioButton("Fahrenheit to Kelvin", self.frame1)
        self.rb5.setGeometry(80, 390, 400, 60)
        self.rb5.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.rb6 = QRadioButton("Kelvin to Fahrenheit", self.frame1)
        self.rb6.setGeometry(80, 470, 400, 60)
        self.rb6.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.rb1)
        self.button_group.addButton(self.rb2)
        self.button_group.addButton(self.rb3)
        self.button_group.addButton(self.rb4)
        self.button_group.addButton(self.rb5)
        self.button_group.addButton(self.rb6)
        
        self.entry_label=QLabel("Enter the temperature:",self.frame1)
        self.entry_label.setGeometry(80,530,400,70)
        self.entry_label.setStyleSheet("color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500;")
        self.entry_input=QLineEdit(self.frame1)
        self.entry_input.setGeometry(80,580,400,70)
        self.entry_input.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;border-radius:20px; ")
        self.entry_input.setPlaceholderText("0.00")
        
        self.calculate=QPushButton("Calculate",self.frame1)
        self.calculate.setGeometry(80,660,100,50)
        self.calculate.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#EAB308;")
        self.calculate.clicked.connect(self.calculate_function)
        self.exit=QPushButton("Exit",self.frame1)
        self.exit.setGeometry(365,660,100,50)
        self.exit.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#7C2D12;")
        self.exit.clicked.connect(self.close)
        #self.frame1.hide()
        
        
        # frame2 result
        self.frame2=QFrame(self)
        self.frame2.setGeometry(60, 180, 560, 700)
        self.entry_label=QLabel("Result:",self.frame2)
        self.entry_label.setGeometry(80,50,400,100)
        self.entry_label.setStyleSheet("color:#FFFFFF;font-weight:900;font-size:40px;font-family:Arial;")
        self.result_label=QLabel("",self.frame2)
        self.result_label.setGeometry(95,140,400,80)
        self.result_label.setStyleSheet("color:black;font-weight:700;font-size:25px;font-family:Arial;border:2px solid orange;")

        
        self.home_btn=QPushButton("Home", self.frame2)
        self.home_btn.setGeometry(80,230,80,50)
        self.home_btn.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#EAB308;")
        self.home_btn.clicked.connect(self.home)
        self.exit_btn=QPushButton("Exit", self.frame2)
        self.exit_btn.setGeometry(330,230,80,50)
        self.exit_btn.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#7C2D12;")
        self.exit_btn.clicked.connect(self.close)

        self.frame2.hide()
        
    def calculate_function(self):
        try:     
            if self.entry_input.text()=="":
                QMessageBox.warning(self,"Error","Please enter a temperature")
                return
            input=float(self.entry_input.text())
            if not self.button_group.checkedButton():
                QMessageBox.warning(self,"Error","Please select a conversion type")
                return
            result=0
            if self.rb1.isChecked():
                result=(input*(9/5))+32
                self.result_label.setText(f"{input}°C = {result:.2f}F")
            elif self.rb2.isChecked():
                result=(input-32)*(5/9)
                self.result_label.setText(f"{input}F = {result:.2f}°C")
            elif self.rb3.isChecked():
                result=input+273.15
                if result <0:
                    QMessageBox.warning(self,"Error","Temperature below absolute zero :-273.15°C")
                    return
                self.result_label.setText(f"{input}°C = {result:.2f}K")
            elif self.rb4.isChecked():
                if input<0:
                    QMessageBox.warning(self,"Error","Kelvin can't be Negative")
                    return
                result=input-273.15
                self.result_label.setText(f"{input}k = {result:.2f}°C")
            elif self.rb5.isChecked():
                result=(input-32)*(5/9)+273.15
                if result<0:
                    QMessageBox.warning(self,"Error","Temperature below absolute zero :-273.15°C")
                    return
                self.result_label.setText(f"{input}F = {result:.2f}K")
            elif self.rb6.isChecked():
                if input<0:
                    QMessageBox.warning(self,"Error","Kelvin can't be Negative")
                    return
                result_6=(input-273.15)*(9/5)+32
                self.result_label.setText(f"{input}K = {result_6:.2f}F")
            self.frame1.hide()
            self.frame2.show()
        except ValueError:
            QMessageBox.warning(self,"Error","Enter valid number")
            self.home()
            
            
    def home(self):
        self.button_group.setExclusive(False)
        for rb in [self.rb1,self.rb2,self.rb3,self.rb4,self.rb5,self.rb6]:
            rb.setChecked(False)
        self.button_group.setExclusive(True)
        self.entry_input.clear()
        self.frame1.show()
        self.frame2.hide()
        
def main():
    app=QApplication(sys.argv)
    window=fenêtre()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()