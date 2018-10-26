from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class ortalama(QDialog):
    def __init__(self,ebeveyn=None):
        super(ortalama,self).__init__(ebeveyn)

        grid=QGridLayout()

        grid.addWidget(QLabel("Aylik çalışan sayisi"),0,0)

        self.calisan=QLineEdit()
        grid.addWidget(self.calisan,0,1)
        grid.addWidget(QLabel("ay sayısı"),2,0)

        grid.addWidget(QLabel("ortalama çalışan sayısı:"),3,0)

        self.sonuc=QLabel("")
        grid.addWidget(self.sonuc,3,1)

        self.aysay=QSpinBox()
        self.aysay.setRange(1,10)
        self.aysay.setValue(5)
        grid.addWidget(self.aysay,2,1)

        ortalamhesapla=QPushButton("Hesaplaa")
        grid.addWidget(ortalamhesapla,4,0)
        self.connect(ortalamhesapla,SIGNAL('pressed()'),self.hesapla)

        grid.addWidget(QLabel("İşten Ayrılan Sayısı:"),5,0)
        self.istenayrilan=QLineEdit()
        grid.addWidget(self.istenayrilan,5,1)
        Devirhizi=QPushButton("Devir hızı hesapla")
        grid.addWidget(Devirhizi,6,0)
        self.connect(Devirhizi,SIGNAL('pressed()'),self.devir)

        grid.addWidget(QLabel("devir hızı:"),7,0)
        self.devirrr=QLabel("")
        grid.addWidget(self.devirrr,7,1)
        
        
        
        
        self.setLayout(grid)
        self.setWindowTitle("Personel Devir Hızı")
        self.resize(300,100)

    def hesapla(self):
            calisan=int(self.calisan.text())
            ay=int(self.aysay.text())
            sonucc=calisan/ay
           
            self.sonuc.setText(str(sonucc))
    def devir(self):
            sonuccc=float(self.sonuc.text())
            istenayrilan=int(self.istenayrilan.text())
            devirr=istenayrilan/sonuccc
            self.devirrr.setText(str(devirr))
            
   
    
          
       
uygulama=QApplication([])
pencere=ortalama()
pencere.show()
uygulama.exec_
        
