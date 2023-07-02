import psycopg2
import sys
import pathlib
import re
import func_database
import networkx as nx
import matplotlib.pyplot as plt
import datetime
import os
import os.path

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, \
    QDialog, QMessageBox, QFileDialog, QInputDialog, QDateEdit
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt, QDate, QTimer

from design import Ui_MainWindow
from reception import Ui_Dialog as Ui_ReceptionWindow
from reform import Ui_Dialog as Ui_ReformWindow
from sent import Ui_Dialog as Ui_SentWindow
from reports import Ui_Dialog as Ui_ReportsWindow

current_date = None  # текущая дата
number_our_station = None  # технический номер станции местонахождения сотрудника
numbers_tracks = None  # количество доступных для формирования перегонов
neighbours = None  # технические номера станций-соседей
neighbour_stations = None  # таблица (пункт назначения, сосед)


def plot_network_stations(graph: nx.Graph()):
    """
    Функция, строящая сеть станций по графу

    :param graph: граф станций
    """
    options = {
        'node_color': 'yellow',
        'node_size': 850,
        'width': 0.3
    }
    pos = nx.spring_layout(Graph_for_user)
    nx.draw(graph, pos, with_labels=True, **options)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=True)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()


class DateRangeSelector(QMainWindow):
    """
    Класс окна выбора произвольного периода для грузооборота

    Методы:
    get_dates: получает две даты и вычисляет грузооборот станции за этот период
    """

    def __init__(self):
        super().__init__()

        ident = QFontDatabase.addApplicationFont("Arial.ttf")
        if ident < 0:
            print("Error")
        families = QFontDatabase.applicationFontFamilies(ident)
        self.setFont(QFont(families[0], 80))
        self.setStyleSheet('QWidget {color: black;background-color: white;font-size: 16pt;font-family: Arial;'
                           'font-weight: 600;} QPushButton:hover {background-color: rgb(26, 26, 226);'
                           'color: white;}QPushButton:pressed {background-color: #888;}')

        self.setWindowTitle('Выбор периода грузооборота')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        start_label = QLabel('Дата начала грузооборота: ')
        layout.addWidget(start_label)

        self.start_date_edit = QDateEdit(QDate.currentDate())
        layout.addWidget(self.start_date_edit)

        end_label = QLabel('Дата конца грузооборота: ')
        layout.addWidget(end_label)

        self.end_date_edit = QDateEdit(QDate.currentDate())
        layout.addWidget(self.end_date_edit)

        submit_button = QPushButton('Выбрать')
        submit_button.clicked.connect(self.get_dates)
        layout.addWidget(submit_button)

    def get_dates(self):
        start_date = self.start_date_edit.date().toString('yyyy-MM-dd')
        end_date = self.end_date_edit.date().toString('yyyy-MM-dd')

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True

        cargo_dictionary = {
            'Насыпные': 0,
            'Штучные': 0,
            'Наливные': 0,
            'Взрывоопасные': 0,
            'Провизия': 0
        }

        cursor.execute(f"SELECT wagon_cargo_category, wagon_net FROM reception_wagons WHERE (recept_w_arrival_date"
                       f" BETWEEN '{start_date}' AND '{end_date}')")
        reception_cargo = cursor.fetchall()

        for wagon_cargo in reception_cargo:
            match wagon_cargo[0]:
                case "'Насыпные'":
                    cargo_dictionary['Насыпные'] = cargo_dictionary['Насыпные'] + wagon_cargo[1]
                case "'Штучные'":
                    cargo_dictionary['Штучные'] = cargo_dictionary['Штучные'] + wagon_cargo[1]
                case "'Наливные'":
                    cargo_dictionary['Наливные'] = cargo_dictionary['Наливные'] + wagon_cargo[1]
                case "'Взрывоопасные'":
                    cargo_dictionary['Взрывоопасные'] = cargo_dictionary['Взрывоопасные'] + wagon_cargo[1]
                case "'Провизия'":
                    cargo_dictionary['Провизия'] = cargo_dictionary['Провизия'] + wagon_cargo[1]
                case _:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("ОШИБКА ДАННЫХ")
                    msg.setInformativeText("Один из принятых вагонов имеет категорию груза, не входящую в документацию")
                    msg.setWindowTitle("Ошибка")
                    msg.exec_()
                    return

        cursor.execute(f"SELECT sent_w_cargo_category, sent_w_net FROM sent_wagons WHERE (sent_w_departure_date"
                       f" BETWEEN '{start_date}' AND '{end_date}')")
        sent_cargo = cursor.fetchall()

        for wagon_cargo in sent_cargo:
            match wagon_cargo[0]:
                case "'Насыпные'":
                    cargo_dictionary['Насыпные'] = cargo_dictionary['Насыпные'] + wagon_cargo[1]
                case "'Штучные'":
                    cargo_dictionary['Штучные'] = cargo_dictionary['Штучные'] + wagon_cargo[1]
                case "'Наливные'":
                    cargo_dictionary['Наливные'] = cargo_dictionary['Наливные'] + wagon_cargo[1]
                case "'Взрывоопасные'":
                    cargo_dictionary['Взрывоопасные'] = cargo_dictionary['Взрывоопасные'] + wagon_cargo[1]
                case "'Провизия'":
                    cargo_dictionary['Провизия'] = cargo_dictionary['Провизия'] + wagon_cargo[1]
                case _:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("ОШИБКА ДАННЫХ")
                    msg.setInformativeText("Один из отправленных вагонов имеет категорию груза,"
                                           " не входящую в документацию")
                    msg.setWindowTitle("Ошибка")
                    msg.exec_()
                    return

        cargo_turnover_file = f'cargo_turnover_between_{start_date}_and_{end_date}.txt'
        title_list = ['Насыпные', 'Штучные', 'Наливные', 'Взрывоопасные', 'Провизия']

        i = 1
        while os.path.exists(cargo_turnover_file):
            cargo_turnover_file = f'cargo_turnover_between_{start_date}_and_{end_date} ({i}).txt'
            i += 1

        with open(cargo_turnover_file, 'w') as report:
            report.write(f'ГРУЗООБОРОТ СТАНЦИИ С {start_date} ПО {end_date} В ТОННАХ\n\n')
            report.write('{:^20s}{:^15s}{:^15s}{:^15s}{:^15s}\n'.format(title_list[0], title_list[1], title_list[2],
                                                                        title_list[3], title_list[4]))

            report.write('{:^20d}{:^15d}{:^15d}{:^15d}{:^15d}\n'.format(cargo_dictionary['Насыпные'],
                                                                        cargo_dictionary['Штучные'],
                                                                        cargo_dictionary['Наливные'],
                                                                        cargo_dictionary['Взрывоопасные'],
                                                                        cargo_dictionary['Провизия']))

        os.startfile(cargo_turnover_file)

        connection.commit()
        cursor.close()
        connection.close()


