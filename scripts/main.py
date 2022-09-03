import os
import time
from colorama import Fore, Back, Style
from colorama.ansi import code_to_chars
import colorama
import cv2
import dlib
import numpy as np
from datetime import datetime
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QMessageBox, QVBoxLayout, QLabel, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import *
from tkinter import *
import regex
from PIL import Image, ImageTk

colorama.init()
os.system('cls')

print(f"\n{Fore.CYAN}-------------------- Sheriff - Console --------------------{Fore.WHITE}")

carCascade = cv2.CascadeClassifier('data/HaarCascadeClassifier.xml')

WIDTH = 1280 #WIDTH OF VIDEO FRAME
HEIGHT = 720 #HEIGHT OF VIDEO FRAME
cropBegin = 240 #CROP VIDEO FRAME FROM THIS POINT
mark1 = 120 #MARK TO START TIMER
mark2 = 360 #MARK TO END TIMER
markGap = 15 #DISTANCE IN METRES BETWEEN THE MARKERS
fpsFactor = 3 #TO COMPENSATE FOR SLOW PROCESSING
startTracker = {} #STORE STARTING TIME OF CARS
endTracker = {} #STORE ENDING TIME OF CARS

if not os.path.exists('overspeeding/cars/'):
    os.makedirs('overspeeding/cars/')

class Ui_MainWindow(QMainWindow, object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 800)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(33, 33, 33, 255), stop:0.548023 rgba(15, 15, 15, 255));")
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 630, 271, 111))
        font = QtGui.QFont()
        font.setFamily("Keep Calm")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefiles)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 50, 581, 151))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 0, 151, 151))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/logo.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.setMargin(17)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 521, 101))
        font = QtGui.QFont()
        font.setFamily("Keep Calm")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(51, 51, 51);")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 430, 721, 111))
        font = QtGui.QFont()
        font.setFamily("Keep Calm")
        font.setPointSize(36)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"border-radius:15px;\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"QTextEdit:hover{\n"
"background-color:rgb(213, 213, 213);\n"
"}")
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 280, 591, 131))
        font = QtGui.QFont()
        font.setFamily("Keep Calm")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setToolTipDuration(12)
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sheriff - Home"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.label_2.setText(_translate("MainWindow", "SHERIFF"))
        self.label_3.setText(_translate("MainWindow", "ENTER SPEED LIMIT"))
    
    def browsefiles(self):
        global fname
        global speedlimit
        fileFilter = 'MP4 files (*.mp4);; MOV files (*.mov);; WMV files (*.wmv);; AVI files (*.avi);; MKV files (*.mkv);; All files (*.*)'
        filename = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open File', filter=fileFilter, initialFilter='MP4 files (*.mp4)')
        speedlimit = self.textEdit.toPlainText()
        fname = str(filename[0])
        trackMultipleObjects()


def blackout(image):
    xBlack = 360
    yBlack = 300
    triangle_cnt = np.array( [[0,0], [xBlack,0], [0,yBlack]] )
    triangle_cnt2 = np.array( [[WIDTH,0], [WIDTH-xBlack,0], [WIDTH,yBlack]] )
    cv2.drawContours(image, [triangle_cnt], 0, (0,0,0), -1)
    cv2.drawContours(image, [triangle_cnt2], 0, (0,0,0), -1)

    return image

def saveReport(speed,id,speedlimit):
    try:
        reportFile = open('overspeeding/report.log','a')
    except FileExistsError as e:
        os.remove('overspeeding/report.log')
        reportFile = open('overspeeding/report.log','a')
    now = datetime.today().now()
    if speed > int(speedlimit):
        reportLine = now.strftime("%d/%m/%Y\t%H:%M:%S") + f"\tID-{id}\tSPEED-{speed}kmph OVERSPEED\n"
        reportFile.write(reportLine)
    if speed < int(speedlimit):
        reportLine = now.strftime("%d/%m/%Y\t%H:%M:%S") + f"\tID-{id}\tSPEED-{speed}kmph UNDERSPEED\n"
        reportFile.write(reportLine)

def saveCar(speed,image,id):
    now = datetime.today().now()
    nameCurTime = now.strftime("%d-%m-%Y-%H-%M-%S")
    finalName = nameCurTime + f"-{speed}-{id}"

    link = 'overspeeding/cars/'+finalName+'.jpeg'
    cv2.imwrite(link,image)

#FUNCTION TO CALCULATE SPEED----------------------------------------------------
def estimateSpeed(carID):
    timeDiff = endTracker[carID]-startTracker[carID]
    speed = round(markGap/timeDiff*fpsFactor*3.6,2)
    return speed

