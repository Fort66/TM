from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import mainForm, dialogFormTask, dialogTaskWindow, dialogFormFinance, dialogFinanceWindow

def AddRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.dateEditTask.setDate(QDate.currentDate())
        dialogFormTask.timeEditStart.setTime(QtCore.QTime.currentTime())
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Добавление записи в базу"))
        dialogTaskWindow.show()
     
    elif mainForm.tabWidget.currentIndex() == 1:
        dialogFormFinance.dateEditFinance.setDate(QDate.currentDate())
        dialogFinanceWindow.show()

def DelRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Удаление записи из базы"))
        dialogTaskWindow.show()

    elif mainForm.tabWidget.currentIndex() == 1:
        dialogFormFinance.CaptionLabel.setText(_translate("DialogFormFinance", "Удаление записи из базы"))
        dialogFinanceWindow.show()

def EditRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate("DialogFormTask", "Изменение записи в базе"))
        dialogTaskWindow.show()

    elif mainForm.tabWidget.currentIndex() == 1:
        dialogFormFinance.CaptionLabel.setText(_translate("DialogFormFinance", "Изменение записи в базе"))
        dialogFinanceWindow.show()