class RailwayJunction(QMainWindow):
    """
    Класс основного окна приложения.

    Методы:
    update_lbl_warning: обновляет уведомление об сформированном, но не отправленном поезде
    open_reception_window: открывает окно приема поезда
    open_reform_window: открывает окно формирования поезда
    open_sent_window: открывает окно отправки поезда
    report_sent_train: формирует отчет об отправленном поезде
    open_reports_window: открывает окно с отчётами
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        id = QFontDatabase.addApplicationFont("Arial.ttf")
        if id < 0:
            print("Error")
        families = QFontDatabase.applicationFontFamilies(id)
        self.setFont(QFont(families[0], 80))

        self.ui.bnt_train_reception.clicked.connect(self.open_reception_window)
        self.ui.btn_reformation_train.clicked.connect(self.open_reform_window)
        self.ui.btn_sending_train.clicked.connect(self.open_sent_window)
        self.ui.btn_create_rep_tr.clicked.connect(self.report_sent_train)
        self.ui.btn_reports.clicked.connect(self.open_reports_window)
        self.ui.lbl_warning_form.setText('')
        self.ui.lbl_warning_form.setAlignment(QtCore.Qt.AlignCenter)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_lbl_warning_from)
        self.timer.start()

    def update_lbl_warning_from(self):
        """
        Функция обновляет в нижней части главного окна приложения предупреждение о
        сформированном, но не отправленном поезде
        """

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True

        cursor.execute("SELECT * FROM form_trains WHERE isReady = True")
        if cursor.fetchone() is None:
            self.ui.lbl_warning_form.setText("")
        else:
            self.ui.lbl_warning_form.setText("ВНИМАНИЕ! У ВАС СФОРМИРОВАН, НО НЕ ОТПРАВЛЕН ПОЕЗД!")

        self.ui.lbl_warning_form.repaint()
        connection.commit()
        cursor.close()
        connection.close()

    def open_reception_window(self):
        """
        Функция для открытия окна приема поезда
        """

        reception_window = ReceptionWindow()
        reception_window.exec()

    def open_reform_window(self):
        """
        Функция для открытия окна формирования поезда
        """

        name_our_track, isOktrack = QInputDialog.getItem(window, 'Выбор пути',
                                                         'Укажите станцию, на пути к которой хотите формировать поезд',
                                                         available_tracks_for_user)
        for element in stations_list:
            if element[1] == name_our_track:
                number_current_track = element[0]

        if isOktrack:
            reform_window = ReformWindow(number_current_track, name_our_track)
            reform_window.exec()

    def open_sent_window(self):
        """
        Функция для открытия окна отправления поезда
        """

        name_our_track, isOktrack = QInputDialog.getItem(window, 'Выбор пути',
                                                         'Укажите станцию, к которой хотите отправить поезд',
                                                         available_tracks_for_user)
        for element in stations_list:
            if element[1] == name_our_track:
                number_current_track = element[0]

        if isOktrack:
            sent_window = SentWindow(number_current_track, name_our_track)
            sent_window.exec()

    def report_sent_train(self):
        """
        Функция для формирования отчета об отправленном поезде.
        Создает файл с отчетом и сразу открывает его.
        """

        name_our_track1, isOktrack1 = QInputDialog.getItem(window, 'Выбор пути',
                                                           'Укажите станцию, к которой отправился поезд, чтобы '
                                                           'сформировать отчет',
                                                           available_tracks_for_user)
        for element in stations_list:
            if element[1] == name_our_track1:
                number_current_track1 = element[0]

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True

        sent_number, isOkNumSent = QInputDialog.getText(self, 'Выбор номера поезда',
                                                        'Укажите номер отправленного поезда', text='NRTxxx')

        cursor.execute(f"SELECT * FROM sent_trains WHERE (sent_arrival_station = {number_current_track1} "
                       f"AND sent_number = '{sent_number}')")
        sent_train = cursor.fetchone()
        print(sent_train)
        if not sent_train:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ОШИБКА ДАННЫХ")
            msg.setInformativeText("Отправленного поезда с таким номером не существует")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        report_file = f'report{sent_number}.txt'
        with open(report_file, 'w') as report:
            report.write(f'ОТЧЕТ ОБ ОТПРАВЛЕННОМ ПОЕЗДЕ № {sent_number}\n\n')
            report.write(f'Количество вагонов: {sent_train[1]} шт.\n')
            report.write(f'Вес поезда: {sent_train[4]} т\n')
            report.write(f'Станция прибытия: {name_our_track1}\n')
            report.write(f'Дата отправления поезда: {sent_train[3]}')

        os.startfile(report_file)

        connection.commit()
        cursor.close()
        connection.close()

    def open_reports_window(self):
        """
        Функция для открытия окна отчётов
        """

        reports_window = ReportsWindow()
        reports_window.exec()


class ReceptionWindow(QDialog):
    """
    Класс окна приема поезда

    Методы:
    open_select_file: функция, принимающая и обрабатывающая текстовый файл
    с описанием поезда
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_ReceptionWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_select_file)

    def open_select_file(self):
        """
        Функция для приема и обработки текстового файла с описанием поезда
        Вызывает внутри себя функцию func_database.add_train_into_db
        """

        file_train = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "File txt (* .txt)")
        file_extension = pathlib.Path(file_train[0]).suffix

        if file_extension != '.txt':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ОШИБКА ФАЙЛА")
            msg.setInformativeText("Формат файла не соответствует указанному. Перепроверьте формат файла.")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return
        try:
            with open(file_train[0], 'r', encoding='UTF-8') as f:
                info_train = f.readlines()
                train_list = re.split(', |,|\\(|\\)\n', info_train[0])[1:4]
                wagons_list = []
                for i in range(1, len(info_train)):
                    wagons_list.append(re.split(', |,|\\(|\\)\n|\\)', info_train[i])[1:10])
            print(train_list)
        except UnicodeDecodeError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ОШИБКА КОДИРОВКИ ФАЙЛА")
            msg.setInformativeText("У прикрепленного файла неверная кодировка. "
                                   "Перепроверьте, чтобы кодировка была UTF-8.")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ОШИБКА ЗНАЧЕНИЙ В ФАЙЛЕ")
            msg.setInformativeText("У прикрепленного файла неверные данные или их отсутствие. Перепроверьте"
                                   " правильность входных данных")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
        wagons_list = [x for x in wagons_list if x != []]  # очистка от лишних пустых строк в файле
        print(wagons_list)
        print(train_list[1])
        print(len(wagons_list))
        try:
            if int(train_list[1]) - int(len(wagons_list)) != 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ОШИБКА ДАННЫХ")
                msg.setInformativeText("Количество вагонов не соответствует числу, указанному в поезде. "
                                       "Перепроверьте правильность входных данных.")
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                return

        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ОШИБКА ЗНАЧЕНИЙ В ФАЙЛЕ")
            msg.setInformativeText("У прикрепленного файла неверные данные или их отсутствие. Перепроверьте"
                                   " правильность входных данных")
            msg.setWindowTitle("Ошибка")
            msg.exec_()

        func_database.add_train_into_db(train_list, wagons_list, current_date, number_our_station)


