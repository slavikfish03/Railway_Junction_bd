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
        Dialog.resize(678, 342)
        Dialog.setStyleSheet(u"QWidget {\n"
                             "	color: black;\n"
                             "	background-color: white;\n"
                             "	font-family: Arial;\n"
                             "	font-size: 16pt;\n"
                             "	font-weight: 600;\n"
                             "}\n"
                             "\n"
                          "QPushButton {"
"	border-top: 1px solid black;"
"	border-bottom: 1px solid black;"
"	border-right: 1px solid black;"
"	border-left: 1px solid black;"
"   width: 70px;"
                                 "height: 40px;" 
"}"

"QPushButton:hover {\n"
"	background-color: rgb(26, 26, 226);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}\n"
"")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(149, 49, 422, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(154, 270, 411, 20))
        self.label_2.setStyleSheet(u"font-size: 8pt;\n"
"font-weight: normal;\n"
"color: red")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b \u0441 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u043c \u043f\u043e\u0435\u0437\u0434\u0430:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 txt", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u041d\u0418\u041c\u0410\u041d\u0418\u0415! \u041f\u0420\u041e\u0412\u0415\u0420\u042f\u0419\u0422\u0415 \u041a\u041e\u0420\u0420\u0415\u041a\u0422\u041d\u041e\u0421\u0422\u042c \u0417\u0410\u0413\u0420\u0423\u0416\u0415\u041d\u041d\u042b\u0425 \u0424\u0410\u0419\u041b\u041e\u0412", None))
    # retranslateUi

