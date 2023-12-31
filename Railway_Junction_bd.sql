PGDMP     6    	                {            Railway junction    15.2    15.2 9    [           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            \           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ]           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ^           1262    16399    Railway junction    DATABASE     �   CREATE DATABASE "Railway junction" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
 "   DROP DATABASE "Railway junction";
                postgres    false            �            1259    16558 
   all_trains    TABLE     _   CREATE TABLE public.all_trains (
    available_train_number character varying(128) NOT NULL
);
    DROP TABLE public.all_trains;
       public         heap    postgres    false            �            1259    16565 
   all_wagons    TABLE     _   CREATE TABLE public.all_wagons (
    available_wagon_number character varying(128) NOT NULL
);
    DROP TABLE public.all_wagons;
       public         heap    postgres    false            �            1259    16430    form_trains    TABLE     �   CREATE TABLE public.form_trains (
    form_id integer NOT NULL,
    form_wagons_amount integer NOT NULL,
    form_weight integer NOT NULL,
    form_number text NOT NULL,
    form_current_date date,
    isready boolean NOT NULL
);
    DROP TABLE public.form_trains;
       public         heap    postgres    false            �            1259    16480    neighbour_stations    TABLE     �   CREATE TABLE public.neighbour_stations (
    n_destination_station integer NOT NULL,
    n_neighbour_station integer NOT NULL
);
 &   DROP TABLE public.neighbour_stations;
       public         heap    postgres    false            �            1259    16465    network_stations    TABLE     i   CREATE TABLE public.network_stations (
    station_1 integer NOT NULL,
    station_2 integer NOT NULL
);
 $   DROP TABLE public.network_stations;
       public         heap    postgres    false            �            1259    16602 
   our_wagons    TABLE     >   CREATE TABLE public.our_wagons (
    number_our_wagon text
);
    DROP TABLE public.our_wagons;
       public         heap    postgres    false            �            1259    16659    reception_wagons    TABLE     f  CREATE TABLE public.reception_wagons (
    wagon_id integer,
    wagon_cargo_category character varying(16),
    wagon_cargo character varying(16),
    wagon_net integer,
    wagon_gross integer,
    wagon_destination_station integer,
    wagon_home_station integer,
    fk_train_id integer,
    wagon_number text,
    recept_w_arrival_date date NOT NULL
);
 $   DROP TABLE public.reception_wagons;
       public         heap    postgres    false            �            1259    16425    sent_trains    TABLE     �   CREATE TABLE public.sent_trains (
    sent_id integer NOT NULL,
    sent_wagons_amount integer NOT NULL,
    sent_arrival_station integer NOT NULL,
    sent_departure_date date NOT NULL,
    sent_weight integer NOT NULL,
    sent_number text NOT NULL
);
    DROP TABLE public.sent_trains;
       public         heap    postgres    false            �            1259    16445    sent_wagons    TABLE     �  CREATE TABLE public.sent_wagons (
    sent_w_id integer NOT NULL,
    sent_w_cargo_category character varying(16) NOT NULL,
    sent_w_cargo character varying(16) NOT NULL,
    sent_w_net integer NOT NULL,
    sent_w_gross integer NOT NULL,
    sent_w_destination_station integer NOT NULL,
    sent_w_home_station integer NOT NULL,
    fk_sent_train_id integer,
    sent_w_number text NOT NULL,
    sent_w_departure_date date NOT NULL
);
    DROP TABLE public.sent_wagons;
       public         heap    postgres    false            �            1259    16673    station_success_trains    TABLE     \   CREATE TABLE public.station_success_trains (
    quantity_empty_trains integer DEFAULT 0
);
 *   DROP TABLE public.station_success_trains;
       public         heap    postgres    false            �            1259    16460    stations    TABLE     s   CREATE TABLE public.stations (
    station_id integer NOT NULL,
    station_name character varying(64) NOT NULL
);
    DROP TABLE public.stations;
       public         heap    postgres    false            �            1259    16420    trains    TABLE     �   CREATE TABLE public.trains (
    train_id integer NOT NULL,
    train_wagons_amount integer NOT NULL,
    train_arrival_date date NOT NULL,
    train_number text NOT NULL
);
    DROP TABLE public.trains;
       public         heap    postgres    false            �            1259    16435    wagons    TABLE     {  CREATE TABLE public.wagons (
    wagon_id integer NOT NULL,
    wagon_cargo_category character varying(16) NOT NULL,
    wagon_cargo character varying(16) NOT NULL,
    wagon_net integer NOT NULL,
    wagon_gross integer NOT NULL,
    wagon_destination_station integer NOT NULL,
    wagon_home_station integer NOT NULL,
    fk_train_id integer,
    wagon_number text NOT NULL
);
    DROP TABLE public.wagons;
       public         heap    postgres    false            �            1259    16455    wagons_for_form_trains    TABLE     �  CREATE TABLE public.wagons_for_form_trains (
    wfft_id integer NOT NULL,
    wfft_cargo_category character varying(16) NOT NULL,
    wfft_cargo character varying(16) NOT NULL,
    wfft_net integer NOT NULL,
    wfft_gross integer NOT NULL,
    wfft_destination_station integer NOT NULL,
    wfft_home_station integer NOT NULL,
    fk_form_train_id integer,
    wfft_number text NOT NULL
);
 *   DROP TABLE public.wagons_for_form_trains;
       public         heap    postgres    false            T          0    16558 
   all_trains 
   TABLE DATA           <   COPY public.all_trains (available_train_number) FROM stdin;
    public          postgres    false    223   �M       U          0    16565 
   all_wagons 
   TABLE DATA           <   COPY public.all_wagons (available_wagon_number) FROM stdin;
    public          postgres    false    224   U       M          0    16430    form_trains 
   TABLE DATA           x   COPY public.form_trains (form_id, form_wagons_amount, form_weight, form_number, form_current_date, isready) FROM stdin;
    public          postgres    false    216   @�       S          0    16480    neighbour_stations 
   TABLE DATA           X   COPY public.neighbour_stations (n_destination_station, n_neighbour_station) FROM stdin;
    public          postgres    false    222   ]�       R          0    16465    network_stations 
   TABLE DATA           @   COPY public.network_stations (station_1, station_2) FROM stdin;
    public          postgres    false    221   ��       V          0    16602 
   our_wagons 
   TABLE DATA           6   COPY public.our_wagons (number_our_wagon) FROM stdin;
    public          postgres    false    225   Ӧ       W          0    16659    reception_wagons 
   TABLE DATA           �   COPY public.reception_wagons (wagon_id, wagon_cargo_category, wagon_cargo, wagon_net, wagon_gross, wagon_destination_station, wagon_home_station, fk_train_id, wagon_number, recept_w_arrival_date) FROM stdin;
    public          postgres    false    226   �       L          0    16425    sent_trains 
   TABLE DATA           �   COPY public.sent_trains (sent_id, sent_wagons_amount, sent_arrival_station, sent_departure_date, sent_weight, sent_number) FROM stdin;
    public          postgres    false    215   �       O          0    16445    sent_wagons 
   TABLE DATA           �   COPY public.sent_wagons (sent_w_id, sent_w_cargo_category, sent_w_cargo, sent_w_net, sent_w_gross, sent_w_destination_station, sent_w_home_station, fk_sent_train_id, sent_w_number, sent_w_departure_date) FROM stdin;
    public          postgres    false    218   *�       X          0    16673    station_success_trains 
   TABLE DATA           G   COPY public.station_success_trains (quantity_empty_trains) FROM stdin;
    public          postgres    false    227   G�       Q          0    16460    stations 
   TABLE DATA           <   COPY public.stations (station_id, station_name) FROM stdin;
    public          postgres    false    220   d�       K          0    16420    trains 
   TABLE DATA           a   COPY public.trains (train_id, train_wagons_amount, train_arrival_date, train_number) FROM stdin;
    public          postgres    false    214   ��       N          0    16435    wagons 
   TABLE DATA           �   COPY public.wagons (wagon_id, wagon_cargo_category, wagon_cargo, wagon_net, wagon_gross, wagon_destination_station, wagon_home_station, fk_train_id, wagon_number) FROM stdin;
    public          postgres    false    217   ��       P          0    16455    wagons_for_form_trains 
   TABLE DATA           �   COPY public.wagons_for_form_trains (wfft_id, wfft_cargo_category, wfft_cargo, wfft_net, wfft_gross, wfft_destination_station, wfft_home_station, fk_form_train_id, wfft_number) FROM stdin;
    public          postgres    false    219   è       �           2606    16613    all_trains all_trains_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.all_trains
    ADD CONSTRAINT all_trains_pkey PRIMARY KEY (available_train_number);
 D   ALTER TABLE ONLY public.all_trains DROP CONSTRAINT all_trains_pkey;
       public            postgres    false    223            �           2606    16634    all_wagons all_wagons_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.all_wagons
    ADD CONSTRAINT all_wagons_pkey PRIMARY KEY (available_wagon_number);
 D   ALTER TABLE ONLY public.all_wagons DROP CONSTRAINT all_wagons_pkey;
       public            postgres    false    224            �           2606    16469 "   network_stations first_second_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.network_stations
    ADD CONSTRAINT first_second_pkey PRIMARY KEY (station_1, station_2);
 L   ALTER TABLE ONLY public.network_stations DROP CONSTRAINT first_second_pkey;
       public            postgres    false    221    221            �           2606    16434    form_trains form_trains_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.form_trains
    ADD CONSTRAINT form_trains_pkey PRIMARY KEY (form_id);
 F   ALTER TABLE ONLY public.form_trains DROP CONSTRAINT form_trains_pkey;
       public            postgres    false    216            �           2606    16484 -   neighbour_stations neighbour_destination_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.neighbour_stations
    ADD CONSTRAINT neighbour_destination_pkey PRIMARY KEY (n_destination_station, n_neighbour_station);
 W   ALTER TABLE ONLY public.neighbour_stations DROP CONSTRAINT neighbour_destination_pkey;
       public            postgres    false    222    222            �           2606    16429    sent_trains sent_trains_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.sent_trains
    ADD CONSTRAINT sent_trains_pkey PRIMARY KEY (sent_id);
 F   ALTER TABLE ONLY public.sent_trains DROP CONSTRAINT sent_trains_pkey;
       public            postgres    false    215            �           2606    16449    sent_wagons sent_wagons_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.sent_wagons
    ADD CONSTRAINT sent_wagons_pkey PRIMARY KEY (sent_w_id);
 F   ALTER TABLE ONLY public.sent_wagons DROP CONSTRAINT sent_wagons_pkey;
       public            postgres    false    218            �           2606    16464    stations stations_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.stations
    ADD CONSTRAINT stations_pkey PRIMARY KEY (station_id);
 @   ALTER TABLE ONLY public.stations DROP CONSTRAINT stations_pkey;
       public            postgres    false    220            �           2606    16424    trains trains_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.trains
    ADD CONSTRAINT trains_pkey PRIMARY KEY (train_id);
 <   ALTER TABLE ONLY public.trains DROP CONSTRAINT trains_pkey;
       public            postgres    false    214            �           2606    16459 2   wagons_for_form_trains wagons_for_form_trains_pkey 
   CONSTRAINT     u   ALTER TABLE ONLY public.wagons_for_form_trains
    ADD CONSTRAINT wagons_for_form_trains_pkey PRIMARY KEY (wfft_id);
 \   ALTER TABLE ONLY public.wagons_for_form_trains DROP CONSTRAINT wagons_for_form_trains_pkey;
       public            postgres    false    219            �           2606    16439    wagons wagons_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.wagons
    ADD CONSTRAINT wagons_pkey PRIMARY KEY (wagon_id);
 <   ALTER TABLE ONLY public.wagons DROP CONSTRAINT wagons_pkey;
       public            postgres    false    217            �           2606    16619 (   form_trains form_trains_form_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.form_trains
    ADD CONSTRAINT form_trains_form_number_fkey FOREIGN KEY (form_number) REFERENCES public.all_trains(available_train_number);
 R   ALTER TABLE ONLY public.form_trains DROP CONSTRAINT form_trains_form_number_fkey;
       public          postgres    false    216    223    3244            �           2606    16485 @   neighbour_stations neighbour_stations_n_destination_station_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.neighbour_stations
    ADD CONSTRAINT neighbour_stations_n_destination_station_fkey FOREIGN KEY (n_destination_station) REFERENCES public.stations(station_id);
 j   ALTER TABLE ONLY public.neighbour_stations DROP CONSTRAINT neighbour_stations_n_destination_station_fkey;
       public          postgres    false    3238    222    220            �           2606    16490 >   neighbour_stations neighbour_stations_n_neighbour_station_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.neighbour_stations
    ADD CONSTRAINT neighbour_stations_n_neighbour_station_fkey FOREIGN KEY (n_neighbour_station) REFERENCES public.stations(station_id);
 h   ALTER TABLE ONLY public.neighbour_stations DROP CONSTRAINT neighbour_stations_n_neighbour_station_fkey;
       public          postgres    false    222    220    3238            �           2606    16470 0   network_stations network_stations_station_1_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.network_stations
    ADD CONSTRAINT network_stations_station_1_fkey FOREIGN KEY (station_1) REFERENCES public.stations(station_id);
 Z   ALTER TABLE ONLY public.network_stations DROP CONSTRAINT network_stations_station_1_fkey;
       public          postgres    false    3238    220    221            �           2606    16475 0   network_stations network_stations_station_2_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.network_stations
    ADD CONSTRAINT network_stations_station_2_fkey FOREIGN KEY (station_2) REFERENCES public.stations(station_id);
 Z   ALTER TABLE ONLY public.network_stations DROP CONSTRAINT network_stations_station_2_fkey;
       public          postgres    false    3238    221    220            �           2606    16650 +   our_wagons our_wagons_number_our_wagon_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.our_wagons
    ADD CONSTRAINT our_wagons_number_our_wagon_fkey FOREIGN KEY (number_our_wagon) REFERENCES public.all_wagons(available_wagon_number);
 U   ALTER TABLE ONLY public.our_wagons DROP CONSTRAINT our_wagons_number_our_wagon_fkey;
       public          postgres    false    224    3246    225            �           2606    16624 (   sent_trains sent_trains_sent_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sent_trains
    ADD CONSTRAINT sent_trains_sent_number_fkey FOREIGN KEY (sent_number) REFERENCES public.all_trains(available_train_number);
 R   ALTER TABLE ONLY public.sent_trains DROP CONSTRAINT sent_trains_sent_number_fkey;
       public          postgres    false    215    3244    223            �           2606    16450 -   sent_wagons sent_wagons_fk_sent_train_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sent_wagons
    ADD CONSTRAINT sent_wagons_fk_sent_train_id_fkey FOREIGN KEY (fk_sent_train_id) REFERENCES public.sent_trains(sent_id);
 W   ALTER TABLE ONLY public.sent_wagons DROP CONSTRAINT sent_wagons_fk_sent_train_id_fkey;
       public          postgres    false    215    3228    218            �           2606    16645 *   sent_wagons sent_wagons_sent_w_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sent_wagons
    ADD CONSTRAINT sent_wagons_sent_w_number_fkey FOREIGN KEY (sent_w_number) REFERENCES public.all_wagons(available_wagon_number);
 T   ALTER TABLE ONLY public.sent_wagons DROP CONSTRAINT sent_wagons_sent_w_number_fkey;
       public          postgres    false    218    3246    224            �           2606    16614    trains trains_train_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.trains
    ADD CONSTRAINT trains_train_number_fkey FOREIGN KEY (train_number) REFERENCES public.all_trains(available_train_number);
 I   ALTER TABLE ONLY public.trains DROP CONSTRAINT trains_train_number_fkey;
       public          postgres    false    223    3244    214            �           2606    16440    wagons wagons_fk_train_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.wagons
    ADD CONSTRAINT wagons_fk_train_id_fkey FOREIGN KEY (fk_train_id) REFERENCES public.trains(train_id);
 H   ALTER TABLE ONLY public.wagons DROP CONSTRAINT wagons_fk_train_id_fkey;
       public          postgres    false    217    3226    214            �           2606    16503 C   wagons_for_form_trains wagons_for_form_trains_fk_form_train_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.wagons_for_form_trains
    ADD CONSTRAINT wagons_for_form_trains_fk_form_train_id_fkey FOREIGN KEY (fk_form_train_id) REFERENCES public.form_trains(form_id);
 m   ALTER TABLE ONLY public.wagons_for_form_trains DROP CONSTRAINT wagons_for_form_trains_fk_form_train_id_fkey;
       public          postgres    false    3230    219    216            �           2606    16640 >   wagons_for_form_trains wagons_for_form_trains_wfft_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.wagons_for_form_trains
    ADD CONSTRAINT wagons_for_form_trains_wfft_number_fkey FOREIGN KEY (wfft_number) REFERENCES public.all_wagons(available_wagon_number);
 h   ALTER TABLE ONLY public.wagons_for_form_trains DROP CONSTRAINT wagons_for_form_trains_wfft_number_fkey;
       public          postgres    false    224    3246    219            �           2606    16635    wagons wagons_wagon_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.wagons
    ADD CONSTRAINT wagons_wagon_number_fkey FOREIGN KEY (wagon_number) REFERENCES public.all_wagons(available_wagon_number);
 I   ALTER TABLE ONLY public.wagons DROP CONSTRAINT wagons_wagon_number_fkey;
       public          postgres    false    3246    217    224            T     x�%ҹ�0 A����N%�Aa���5�X������|���+!)%-#+�;�#.����r\��q9.��\��r]��u�.�庄K��K��K��K��K��K��K��K��K��K��K��K��K��K��K��K��K��K��K��K��˸�˸�˸�˸�˸�˺�˺�˺�˺�˺<���\��sy.��<��}9����R�2����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{�=�v�����a��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v/�����e��{ٽ�^v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��`7�v��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��d7�Mv��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��b��-v��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��f��mv��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��aw�v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v��ew�]v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v�����c����}�>v������g�Ϗ����H�F�      U      x�,٫�hWEA�hF�s�00q��xʯ��&��������������[n��{�s�?7~\{a/셽���^�{i/�������^�K{i/핽�W��^�+{e�약����^�k{m����������{co썽�7����{ko���������[{ko흽�w����;{g�읽���={�޳��={�޳��={����g�����}�>{����^����[n��{�s��#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#��}�>B���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G�#���H}�>R���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G��Q�(}�>J���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z���G����h}�>Z�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c�1�}�>F�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�����c���X}�>V�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������q�8}�>N�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ�O�>>}|�������ǧ��O�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y����o��~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����σ�?~�<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O    ~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ��^{����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�'?O~��<�y�����ϓ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^����ﵧ~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ    �?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϋ�?/~^���y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ��^{����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����ϛ�7?o~����y�����χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|��ﵧ~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�����    ��χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?~>�|�������χ�?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ��^{����ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������ϗ�/?_~��|�������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~����ﵧ~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���    ������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~���������Ϗ�??~~����������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?������?�������k�� ���S�ߥ����N�왑�����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?�������������������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�   <~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?���������y�<~?������]?�s���EA      M      x������ � �      S   I   x�̹�0���C�ԋ����� -�Иx��qC	%톖���ƴ\��l�(|P��kn����? 2_      R      x������ � �      V      x������ � �      W      x������ � �      L      x������ � �      O      x������ � �      X      x������ � �      Q     x�ePKN�@[3��nV R�w�0MJAH @e�BlX!%��iB�W���*$��(c��y\�D<�_Hѣ�aB��nm��5�M�.�j��
}T=��
	b���?%�+h�9Pk�U/hi�I�F�q�	����n⁎�#48?��������T
�qD�=�ּuV1��sg~ШCo��P+!�r_`I��.��dF�]崹�ڕ�7�k�[I�r� ��*�68�=�?�R%��W��w{P�-����Iv��"ռp�)�P̓����B�Ӱ!�      K      x������ � �      N      x������ � �      P      x������ � �     