class ReformWindow(QDialog):
    """
    Класс окна формирования поезда.

    Включает в себя выбор номера формируемых поездов и выбор
    перегона для их формирования. В конструкторе создается техническая карта перегона (список, где каждый
    элемент - список, состоящий из кортежа формируемого поезда из базы данных и словаря перегона с
    информацией о перегоне), а также обновляется и выводится информация о текущем перегоне, текущем количестве
    вагонов и текущем весе.

    Методы:
    add_wagons: добавляет вагоны в базу данных
    """

    def __init__(self, number_current_track, name_our_track):
        super().__init__()
        self.ui = Ui_ReformWindow()
        self.ui.setupUi(self)

        print(number_current_track)
        print(name_our_track)

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True
        cursor.execute("SELECT * FROM form_trains")
        if cursor.fetchone() is None:
            i = 1
            for path in available_tracks_for_db:
                cursor.execute("INSERT INTO form_trains VALUES (%s, %s, %s, %s, %s, %s)",
                               (i, 0, 0, 'NRT001', current_date, False))
                i = i + 1
        cursor.execute("SELECT * FROM form_trains ORDER BY form_id")
        form_trains = cursor.fetchall()
        technical_card_tracks = []
        for i in range(len(available_tracks_for_db)):
            tracks_dictionary[i]['Текущее кол-во вагонов'] = int(form_trains[i][1])
            tracks_dictionary[i]['Текущая масса'] = int(form_trains[i][2])
            technical_card_tracks.append([form_trains[i], tracks_dictionary[i]])
            technical_card_tracks[i][1]['Текущее кол-во вагонов'] = technical_card_tracks[i][0][1]
            technical_card_tracks[i][1]['Текущая масса'] = technical_card_tracks[i][0][2]
            technical_card_tracks[i][1]['Готовность к отправке'] = technical_card_tracks[i][0][5]

        self.current_card_track = [technical_card_tracks[i] for i in range(len(available_tracks_for_db)) if
                                   technical_card_tracks[i][1]['Технический номер перегона'] == number_current_track]
        print(technical_card_tracks)
        print(self.current_card_track)

        self.ui.lbl_title.setText("ОКНО ФОРМИРОВАНИЯ ПОЕЗДА")
        self.ui.lbl_track.setText(f'Перегон до станции {name_our_track}')
        self.ui.lbl_wag.setText(
            f"Текущее кол-во вагонов (шт.): {self.current_card_track[0][1]['Текущее кол-во вагонов']} из "
            f"{self.current_card_track[0][1]['Максимальное кол-во вагонов (шт.)']}")
        self.ui.lbl_weight.setText(f"Текущая масса поезда (т): {self.current_card_track[0][1]['Текущая масса']} из "
                                   f"{self.current_card_track[0][1]['Предельная масса поезда (т)']}")

        self.number_current_track = number_current_track
        self.name_our_track = name_our_track
        self.neighbours = neighbours
        self.number_our_station = number_our_station
        self.current_date = current_date
        self.neighbour_stations = neighbour_stations

        self.ui.btn_add_w.clicked.connect(self.add_wagons)

        connection.commit()
        cursor.close()
        connection.close()

    def add_wagons(self):
        """
        Функция для добавления вагонов на перегон.
        Вызывает внутри себя функцию funs_database.add_wagons_into_form
        """

        if self.current_card_track[0][0][5]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("ПРЕДУПРЕЖДЕНИЕ ФОРМИРОВАНИЯ ПОЕЗДА")
            msg.setInformativeText('Поезд готов к отправке: нельзя больше добавить вагонов')
            msg.setWindowTitle("Предупреждение")
            msg.exec_()
            return
        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True
        cursor.execute(f"SELECT * FROM form_trains WHERE (form_number = 'NTR001' AND "
                       f"form_id = {self.current_card_track[0][0][0]})")
        print(cursor.fetchall())
        if not cursor.fetchall():
            form_number, isOkNumForm = QInputDialog.getText(self, 'Выбор номера поезда',
                                                            'Укажите номер формируемого поезда', text='NRTxxx')
            cursor.execute("SELECT * FROM all_trains")
            all_trains = cursor.fetchall()
            all_trains = list(all_trains)
            print(all_trains)
            form_number = (form_number,)
            if form_number not in all_trains:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ОШИБКА ДАННЫХ")
                msg.setInformativeText('Введите номер поезда в указанном формате')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                return
            form_number = form_number[0]
            func_database.add_wagons_into_form(self.current_card_track, self.neighbour_stations, self.current_date,
                                               form_number, isOkNumForm)
        else:
            form_number = self.current_card_track[0][0][3]
            isOkNumForm = True
            func_database.add_wagons_into_form(self.current_card_track, self.neighbour_stations, self.current_date,
                                               form_number, isOkNumForm)


