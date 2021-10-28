
import urllib.request as req
import bs4
# from color import colorprint

import sys
# from mod import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtRemoveInputHook, pyqtSlot

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.year

datelist = []
titlelist = []
linklist = []

ComboBox = {'1月':'Jan', '2月':'Feb', '3月':'Mar', '4月':'Apr','5月':'May','6月':'Jun','7月':'Jul','8月':'Aug','9月':'Sep','10月':'Oct','11月':'Nov','12月':'Dec'}


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(222, 210)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 60, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(110, 90, 101, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("源樣黑體 N")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("源樣黑體 N")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 140, 201, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("源樣黑體 N")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 120, 211, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "模組排行"))
        self.label.setText(_translate("Form", "Addon Top10"))
        self.label_2.setText(_translate("Form", "選擇月份"))
        self.label_3.setText(_translate("Form", "設定數量"))
        self.pushButton.setText(_translate("Form", "確認"))


class Controller(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        choices = ['1月', '2月', '3月', '4月','5月','6月','7月','8月','9月','10月','11月','12月']
        self.comboBox.addItems(choices)

        self.pushButton.clicked.connect(self.start)
        
        # self.sele.clicked.connect(self.selefile)
        self.dfc()
        self.show()

    @pyqtSlot()
    def dfc(self):
        self.spinBox.setValue(10)
    def getData(self,url):
        global datelist,titlelist,linklist
        datelist = []
        titlelist = []
        linklist = []
        request=req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
        })
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")

        root = bs4.BeautifulSoup(data, "html.parser")
        titles=root.find_all("h2",class_="post__title")
        # print(titles)
        times=root.find_all("div",class_="post__date")

        for title in titles:
            modtitle=(title.string.replace("\n", ""))
            titlelist.append(modtitle)
            linklist.append((title.a)["href"])

        for time in times:
            time=(time.string.replace("\n", ""))
            datelist.append(time)

    def start(self):
        MaxMods = self.spinBox.value()

        month = ComboBox[self.comboBox.currentText()]
        mods = 0

        mod = 0

        text = '<!DOCTYPE html><html><head><title>模組排行</title><style>body{background-color:#e2e2e2}a{background-color:#708090;width:auto;padding:10px;margin-right: 10px;text-decoration:none;color:#fff;border-radius:10px;display:inline}a:hover{background-color:#9dacbb}.box { background-color:white; padding-top: 20px; padding-bottom: 20px; padding-left: 10px; border-radius: 10px; margin: 5px; }.titlebox{background-color:#fff;padding:7px;border-radius:10px;margin:5px}.root{margin:20px}.box:hover { background-color:rgb(246, 246, 246); } .titlebox:hover { background-color:rgb(246, 246, 246); }.boxText{font-weight:700}.title{text-align:center;font-size:30px}</style></head><body><div class="root"><div class="titlebox"><h2 class="title">月份MCPEDL熱門排行模組自動抓取</h2></div>'
        while True:
            self.getData("https://mcpedl.com/category/mods/page/"+ str(mod+1) + "/?sort=popular-month")

            for i in range(len(datelist)):
                if (month+", "+str(year) in datelist[i]):
                    text+='<div class="box"><span class="boxText"><a href="'+"https://mcpedl.com"+linklist[i]+'">前往</a>'+"TOP"+str(mods+1)+". "+titlelist[i]+'</span></div>'
                    print("TOP"+str(mods+1)+". "+titlelist[i]+"\n")
                    print("https://mcpedl.com"+linklist[i]+"\n\n")
                    print(mods)
                    mods+=1
                    self.progressBar.setValue(self.progressBar.value()+100//MaxMods)
                    if mods >= MaxMods:
                        break
            mod+=1
            if mods >= MaxMods:
                        break
        self.progressBar.setValue(100)
        self.pushButton.setEnabled(False)
        
        try:
            f = open("mods.html","x", encoding="utf-8")
            f.write(text)
            f.close()
        except:
            f = open("mods.html","w", encoding="utf-8")
            f.write(text)
            f.close()



            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controller()
    sys.exit(app.exec_())
