from BrainDetectFunction import BrainDetectFunction
from mainwindow import MainScreen
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from tkinter import *
from tkinter import filedialog
import time
import os

class Main:

    def Initial(self):

        global mtrainingMode
        global mDetectMode       
        global selectMode    
    
        mtrainingMode=1
        mDetectMode=0        
        selectMode=mtrainingMode          
        
    def Main(self):
        print("Main Funtion class Main")    
        app = QApplication(sys.argv) # 
        global mMainScreen
        global mBrainDetectFunction     
        mMainScreen = MainScreen()
        mMainScreen.show()			
        mMainScreen.ui.label_NotifyStatus.setText( "While training data, please wait until finished")  
        mBrainDetectFunction=BrainDetectFunction()
        mMainScreen.ui.label_NotifyStatus.setText("The training process has been completed, choose a photo to segmentation")        
        mMainScreen.ui.pushButton_OpenFileBroswer.clicked.connect(self.FileBroswer)          
        mMainScreen.ui.pushButton_segmentation.clicked.connect(self.DetectObject)      #  
        mMainScreen.ui.pushButton_trainingData.clicked.connect(self.TrainingData)      #  
        mMainScreen.ui.radioButtonDetectedMode.clicked.connect(self.SetDetectMode)
        mMainScreen.ui.radioButton_trainingMode.clicked.connect(self.SetModeTraining)
        mMainScreen.ui.radioButtonDetectedMode.setChecked(True)       
        mMainScreen.ui.pushButton_trainingData.setEnabled(False)
        sys.exit(app.exec_())

    def FileBroswer(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        print("FileBroswer mclass_names class Main")
        global filename          
        currdir=os.getcwd()
        root =Tk()        
        if mMainScreen.ui.radioButton_trainingMode.isChecked():
            filename = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')            
            print("selectMode = trainingMode") 
            mBrainDetectFunction.SetDataPath(filename)                    
        else:
            print("selectMode = mDetectMode") 
            filename = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
           
        mMainScreen.ui.lineEdit_FolderPath.setText(filename) 
        
        root.destroy()
        print(filename)
        return filename   
    
    def SetModeTraining(self):
        print("SetModeTraining Funtion class Main")
        selectMode=mtrainingMode
        print("selectMode =",selectMode)     
        mMainScreen.ui.label_NotifyStatus.setText( "Training data mode")                              
        mMainScreen.ui.pushButton_trainingData.setText("Training Data")             
        mMainScreen.ui.radioButtonDetectedMode.setChecked(False)
        mMainScreen.ui.radioButton_trainingMode.setChecked(True)
        mMainScreen.ui.pushButton_segmentation.setEnabled(False)        
        mMainScreen.ui.pushButton_trainingData.setEnabled(True)        
        
    def SetDetectMode(self):
        print("SetDetectMode Funtion class Main")
        selectMode=mDetectMode
        print("selectMode =",selectMode)
        mMainScreen.ui.label_NotifyStatus.setText( "Detect Object mode")                  
        mMainScreen.ui.radioButtonDetectedMode.setChecked(True)
        mMainScreen.ui.radioButton_trainingMode.setChecked(False)        
        mMainScreen.ui.pushButton_segmentation.setEnabled(True)        
        mMainScreen.ui.pushButton_trainingData.setEnabled(False)
        
    def DetectObject(self):
        print("DetectObject Funtion class Main")
        print("selectMode =",selectMode)    
        if mMainScreen.ui.radioButtonDetectedMode.isChecked():
            print("selectMode is DetectMode")  
            filename= mMainScreen.ui.lineEdit_FolderPath.text()
            if filename:
                statusPath=mBrainDetectFunction.DetectSpecialImage(filename)    
                if not statusPath:
                    mMainScreen.ui.label_NotifyStatus.setText("Model file exit, please insert them to folder data/output/, with name BrainDetectModel.h5")                            
                
    def TrainingData(seft): 
        print("DetectObject Funtion class Main")
        print("selectMode =",selectMode)                
        if mMainScreen.ui.radioButton_trainingMode.isChecked():
            print("selectMode is trainingMode")  
            mMainScreen.ui.label_NotifyStatus.setText( "While training data, please wait until finished")  
            mMainScreen.ui.pushButton_trainingData.setText("Started Training")   
            time.sleep(3) # Delay for 5 seconds.             
            mBrainDetectFunction.BrainDetectFunction()                
            mMainScreen.ui.pushButton_trainingData.setText("Stoped Training")                      
            mMainScreen.ui.label_NotifyStatus.setText("The training process has been completed, choose a photo to segmentation")          
if __name__ == "__main__":    
    main=Main()
    main.Initial()
    main.Main()