class SentWindow(QDialog):
    """
    Класс окна отправления поезда.

    Включает в себя выбор номера отправляемых поездов и выбор
    станции отправки. В конструкторе обновляется техническая карта перегона для вывода
    информацим о текущем перегоне, текущем количестве вагонов и текущем весе.

    Методы:
    sent_train: осуществляет отправку поезда (добавляет соответствующую запись в базу данных)
    """

    def __init__(self, number_current_track, name_our_track):
        super().__init__()
        self.ui = Ui_SentWindow()
        self.ui.setupUi(self)

        print(number_current_track)
        print(name_our_track)

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True

        cursor.execute("SELECT * FROM form_trains ORDER BY form_id")
        form_trains = cursor.fetchall()

        if not form_trains:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ИНФОРМАЦИЯ ОТПРАВКИ")
            msg.setInformativeText('Вы не можете отправить поезд: нет сформированных/формируемых поездов')
            msg.setWindowTitle("Информация")
            msg.exec_()
            self.close()

        technical_card_tracks = []
        for i in range(len(available_tracks_for_db)):
            tracks_dictionary[i]['Текущее кол-во вагонов'] = int(form_trains[i][1])
            tracks_dictionary[i]['Предельная масса поезда'] = int(form_trains[i][2])
            technical_card_tracks.append([form_trains[i], tracks_dictionary[i]])
            technical_card_tracks[i][1]['Текущее кол-во вагонов'] = technical_card_tracks[i][0][1]
            technical_card_tracks[i][1]['Текущая масса'] = technical_card_tracks[i][0][2]
            technical_card_tracks[i][1]['Готовность к отправке'] = technical_card_tracks[i][0][5]
            print(technical_card_tracks[i])

        self.current_card_track = [technical_card_tracks[i] for i in range(len(available_tracks_for_db)) if
                                   technical_card_tracks[i][1]['Технический номер перегона'] == number_current_track]

        print(technical_card_tracks)
        print(self.current_card_track)

        self.ui.lbl_title.setText("ОКНО ОТПРАВЛЕНИЯ ПОЕЗДА")
        self.ui.lbl_track.setText(f'Перегон до станции {name_our_track}')
        self.ui.lbl_wag.setText(
            f"Текущее кол-во вагонов (шт.): {self.current_card_track[0][1]['Текущее кол-во вагонов']} из "
            f"{self.current_card_track[0][1]['Максимальное кол-во вагонов (шт.)']}")
        self.ui.lbl_weight.setText(
            f"Текущая масса поезда (т): {float(self.current_card_track[0][1]['Текущая масса'])} из "
            f"{self.current_card_track[0][1]['Предельная масса поезда (т)']}")
        self.ui.btn_add_w.setText('Отправить поезд')

        self.number_current_track = number_current_track
        self.name_our_track = name_our_track
        self.neighbours = neighbours
        self.number_our_station = number_our_station
        self.current_date = current_date
        self.neighbour_stations = neighbour_stations

        self.ui.btn_add_w.clicked.connect(self.sent_train)

        connection.commit()
        cursor.close()
        connection.close()

    def sent_train(self):
        """
        Функция отправки поезда.
        Вызывает внутри себя функцию func_database.sent_train_into_db
        """

        if not self.current_card_track[0][1]['Готовность к отправке']:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("ПРЕДУПРЕЖДЕНИЕ ОТПРАВЛЕНИЯ ПОЕЗДА")
            msg.setInformativeText('Данный поезд не готов к отправке: нужно добавить больше вагонов')
            msg.setWindowTitle("Предупреждение")
            msg.exec_()
            return
        func_database.sent_train_into_db(self.current_card_track, self.current_date, self.number_current_track,
                                         self.name_our_track)