class trackMultipleObjects(Ui_MainWindow,QMainWindow):
    def __init__(self):
        global root
        super(Ui_MainWindow,self).__init__()
        # loadUi('scripts/app.ui',self)
        speedLimit = speedlimit
        if speedLimit == '':
            print(f"{Fore.RED}\nPlease Enter Speed Limit!{Fore.WHITE}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error : Please Enter Speed Limit")
            msg.setWindowTitle("Sheriff - Error")
            msg.exec_()
            Ui_MainWindow()
        elif regex.search('[a-zA-Z]', speedLimit):
            print(f"{Fore.RED}\nPlease Enter Valid Speed Limit!{Fore.WHITE}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error : Please Enter Valid Speed Limit")
            msg.setWindowTitle("Sheriff - Error")
            msg.exec_()
            Ui_MainWindow()
        elif fname == '':
            print(f"{Fore.RED}\nPlease Select a File!{Fore.WHITE}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error : Please select a file")
            msg.setWindowTitle("Sheriff - Error")
            msg.exec_()
            Ui_MainWindow()
        elif fname.endswith(".mp4") or fname.endswith(".mov") or fname.endswith(".wmv") or fname.endswith(".avi") or fname.endswith(".mkv"):
            print(f"\n{Fore.GREEN}Video File selected - {Fore.YELLOW}{fname}")
            video = cv2.VideoCapture(f'{fname}')
            print(f'\n{Fore.GREEN}Speed Limit Set at : {Fore.YELLOW}{speedLimit} Kmph\n{Fore.WHITE}\n')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error : Please select a Valid File!")
            msg.setWindowTitle("Sheriff - Error")
            msg.exec_()
            print(f"{Fore.RED}Invalid File Selected!{Fore.WHITE}")
            Ui_MainWindow()
        root = Tk()
        root.geometry("1400x800")
        root.resizable(0,0)
        root.iconbitmap("res/logo.ico")
        bg = PhotoImage(file = "res/bg.png")
        BackgroundLabel = Label( root, image = bg,bd=0)
        BackgroundLabel.place(x = 0, y = 0)
        feedLabel = Label(root, bg="black")
        feedLabel.place(x=50,y=250)
        
        rectangleColor = (0, 255, 0)
        frameCounter = 0
        currentCarID = 0
        carTracker = {}
        while True:
            rc, image = video.read()
            if type(image) == type(None):
                break
            frameTime = time.time()
            image = cv2.resize(image, (WIDTH, HEIGHT))[cropBegin:720,0:1280]
            resultImage = blackout(image)
            cv2.line(resultImage,(0,mark1),(1280,mark1),(0,0,255),2)
            cv2.line(resultImage,(0,mark2),(1280,mark2),(0,0,255),2)
            frameCounter = frameCounter + 1
            carIDtoDelete = []
            for carID in carTracker.keys():
                trackingQuality = carTracker[carID].update(image)
                if trackingQuality < 7:
                    carIDtoDelete.append(carID)
            for carID in carIDtoDelete:
                carTracker.pop(carID, None)
            #MAIN PROGRAM-----------------------------------------------------------
            if (frameCounter%60 == 0):
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cars = carCascade.detectMultiScale(gray, 1.1, 13, 18, (24, 24)) #DETECT CARS IN FRAME
                for (_x, _y, _w, _h) in cars:
                    #GET POSITION OF A CAR
                    x = int(_x)
                    y = int(_y)
                    w = int(_w)
                    h = int(_h)
                    xbar = x + 0.5*w
                    ybar = y + 0.5*h
                    matchCarID = None
                    #IF CENTROID OF CURRENT CAR NEAR THE CENTROID OF ANOTHER CAR IN PREVIOUS FRAME THEN THEY ARE THE SAME
                    for carID in carTracker.keys():
                        trackedPosition = carTracker[carID].get_position()
                        tx = int(trackedPosition.left())
                        ty = int(trackedPosition.top())
                        tw = int(trackedPosition.width())
                        th = int(trackedPosition.height())
                        txbar = tx + 0.5 * tw
                        tybar = ty + 0.5 * th
                        if ((tx <= xbar <= (tx + tw)) and (ty <= ybar <= (ty + th)) and (x <= txbar <= (x + w)) and (y <= tybar <= (y + h))):
                            matchCarID = carID
                    if matchCarID is None:
                        tracker = dlib.correlation_tracker()
                        tracker.start_track(image, dlib.rectangle(x, y, x + w, y + h))
                        carTracker[currentCarID] = tracker
                        currentCarID = currentCarID + 1
            for carID in carTracker.keys():
                trackedPosition = carTracker[carID].get_position()
                tx = int(trackedPosition.left())
                ty = int(trackedPosition.top())
                tw = int(trackedPosition.width())
                th = int(trackedPosition.height())
                #PUT BOUNDING BOXES-------------------------------------------------
                cv2.rectangle(resultImage, (tx, ty), (tx + tw, ty + th), rectangleColor, 2)
                cv2.putText(resultImage, str(carID), (tx,ty-5), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)
                #ESTIMATE SPEED-----------------------------------------------------
                if carID not in startTracker and mark2 > ty+th > mark1 and ty < mark1:
                    startTracker[carID] = frameTime
                elif carID in startTracker and carID not in endTracker and mark2 < ty+th:
                    endTracker[carID] = frameTime
                    speed = estimateSpeed(carID)
                    if speed > int(speedLimit):
                        print(f'{Fore.BLUE}CAR-ID : {carID} - {Fore.YELLOW}{speed} kmph - {Fore.RED}OVERSPEED{Fore.RESET}\n')
                        saveCar(speed,image[ty:ty+th, tx:tx+tw],carID)
                        saveReport(speed, carID, speedLimit)
                    else:
                        print(f'{Fore.BLUE}CAR-ID : {carID} - {Fore.YELLOW}{speed} kmph - {Fore.GREEN}UNDERSPEED{Fore.RESET}\n')
                        saveReport(speed, carID, speedLimit)
            img = ImageTk.PhotoImage(Image.fromarray(image))
            feedLabel['image'] = img
            root.title(f"Sheriff - {fname}")
            root.update()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

root.mainloop()