from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(557, 401)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: black;\n"
"	background-color: white;\n"
"	font-family: Arial;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
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
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(29, 29, 491, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: rgb(26, 26, 226)")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0422\u0427\u0401\u0422\u042b", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u043c\u044b\u0435 \u043f\u043e\u0435\u0437\u0434\u0430 \u043d\u0430 \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u0434\u0430\u0442\u0443", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0424\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u043c\u044b\u0435 \u043f\u043e\u0435\u0437\u0434\u0430 \u043d\u0430 \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u0434\u0430\u0442\u0443", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0443\u0437\u043e\u043e\u0431\u043e\u0440\u043e\u0442 \u0441\u0442\u0430\u043d\u0446\u0438\u0438 \u0437\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Эффективность станции", None))
    # retranslateUi