class ReportsWindow(QDialog):
    """
    Класс окна отчётов.

    Включает в себя несколько отчетов: о текущих принимаемых и формируемых поезда, грузообороте
    за произвольный период и эффективность работы станции. Все отчеты создаются в виде отдельного
    файла, который сразу же открывается.

    Методы:
    current_reception_trains: формирует отчет о текущих принимаемых поездах
    current_reform_trains: формирует отчет о текущих формируемых поездах
    cargo_turnover_table: формирует отчет грузооборота станции за произвольный период
    station_success_table: формирует отчет эффективности станции
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_ReportsWindow()
        self.ui.setupUi(self)

        id = QFontDatabase.addApplicationFont("Arial.ttf")
        if id < 0:
            print("Error")
        families = QFontDatabase.applicationFontFamilies(id)
        self.setFont(QFont(families[0], 80))

        self.ui.pushButton.clicked.connect(self.current_reception_trains)
        self.ui.pushButton_2.clicked.connect(self.current_reform_trains)
        self.ui.pushButton_3.clicked.connect(self.cargo_turnover_table)
        self.ui.pushButton_4.clicked.connect(self.station_success_table)

        self.date_range_selector = None

    def current_reception_trains(self):
        """
        Функция создания отчета о принимаемых поездах на текущую дату
        """

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True

        cursor.execute(f"SELECT * FROM trains WHERE train_arrival_date = '{current_date}'")
        trains = cursor.fetchall()

        if not trains:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ОТЧЁТНАЯ ИНФОРМАЦИЯ")
            msg.setInformativeText('Отсутствуют принятые поезда на текущую дату')
            msg.setWindowTitle("Информация")
            msg.exec_()
            return

        title_list = ['Номер поезда', 'Кол-во вагонов']
        trains_list = []

        for train in trains:
            train = list(train)
            train = [train[3]] + [train[1]]
            print(train)
            trains_list.append(train)

        print(trains)

        report_recept_file = f'report_reception_trains.txt'

        i = 1
        while os.path.exists(report_recept_file):
            report_recept_file = f'report_reception_trains ({i}).txt'
            i += 1

        with open(report_recept_file, 'w') as report:
            report.write(f'ПЕРЕЧЕНЬ ПРИНИМАЕМЫХ ПОЕЗДОВ НА {current_date}\n\n')
            report.write('{:^20s}{:^15s}\n'.format(title_list[0], title_list[1]))

            for train in trains_list:
                report.write('{:^20s}{:^15d}\n'.format(train[0], train[1]))

        os.startfile(report_recept_file)

        connection.commit()
        cursor.close()
        connection.close()

    def current_reform_trains(self):
        """
        Функция создания отчета о формируемых поездах на текущую дату
        """

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True

        cursor.execute(f"SELECT * FROM form_trains WHERE (isReady = False "
                       f"AND form_number <> 'NRT001')")
        form_trains = cursor.fetchall()

        if not form_trains:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ОТЧЁТНАЯ ИНФОРМАЦИЯ")
            msg.setInformativeText('Отсутствуют формируемые поезда на текущую дату')
            msg.setWindowTitle("Информация")
            msg.exec_()
            return

        title_list = ['Номер поезда', 'Кол-во вагонов', 'Вес']
        form_trains_list = []

        for train in form_trains:
            train = list(train)
            train = [train[3]] + [train[1]] + [train[2]]
            print(train)
            form_trains_list.append(train)

        print(form_trains_list)

        report_reform_file = f'report_reform_trains.txt'

        i = 1
        while os.path.exists(report_reform_file):
            report_reform_file = f'report_reform_trains ({i}).txt'
            i += 1

        with open(report_reform_file, 'w') as report:
            report.write(f'ПЕРЕЧЕНЬ ФОРМИРУЕМЫХ ПОЕЗДОВ НА {current_date}\n\n')
            report.write('{:^20s}{:^15s}{:^15s}\n'.format(title_list[0], title_list[1], title_list[2]))

            for train in form_trains_list:
                report.write('{:^20s}{:^15d}{:^15d}\n'.format(train[0], train[1], train[2]))

        os.startfile(report_reform_file)

        connection.commit()
        cursor.close()
        connection.close()

    def cargo_turnover_table(self):
        """
        Функция создания отчета грузооборота станции за произвольный период
        """

        if not self.date_range_selector:
            self.date_range_selector = DateRangeSelector()
            self.date_range_selector.setWindowModality(Qt.ApplicationModal)
        self.date_range_selector.show()

    def station_success_table(self):
        """
        Функция создания отчета эффективности станции
        """

        connection = psycopg2.connect(
            database="Railway junction",
            user="postgres",
            password="PMIdatabase",
            host="127.0.0.1",
            port="5432"
        )
        cursor = connection.cursor()
        connection.autocommit = True

        report_success_file = f'report_success_file.txt'

        i = 1
        while os.path.exists(report_success_file):
            report_success_file = f'report_success_file ({i}).txt'
            i += 1

        cursor.execute("SELECT * FROM station_success_trains")
        success = cursor.fetchall()[0][0]
        print(success)

        cursor.execute("SELECT * FROM wagons_for_form_trains WHERE fk_form_train_id IS NOT NULL")
        total_wagons = len(cursor.fetchall())

        cursor.execute("SELECT * FROM wagons_for_form_trains WHERE (fk_form_train_id IS NOT NULL AND "
                       "wfft_net = 0)")
        empty_wagons = len(cursor.fetchall())

        try:
            ratio = empty_wagons / total_wagons
        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ОТЧЁТНАЯ ИНФОРМАЦИЯ")
            msg.setInformativeText('Отсутствуют формируемые поезда на данный момент')
            msg.setWindowTitle("Информация")
            msg.exec_()
            return

        with open(report_success_file, 'w') as report:
            report.write(f'ЭФФЕКТИВНОСТЬ СТАНЦИИ\n\n')
            report.write(f'Количество "пустых" принятых/сформированных поездов (шт.): {success}\n')
            report.write(f'Среднее отношение пустых вагонов к вагонам с грузом в сформированных поездах: {ratio}')

        os.startfile(report_success_file)

        connection.commit()
        cursor.close()
        connection.close()


if __name__ == "__main__":
    # Блок чтения номеров поездов и вагонов и добавление их в базу данных
    with open('numbers_trains.txt', 'r', encoding='UTF-8') as all_trains_file:
        info_all_trains = all_trains_file.readlines()
        all_trains_list_2d = []
        all_trains_list = []
        for i in range(0, len(info_all_trains)):
            all_trains_list_2d.append(re.split('\n', info_all_trains[i])[0:1])
            all_trains_list.append(all_trains_list_2d[i][0])
    all_trains_list = [x for x in all_trains_list if x != []]
    with open('numbers_wagons.txt', 'r', encoding='UTF-8') as all_wagons_file:
        info_all_wagons = all_wagons_file.readlines()
        all_wagons_list_2d = []
        all_wagons_list = []
        for i in range(0, len(info_all_wagons)):
            all_wagons_list_2d.append(re.split('\n', info_all_wagons[i])[0:1])
            all_wagons_list.append(all_wagons_list_2d[i][0])
    all_wagons_list = [x for x in all_wagons_list if x != []]
    # func_database.add_numbers_trains_and_wagons_into_db(all_trains_list, all_wagons_list)

    # Блок чтения станций из файла со станциями и добавление их в базу данных
    with open('stations.txt', 'r', encoding='UTF-8') as stations_file:
        info_stations = stations_file.readlines()
        stations_list = []
        for i in range(0, len(info_stations)):
            stations_list.append(re.split(', |\\(|\\)\n', info_stations[i])[1:3])
            stations_list[i][0] = int(stations_list[i][0])

    stations_list = [x for x in stations_list if x != []]
    # func_database.add_stations_into_db(stations_list)

    # Блок чтения графа станций из файла с сетью станций и добавление его в базу данных
    with open('network_stations.txt', 'r', encoding='UTF-8') as network_stations_file:
        info_network_stations = network_stations_file.readlines()
        network_stations_list = []
        for i in range(0, len(info_network_stations)):
            network_stations_list.append(re.split(', |\\(|\\)\n|\\)', info_network_stations[i])[1:3])
            network_stations_list[i][0] = int(network_stations_list[i][0])
            network_stations_list[i][1] = int(network_stations_list[i][1])

    network_stations_list = [x for x in network_stations_list if x != []]
    # func_database.add_network_stations_into_db(network_stations_list)

    # Блок создания графов станций и его вывод (в т.ч. графический)
    Graph_for_user = nx.Graph()
    Graph_for_db = nx.Graph()
    for station in stations_list:
        Graph_for_user.add_node(station[1])
        Graph_for_db.add_node(station[0])
    for network in network_stations_list:
        Graph_for_user.add_edge(stations_list[network[0] - 1][1], stations_list[network[1] - 1][1])
        Graph_for_db.add_edge(network[0], network[1])
    # plot_network_stations(Graph_for_user)

    # Блок задания параметров N (максимальное кол-во вагонов) и K (максимальная масса) для каждого перегона
    Graph_railway = nx.Graph()
    with open('railway_characteristics.txt', 'r', encoding='UTF-8') as characteristics_file:
        info_characteristics = characteristics_file.readlines()
        characteristics_list = []
        for i in range(0, len(info_characteristics)):
            characteristics_list.append(re.split(', |\\(|\\)\n|\\)', info_characteristics[i])[1:3])
            characteristics_list[i][0] = int(characteristics_list[i][0])
            characteristics_list[i][1] = int(characteristics_list[i][1])
    characteristics_list = [x for x in characteristics_list if x != []]
    for station in stations_list:
        Graph_railway.add_node(station[0])
    for network in network_stations_list:
        Graph_railway.add_edge(network[0], network[1],
                               weight=characteristics_list[network_stations_list.index(network)][0] +
                                      characteristics_list[network_stations_list.index(network)][1] * 1j)

    # Блок создания основного окна приложения
    app = QApplication(sys.argv)
    window = RailwayJunction()

    # Блок выбора текущей станции
    stations_list_name = [stations_list[i][1] for i in range(len(stations_list))]
    our_station, isOk = QInputDialog.getItem(window, 'Выбор станции',
                                             'Укажите станцию, на которой находитесь', stations_list_name)

    # Блок выбора текущей даты
    try:
        for station in stations_list:
            if str(station[1]) == str(our_station):
                number_our_station = int(station[0])
        date, isOk1 = QInputDialog.getText(window, 'Выбор даты', 'Укажите текущую дату', text='дд.мм.гггг')
        date = str(date).split('.')
        date = ''.join(date)
        current_date = datetime.datetime.strptime(date, "%d%m%Y").date()
    except Exception:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ВВОДА ДАТЫ")
        msg.setInformativeText("Введите дату в указанном формате.")
        msg.setWindowTitle("Ошибка")
        msg.exec_()
        isOk1 = False

    # Блок составления списка "(пункт назначения, сосед)"
    neighbour_stations = []
    for station in stations_list:
        if station[1] != our_station:
            shortest_path_with_points = nx.bidirectional_shortest_path(Graph_for_db,
                                                                       stations_list_name.index(our_station) + 1,
                                                                       station[0])
            neighbour_stations_elem = [int(station[0]), int(shortest_path_with_points[1])]
            neighbour_stations.append(neighbour_stations_elem)
    # func_database.add_neighbour_stations_into_db(neighbour_stations)

    # Блок вычисления количества доступных для формирования путей и вычисления соседей текущей станции
    neighbours = set()
    for elem in neighbour_stations:
        neighbours.add(int(elem[1]))
    numbers_tracks = len(neighbours)
    neighbours = list(neighbours)

    # Блок составления списка доступных перегонов
    available_tracks_for_user = []
    available_tracks_for_db = []
    for track in neighbours:
        available_tracks_for_user.append(stations_list[track - 1][1])
        available_tracks_for_db.append(track)

    # Блок составления словарей доступных перегонов
    tracks_dictionary = []
    for i in range(len(available_tracks_for_db)):
        diction = dict()
        edge_data = Graph_railway.get_edge_data(number_our_station, available_tracks_for_db[i])
        edge_weight = edge_data['weight']
        N = int(edge_weight.real)  # максимальное кол-во вагонов для данного перегона
        K = edge_weight.imag  # максимальный вес поезда для данного перегона
        diction['Технический номер перегона'] = available_tracks_for_db[i]
        diction['Перегон'] = (our_station, available_tracks_for_user[i])
        diction['Максимальное кол-во вагонов (шт.)'] = N
        diction['Предельная масса поезда (т)'] = K
        diction['Текущее кол-во вагонов'] = 0
        diction['Текущая масса'] = 0
        diction['Готовность к отправке'] = False
        tracks_dictionary.append(diction)

    # Блок открытия основного окна приложения после выбора даты и станции
    if isOk and isOk1:
        window.show()

    # Блок выхода из приложения
    sys.exit(app.exec())
