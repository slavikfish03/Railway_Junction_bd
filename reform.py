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
        Dialog.resize(760, 405)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: black;\n"
"	background-color: white;\n"
"	font-family: Arial;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
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
        self.verticalLayoutWidget.setGeometry(QRect(39, 260, 691, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_add_w = QPushButton(self.verticalLayoutWidget)
        self.btn_add_w.setObjectName(u"btn_add_w")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_w.sizePolicy().hasHeightForWidth())
        self.btn_add_w.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_add_w)

        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(39, 29, 691, 211))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.verticalLayoutWidget_3)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setStyleSheet(u"color: rgb(26,26,226)")

        self.verticalLayout_3.addWidget(self.lbl_title)

        self.lbl_track = QLabel(self.verticalLayoutWidget_3)
        self.lbl_track.setObjectName(u"lbl_track")

        self.verticalLayout_3.addWidget(self.lbl_track)

        self.lbl_wag = QLabel(self.verticalLayoutWidget_3)
        self.lbl_wag.setObjectName(u"lbl_wag")

        self.verticalLayout_3.addWidget(self.lbl_wag)

        self.lbl_weight = QLabel(self.verticalLayoutWidget_3)
        self.lbl_weight.setObjectName(u"lbl_weight")

        self.verticalLayout_3.addWidget(self.lbl_weight)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_add_w.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u0430\u0433\u043e\u043d\u044b", None))
        self.lbl_title.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a\u041d\u041e \u0424\u041e\u0420\u041c\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u042f \u041f\u041e\u0415\u0417\u0414\u0410", None))
        self.lbl_track.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0433\u043e\u043d:", None))
        self.lbl_wag.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u043a\u043e\u043b-\u0432\u043e \u0432\u0430\u0433\u043e\u043d\u043e\u0432: ", None))
        self.lbl_weight.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043c\u0430\u0441\u0441\u0430: ", None))
    # retranslateUi

