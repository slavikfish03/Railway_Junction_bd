from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 406)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: black;\n"
"	background-color: white;\n"
"	font-family: Arial;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {"
"	border-top: none;"
"	border-bottom: none;"
"	border-right: none;"
"	border-left: none;"
"   width: 70px;"
                                 "height: 40px;" 
"}"

"QPushButton:hover {\n"
"	background-color: rgb(26, 26, 226);\n"
"	color: white;\n"
"	border-top: 0.5px solid black;"
"	border-bottom: 0.5px solid black;"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        #self.label_2 = QLabel(self.centralwidget)
        #self.label_2.setObjectName(u"label_2")
        #self.label_2.setPixmap(QPixmap(u":/icons/logo.png"))
        #self.label_2.setAlignment(Qt.AlignCenter)

        #self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bnt_train_reception = QPushButton(self.centralwidget)
        self.bnt_train_reception.setObjectName(u"bnt_train_reception")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bnt_train_reception.sizePolicy().hasHeightForWidth())
        self.bnt_train_reception.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.bnt_train_reception)

        self.btn_reformation_train = QPushButton(self.centralwidget)
        self.btn_reformation_train.setObjectName(u"btn_reformation_train")
        sizePolicy.setHeightForWidth(self.btn_reformation_train.sizePolicy().hasHeightForWidth())
        self.btn_reformation_train.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_reformation_train)

        self.btn_sending_train = QPushButton(self.centralwidget)
        self.btn_sending_train.setObjectName(u"btn_sending_train")
        sizePolicy.setHeightForWidth(self.btn_sending_train.sizePolicy().hasHeightForWidth())
        self.btn_sending_train.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_sending_train)

        self.btn_create_rep_tr = QPushButton(self.centralwidget)
        self.btn_create_rep_tr.setObjectName(u"btn_create_rep_tr")
        sizePolicy.setHeightForWidth(self.btn_create_rep_tr.sizePolicy().hasHeightForWidth())
        self.btn_create_rep_tr.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_create_rep_tr)

        self.btn_reports = QPushButton(self.centralwidget)
        self.btn_reports.setObjectName(u"btn_reports")
        sizePolicy.setHeightForWidth(self.btn_reports.sizePolicy().hasHeightForWidth())
        self.btn_reports.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_reports)

        self.lbl_warning_form = QLabel(self.centralwidget)
        self.lbl_warning_form.setObjectName(u"lbl_warning_form")
        self.lbl_warning_form.setStyleSheet(u"color: rgb(26,26,226);\n"
"font-size: 12pt")

        self.verticalLayout.addWidget(self.lbl_warning_form)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Railway Junction", None))
        #self.label_2.setText("")
        self.bnt_train_reception.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0435\u043c \u043f\u043e\u0435\u0437\u0434\u0430", None))
        self.btn_reformation_train.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0438\u043d\u044f\u0442\u043e\u0433\u043e \u043f\u043e\u0435\u0437\u0434\u0430", None))
        self.btn_sending_train.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u043e\u0435\u0437\u0434\u0430", None))
        self.btn_create_rep_tr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0438\u0441\u044c\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u0442\u0447\u0435\u0442\u0430 \u043e\u0431 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u043e\u043c \u043f\u043e\u0435\u0437\u0434\u0435", None))
        self.btn_reports.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442\u044b", None))
        self.lbl_warning_form.setText("")
    # retranslateUi

