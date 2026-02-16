# WAV generation logic adapted from Alessandro Cudazzo's MIT-licensed sine_wave.py
# https://gist.github.com/alessandrocuda/9df6043b79e68e3ddc1c262eddcfa015

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QFormLayout, QSpinBox, QLineEdit
from PyQt6 import QtGui
import sys, math, wave, struct, os
from interface_gen import Ui_MainWindow


directory = os.getcwd()


class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.btnBrowse2.clicked.connect(self.wave_gen)
        self.setWindowIcon(QtGui.QIcon('Soundwave.ico'))
        self.show()

    def browse_folder(self):
        
        global directory
        directory = QFileDialog.getExistingDirectory(self, "Pick a folder")
        if directory:
            self.listWidget.clear()
            
            self.listWidget.addItem('[+] Selected folder is: '+directory)
         
        
    def wave_gen(self):
        correctValue = True
        try:
            self.listWidget.addItem("[+] Full path: "+str(directory)+"\n")  
            self.listWidget.addItem("[+] SAMPLE RATE is: " +self.lineOne.text())
            self.listWidget.addItem("[+] Number of seconds is: " +self.lineTwo.text())
            self.listWidget.addItem("[+] Frequency is: " +self.lineThree.text())
            self.listWidget.addItem("[+] Volume is: " +self.lineFour.text()+"\n")
            
            SAMPLE_RATE = float(self.lineOne.text())	
            NUM_SECONDS = float(self.lineTwo.text())
            FREQUENCY =  float(self.lineThree.text())       
            VOLUME = float(self.lineFour.text())*100
            OUTPUT_FILE = self.lineFive.text()
            
        except Exception as e:
            self.listWidget.addItem("[!] Something Got Wrong:")
            if "directory" in str(e):
                self.listWidget.addItem("[!] Please chose directory")
            else:
                self.listWidget.addItem("[!] "+str(e))
        try:
            if NUM_SECONDS <= 0.0:
                self.listWidget.addItem('[!] Duration must be higher than 0 seconds.')
                correctValue = False
            if FREQUENCY < 0.0 or FREQUENCY > 20000.0:
                self.listWidget.addItem('[!] Wave frequency must be positive and lesser than 20000 Hz.')
                correctValue = False
            if VOLUME < 100.0 or VOLUME > 1000.0:
                self.listWidget.addItem('[!] Volume must be higher than 0 and lesser than 100.')
                correctValue = False

            if correctValue:

                path = os.path.join(directory, OUTPUT_FILE+".wav")  

                file = wave.open(path,'wb')
                file.setnchannels(1)
                file.setsampwidth(2) 
                file.setframerate(SAMPLE_RATE)

                for i in range(int(NUM_SECONDS * SAMPLE_RATE)):
                
	                value = int(VOLUME * math.sin(2 * FREQUENCY * math.pi * float(i) / float(SAMPLE_RATE)))
	                data = struct.pack('<h', value)
	                file.writeframesraw(data)
	            
                file.close()
                self.listWidget.addItem("[+] File was saved at: "+directory)
            
        except Exception as e:
            self.listWidget.addItem("[+] Exception Occured!")

        
        self.lineOne.setText("SAMPLE RATE (Example: 44100)")
        self.lineTwo.setText("NUMBER OF SECONDS (Must be > 0)")
        self.lineThree.setText("FREQUENCY IN HZ (range 1...20000Hz)")
        self.lineFour.setText("VOLUME (Float value between 1.0 and 10.0)")


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    form = ExampleApp()
    sys.exit(qApp.exec())
