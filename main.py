from formcreator import mainForm, dialogFormTask, dialogFormFinance, app

from Flags import Flags
from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick
from MainForm.onClickCalendar import onClickCalendar
from MainForm.CheckBoxClick import CheckBoxClick
from DialogFormTask.DialogFormTaskClose import dialogFormTaskClose
from DialogFormFinance.DialogFormFinanceClose import dialogFormFinanceClose
from MainForm.DatePeriod import SetDateIn, SetDateOut

flag = Flags()


mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)
mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(CheckBoxClick)
mainForm.dateEditIn.dateChanged.connect(SetDateIn)
mainForm.dateEditOut.dateChanged.connect(SetDateOut)


dialogFormTask.ButtonCancel.clicked.connect(dialogFormTaskClose)
dialogFormFinance.ButtonCancel.clicked.connect(dialogFormFinanceClose)

#select из Finance

app.exec()