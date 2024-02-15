from formcreator import mainForm
from PyQt5.QtCore import QDate

def CheckBoxClick():
    if mainForm.checkBoxFilterDate.isChecked():
        mainForm.dateEditIn.setDate(QDate.currentDate())
        mainForm.dateEditOut.setDate(QDate.currentDate())
        mainForm.dateEditOut.setEnabled(True)
        mainForm.dateEditIn.setEnabled(True)
        mainForm.ButtonFilter.setEnabled(True)
    else:
        mainForm.dateEditOut.setEnabled(False)
        mainForm.dateEditIn.setEnabled(False)
        mainForm.ButtonFilter.setEnabled(False)
