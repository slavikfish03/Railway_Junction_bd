"""Функции, связанные с добавлением данных из Python в базу данных PostgreSQL"""


import psycopg2
import main
import datetime

from typing import List, Set

from PySide6.QtWidgets import QMessageBox, QInputDialog


def add_numbers_trains_and_wagons_into_db(all_trains: List, all_wagons: List):
    """
    Функция добавления допустимых номеров поездов и вагонов в базу данных

    :param all_trains: список всех допустимых номеров поездов
    :param all_wagons: список всех допустимых номеров вагонов
    """

    connection = psycopg2.connect(
        database="Railway junction",
        user="postgres",
        password="PMIdatabase",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    try:
        for number_train in all_trains:
            cursor.execute("INSERT INTO all_trains VALUES (%s)", (number_train,))
        for number_wagon in all_wagons:
            cursor.execute("INSERT INTO all_wagons VALUES (%s)", (number_wagon,))
    except psycopg2.DataError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ДАННЫХ")
        msg.setInformativeText('Ошибка соответствия типов данных. Перепроверьте правильность типов данных во входном '
                               'файле.')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    connection.commit()
    cursor.close()
    connection.close()


def add_neighbour_stations_into_db(neighbour_stations_list: List):
    """
    Функция добавления таблицы (пункт назначения, сосед) в базу данных

    :param neighbour_stations_list: таблица (пункт назначения, сосед)
    """

    connection = psycopg2.connect(
        database="Railway junction",
        user="postgres",
        password="PMIdatabase",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    try:
        for neighbour in neighbour_stations_list:
            cursor.execute("INSERT INTO neighbour_stations VALUES (%s, %s)", neighbour)
    except psycopg2.DataError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ДАННЫХ")
        msg.setInformativeText('Ошибка соответствия типов данных. Перепроверьте правильность типов данных во входном '
                               'файле.')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    connection.commit()
    cursor.close()
    connection.close()


def add_network_stations_into_db(network_stations_list: List):
    """
    Функция добавления станций в базу данных

    :param network_stations_list: список с информацией о сети станций (номер 1-ой станции, номер 2-ой станции)
    """
    connection = psycopg2.connect(
        database="Railway junction",
        user="postgres",
        password="PMIdatabase",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    try:
        for network in network_stations_list:
            cursor.execute("INSERT INTO network_stations VALUES (%s, %s)", network)
    except psycopg2.DataError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ДАННЫХ")
        msg.setInformativeText('Ошибка соответствия типов данных. Перепроверьте правильность типов данных во входном '
                               'файле.')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    connection.commit()
    cursor.close()
    connection.close()


def add_stations_into_db(stations_list: List):
    """
    Функция добавления станций в базу данных

    :param stations_list: список с информацией о станциях (номер, название)
    """
    connection = psycopg2.connect(
        database="Railway junction",
        user="postgres",
        password="PMIdatabase",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    try:
        for station in stations_list:
            cursor.execute("INSERT INTO stations VALUES (%s, %s)", station)
    except psycopg2.DataError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ДАННЫХ")
        msg.setInformativeText('Ошибка соответствия типов данных. Перепроверьте правильность типов данных во входном '
                               'файле.')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    connection.commit()
    cursor.close()
    connection.close()


def add_train_into_db(train_list: List, wagons_list: List, current_date: datetime, number_our_station: int):
    """
    Функция добавления информации о прибывшем поезде и его вагонах в базу данных

    :param train_list: список с информацией о поезде (специальный номер, кол-во вагонов, номер поезда)
    :param wagons_list: список с информацией о каждом вагоне прибывшего поезда (элемент списка:
    специальный номер вагона, категория груза, груз, вес нетто, вес брутто, станция назначения, станция приписки, номер вагона)
    :param current_date: дата принятия поезда (т.е. текущая)
    :param number_our_station: технический номер станции местонахождения сотрудника
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

    try:
        cursor.execute(f"SELECT count(1) > 0 FROM all_trains WHERE available_train_number = '{train_list[2]}'")
        if not cursor.fetchone()[0]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ОШИБКА ДАННЫХ")
            msg.setInformativeText('Поезда с таким номером не существует. Проверьте правильность входных данных')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            connection.commit()
            cursor.close()
            connection.close()

        cursor.execute(f"SELECT count(1) > 0 FROM trains WHERE (train_number = '{train_list[2]}' "
                       f"and train_arrival_date = '{current_date}')")
        if cursor.fetchone()[0]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ОШИБКА ДАННЫХ")
            msg.setInformativeText('Поезд с таким номером уже принят. Проверьте правильность входных данных')
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            connection.commit()
            cursor.close()
            connection.close()

        for wagon in wagons_list:
            cursor.execute(f"SELECT count(1) > 0 FROM all_wagons WHERE available_wagon_number = '{wagon[8]}'")
            if not cursor.fetchone()[0]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ОШИБКА ДАННЫХ")
                msg.setInformativeText('Вагона с таким номером не существует. Проверьте правильность входных данных')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                connection.commit()
                cursor.close()
                connection.close()

            cursor.execute(f"SELECT count(1) > 0 FROM our_wagons WHERE number_our_wagon ='{wagon[8]}'")
            if cursor.fetchone()[0]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ОШИБКА ДАННЫХ")
                msg.setInformativeText('Один из вагонов с таким номером уже находится на станции как приписанный. '
                                       'Проверьте правильность входных данных')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                connection.commit()
                cursor.close()
                connection.close()

            cursor.execute(f"SELECT count(1) > 0 FROM wagons_for_form_trains WHERE wfft_number = '{wagon[8]}'")
            if cursor.fetchone()[0]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ОШИБКА ДАННЫХ")
                msg.setInformativeText('Один из вагонов с таким номером уже находится на станции в сортировочном парке.'
                                       ' Проверьте правильность входных данных')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                connection.commit()
                cursor.close()
                connection.close()

        cursor.execute("SELECT * from trains")
        if cursor.fetchone() is None:
            list_train = [1] + train_list[1:]
        else:
            cursor.execute("SELECT * FROM trains ORDER BY train_id DESC LIMIT 1")
            list_train = [cursor.fetchone()[0] + 1] + train_list[1:]

        list_train.insert(2, current_date)
        print(list_train)
        cursor.execute("INSERT INTO trains VALUES (%s, %s, %s, %s)", list_train)

        isEmptyWagon = 0
        for wagon in wagons_list:

            if int(wagon[3]) == 0:
                isEmptyWagon = isEmptyWagon + 1

            cursor.execute("SELECT * from wagons")
            if cursor.fetchone() is None:
                list_wagon = [1] + wagon[1:9]
            else:
                cursor.execute("SELECT * FROM wagons ORDER BY wagon_id DESC LIMIT 1")
                list_wagon = [cursor.fetchone()[0] + 1] + wagon[1:9]
            print(list_wagon)
            cursor.execute("INSERT INTO wagons VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", list_wagon)

        cursor.execute("SELECT * FROM station_success_trains")
        isEmptyTrain = cursor.fetchall()
        if not isEmptyTrain:
            cursor.execute("INSERT INTO station_success_trains (quantity_empty_trains) VALUES (0)")

        if int(isEmptyWagon) == int(len(wagons_list)):
            cursor.execute("UPDATE station_success_trains SET quantity_empty_trains = quantity_empty_trains + 1")

        for wagon in wagons_list:
            wagon = list(wagon)
            cursor.execute("SELECT * from reception_wagons")
            wagon[7] = None
            if cursor.fetchone() is None:
                list_wagon = [1] + wagon[1:9] + [current_date]
            else:
                cursor.execute("SELECT * FROM reception_wagons ORDER BY wagon_id DESC LIMIT 1")
                list_wagon = [cursor.fetchone()[0] + 1] + wagon[1:9] + [current_date]
            print(list_wagon)
            cursor.execute("INSERT INTO reception_wagons VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list_wagon)

        cursor.execute("SELECT * FROM wagons")
        wagons = cursor.fetchall()
        cursor.execute("DELETE FROM wagons")
        for wagon in wagons:
            wagon = list(wagon)
            wagon[7] = None
            if wagon[5] == number_our_station and wagon[6] == number_our_station:
                print(wagon)
                cursor.execute(f"DELETE FROM wagons WHERE (wagon_destination_station = '{number_our_station}' AND "
                               f"wagon_home_station = '{number_our_station}')")
                cursor.execute("INSERT INTO our_wagons VALUES (%s)", (wagon[8],))
            elif wagon[5] == number_our_station and wagon[6] != number_our_station:
                wagon[4] = wagon[4] - wagon[3]
                wagon[3] = 0
                cursor.execute("SELECT * from wagons_for_form_trains")
                if cursor.fetchone() is None:
                    list_wagon = [1] + wagon[1:9]
                else:
                    cursor.execute("SELECT * FROM wagons_for_form_trains ORDER BY wfft_id DESC LIMIT 1")
                    list_wagon = [cursor.fetchone()[0] + 1] + wagon[1:9]
                cursor.execute("INSERT INTO wagons_for_form_trains VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               list_wagon)
            elif wagon[6] != number_our_station or wagon[5] != number_our_station:
                cursor.execute("SELECT * from wagons_for_form_trains")
                if cursor.fetchone() is None:
                    list_wagon = [1] + wagon[1:9]
                else:
                    cursor.execute("SELECT * FROM wagons_for_form_trains ORDER BY wfft_id DESC LIMIT 1")
                    list_wagon = [cursor.fetchone()[0] + 1] + wagon[1:9]
                cursor.execute("INSERT INTO wagons_for_form_trains VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               list_wagon)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText('Поезд успешно принят')
        msg.setWindowTitle("Информация")
        msg.exec_()
    except psycopg2.DataError:
        cursor.execute("DELETE FROM wagons")
        cursor.execute("DELETE FROM trains")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ДАННЫХ")
        msg.setInformativeText('Ошибка соответствия типов данных. Перепроверьте правильность типов данных во входном '
                               'файле.')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    connection.commit()
    cursor.close()
    connection.close()


def add_wagons_into_form(current_card_track: List, neighbours_stations: List, current_date, form_number, isOkNumForm):
    """
    Функция перереформирования поезда с указанным максимальным весом и максимальным кол-вом вагонов

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
    # number_tracks = len(neighbours)
    try:

        if isOkNumForm:
            cursor.execute("SELECT * FROM wagons_for_form_trains WHERE fk_form_train_id IS NULL")
            wfft = cursor.fetchall()
            if not wfft:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("ИНФОРМАЦИЯ О СФОРМИРОВАНИИ ПОЕЗДА")
                msg.setInformativeText('Нет доступных для формирования вагонов.')
                msg.setWindowTitle("Информация")
                msg.exec_()
                return
            wfft = [wagon for wagon in wfft if ([wagon[5], current_card_track[0][1]['Технический номер перегона']]
                                                in neighbours_stations or [wagon[6], current_card_track[0][1][
                        'Технический номер перегона']] in neighbours_stations)]

            if not wfft:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("ИНФОРМАЦИЯ О СФОРМИРОВАНИИ ПОЕЗДА")
                msg.setInformativeText('Нет доступных для формирования вагонов на этом направлении.')
                msg.setWindowTitle("Информация")
                msg.exec_()
                return

            current_weight = current_card_track[0][1]['Текущая масса']
            current_wagons = current_card_track[0][1]['Текущее кол-во вагонов']
            max_weight = current_card_track[0][1]['Предельная масса поезда (т)']
            max_wagons = current_card_track[0][1]['Максимальное кол-во вагонов (шт.)']
            for wagon in wfft:
                wagon = list(wagon)
                current_weight = current_weight + wagon[4]
                current_wagons = current_wagons + 1
                if current_weight > max_weight:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("ПРЕДУПРЕЖДЕНИЕ ФОРМИРОВАНИЯ ПОЕЗДА")
                    msg.setInformativeText('Достигнут предел по массе')
                    msg.setWindowTitle("Предупреждение")
                    msg.exec_()

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("ИНФОРМАЦИЯ О СФОРМИРОВАНИИ ПОЕЗДА")
                    msg.setInformativeText(
                        f"Поезд на перегоне {current_card_track[0][1]['Перегон']} сформирован и готов "
                        f"к отправке. Перейдите в раздел 'Отправка поезда'")
                    msg.setWindowTitle("Информация")
                    msg.exec_()
                    cursor.execute(f"UPDATE form_trains SET isReady = True WHERE form_id = '{current_card_track[0][0][0]}'")
                    break
                if current_wagons > max_wagons:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("ПРЕДУПРЕЖДЕНИЕ ФОРМИРОВАНИЯ ПОЕЗДА")
                    msg.setInformativeText('Достигнут предел по количеству вагонов')
                    msg.setWindowTitle("Предупреждение")
                    msg.exec_()

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("ИНФОРМАЦИЯ О СФОРМИРОВАНИИ ПОЕЗДА")
                    msg.setInformativeText(
                        f"Поезд на перегоне {current_card_track[0][1]['Перегон']} сформирован и готов "
                        f"к отправке. Перейдите в раздел 'Отправка поезда'")
                    msg.setWindowTitle("Информация")
                    msg.exec_()
                    cursor.execute(f"UPDATE form_trains SET isReady = True WHERE form_id = '{current_card_track[0][0][0]}'")
                    break

                wagon[7] = current_card_track[0][0][0]
                print(wagon)
                current_card_track[0][1]['Текущее кол-во вагонов'] = current_wagons
                current_card_track[0][1]['Текущая масса'] = current_weight

                cursor.execute(f"DELETE FROM wagons_for_form_trains WHERE wfft_id = '{wagon[0]}'")
                cursor.execute("INSERT INTO wagons_for_form_trains VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", wagon)

            cursor.execute(f"UPDATE form_trains SET "
                           f"form_id = '{current_card_track[0][0][0]}', "
                           f"form_wagons_amount = '{current_card_track[0][1]['Текущее кол-во вагонов']}', "
                           f"form_weight = '{current_card_track[0][1]['Текущая масса']}', "
                           f"form_number = '{form_number}', "
                           f"form_current_date = '{current_date}' "
                           f"WHERE form_id = '{current_card_track[0][0][0]}'")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ИНФОРМАЦИЯ О СФОРМИРОВАНИИ ПОЕЗДА")
            msg.setInformativeText('Вагоны успешно добавлены на данный перегон')
            msg.setWindowTitle("Информация")
            msg.exec_()

    except psycopg2.DataError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ДАННЫХ")
        msg.setInformativeText('Ошибка соответствия типов данных. Перепроверьте правильность типов данных во входном '
                               'файле.')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    connection.commit()
    cursor.close()
    connection.close()


def sent_train_into_db(current_card_track, current_date, number_current_track, name_our_track):
    connection = psycopg2.connect(
        database="Railway junction",
        user="postgres",
        password="PMIdatabase",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()
    connection.autocommit = True
    try:
        cursor.execute(f"SELECT * FROM form_trains WHERE form_id = {current_card_track[0][0][0]}")
        train_being_sent_but_form = cursor.fetchone()

        if train_being_sent_but_form[3] == 'NRT001':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("ПРЕДУПРЕЖДЕНИЕ ОТПРАВКИ ПОЕЗДА")
            msg.setInformativeText(f'Поезд либо уже отправлен, либо еще не сформирован')
            msg.setWindowTitle("Информация")
            msg.exec_()
            return

        if not train_being_sent_but_form[5]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("ПРЕДУПРЕЖДЕНИЕ ОТПРАВКИ ПОЕЗДА")
            msg.setInformativeText(f'Поезд еще не готов к отправке')
            msg.setWindowTitle("Информация")
            msg.exec_()
            return

        cursor.execute("SELECT * from sent_trains")
        if cursor.fetchone() is None:
            train_being_sent = (1,) + (train_being_sent_but_form[1],) + (number_current_track,) + \
                               (current_date,) + tuple(train_being_sent_but_form[2:4])
        else:
            cursor.execute("SELECT * FROM sent_trains ORDER BY sent_id DESC LIMIT 1")
            train_being_sent = (cursor.fetchone()[0] + 1,) + (train_being_sent_but_form[1],) + (number_current_track,) + \
                               (current_date,) + tuple(train_being_sent_but_form[2:4])

        cursor.execute("INSERT INTO sent_trains VALUES (%s, %s, %s, %s, %s, %s)", train_being_sent)

        cursor.execute(f"SELECT * FROM wagons_for_form_trains WHERE fk_form_train_id = '{current_card_track[0][0][0]}'")
        sent_wagons = cursor.fetchall()

        for sent_wagon in sent_wagons:
            cursor.execute('SELECT * FROM sent_wagons')
            sent_wagon = list(sent_wagon)
            sent_wagon[7] = list(train_being_sent)[0]
            if cursor.fetchone() is None:
                sent_wagon[7] = list(train_being_sent)[0]
                sent_wagons_tuple = (1,) + tuple(sent_wagon[1:]) + (list(train_being_sent)[3],)
            else:
                cursor.execute("SELECT * FROM sent_wagons ORDER BY sent_w_id DESC LIMIT 1")
                sent_wagons_tuple = (cursor.fetchone()[0] + 1,) + tuple(sent_wagon[1:]) + (list(train_being_sent)[3],)
            cursor.execute("INSERT INTO sent_wagons VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", sent_wagons_tuple)

        cursor.execute(f"DELETE FROM wagons_for_form_trains WHERE fk_form_train_id = '{current_card_track[0][0][0]}'")

        cursor.execute(f"UPDATE form_trains SET "
                       f"form_id = '{current_card_track[0][0][0]}', "
                       f"form_wagons_amount = '{0}', "
                       f"form_weight = '{0}', "
                       f"form_number = 'NRT001', "
                       f"form_current_date = '{current_date}', "
                       f"isReady = False "
                       f"WHERE form_id = '{current_card_track[0][0][0]}'")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("ИНФОРМАЦИЯ ОТПРАВКИ ПОЕЗДА")
        msg.setInformativeText(f'Поезд успешно отправлен до станции {name_our_track}')
        msg.setWindowTitle("Информация")
        msg.exec_()

    except psycopg2.DataError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ОШИБКА ДАННЫХ")
        msg.setInformativeText('Ошибка соответствия типов данных. Перепроверьте правильность типов данных во входном '
                               'файле.')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    pass
