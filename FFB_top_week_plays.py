import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
import sys
import re
import datetime

def main():

        while True:
            pos = input("Enter Position [QB, RB, WR & TE only]: ").lower()
            if pos == 'qb':
                pos = '1'
            else:
                pass
            if pos == 'rb':
                pos = '2'
            else:
                pass
            if pos == 'wr':
                pos = '3'
            else:
                pass
            if pos == 'te':
                pos = '4'
            else:
                pass
            if pos in ['1', '2', '3', '4']:
                break
            else:
                print('**~INVALID INPUT~** --> Only accepts; QB, RB, WR, TE')

        global qb_name
        global sk_name

        while True:
            year = int(input("Enter Year [~ONLY LAST DECADE~]: "))
            if year in [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]:
                break
            else:
                print('**~INVALID INPUT~** --> Only accepts integers; 2011 - 2019')

        while True:
            week = int(input("Enter Week: "))
            if week in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
                break
            else:
                print('**~INVALID INPUT~** --> Only accepts integers;[weeks] 1 - 17')


        launch_week_3 = datetime.date(2019, 9, 19)
        launch_week_4 = datetime.date(2019, 9, 26)
        launch_week_5 = datetime.date(2019, 10, 3)
        launch_week_6 = datetime.date(2019, 10, 10)
        launch_week_7 = datetime.date(2019, 10, 17)
        launch_week_8 = datetime.date(2019, 10, 24)
        launch_week_9 = datetime.date(2019, 10, 31)
        launch_week_10 = datetime.date(2019, 11, 7)
        launch_week_11 = datetime.date(2019, 11, 14)
        launch_week_12 = datetime.date(2019, 11, 21)
        launch_week_13 = datetime.date(2019, 11, 28)
        launch_week_14 = datetime.date(2019, 12, 5)
        launch_week_15 = datetime.date(2019, 12, 12)
        launch_week_16 = datetime.date(2019, 12, 19)
        launch_week_17 = datetime.date(2019, 12, 26)
        #print(datetime.date.today())
        qb_ind_count = 42
        sk_ind_count = 45

        payload = {"position":pos,"sort":"pts","statCategory":"stats","statSeason":year,"statType":"weekStats","statWeek":week}

        #payload = {"position":str(position),"offset":"1","position":"3","sort":"pts","statCategory":"stats","statSeason":str(year),"statType":"weekStats","statWeek":str(week)}
        url = 'https://fantasy.nfl.com/research/scoringleaders'
        response = requests.get(url,params=payload)

        #Respoonse of 200 means website is scrapable
        print("Response:", response.status_code,response.url)
        print('')

        soup = BeautifulSoup(response.text,'html.parser')

        table_player_name = []
        player_names = soup.find_all('a')
        for name in player_names:
            table_player_name.append(name.text)
        all_names = table_player_name
        all_names = [x for x in all_names if x !='View Videos']
        all_names = [x for x in all_names if x !='View News']
        #print(all_names)
        qb_in_num = 56
        sk_in_num = 59
        #sys.exit()

        if year==2019:
            qb_ind_count = qb_ind_count
            sk_ind_count = sk_ind_count
            qb_name = all_names[qb_ind_count:]
            sk_name = all_names[sk_ind_count:]
            if pos==1 or pos==2 or pos==3 or pos==4:
                    if launch_week_3 < datetime.date.today():
                        qb_ind_count += 1
                        sk_ind_count += 1
                        qb_name = all_names[qb_ind_count:]
                        sk_name = all_names[sk_ind_count:]
                        if launch_week_4 < datetime.date.today():
                            qb_ind_count += 1
                            sk_ind_count += 1
                            qb_name = all_names[qb_ind_count:]
                            sk_name = all_names[sk_ind_count:]
                            if launch_week_5 < datetime.date.today():
                                qb_ind_count += 1
                                sk_ind_count += 1
                                qb_name = all_names[qb_ind_count:]
                                sk_name = all_names[sk_ind_count:]
                                if launch_week_6 < datetime.date.today():
                                    qb_ind_count += 1
                                    sk_ind_count += 1
                                    qb_name = all_names[qb_ind_count:]
                                    sk_name = all_names[sk_ind_count:]
                                    if launch_week_7 < datetime.date.today():
                                        qb_ind_count += 1
                                        sk_ind_count += 1
                                        qb_name = all_names[qb_ind_count:]
                                        sk_name = all_names[sk_ind_count:]
                                        if launch_week_8 < datetime.date.today():
                                            qb_ind_count += 1
                                            sk_ind_count += 1
                                            qb_name = all_names[qb_ind_count:]
                                            sk_name = all_names[sk_ind_count:]
                                            if launch_week_9 < datetime.date.today():
                                                qb_ind_count += 1
                                                sk_ind_count += 1
                                                qb_name = all_names[qb_ind_count:]
                                                sk_name = all_names[sk_ind_count:]
                                                if launch_week_10 < datetime.date.today():
                                                    qb_ind_count += 1
                                                    sk_ind_count += 1
                                                    qb_name = all_names[qb_ind_count:]
                                                    sk_name = all_names[sk_ind_count:]
                                                    if launch_week_11 < datetime.date.today():
                                                        qb_ind_count += 1
                                                        sk_ind_count += 1
                                                        qb_name = all_names[qb_ind_count:]
                                                        sk_name = all_names[sk_ind_count:]
                                                        if launch_week_12 < datetime.date.today():
                                                            qb_ind_count += 1
                                                            sk_ind_count += 1
                                                            qb_name = all_names[qb_ind_count:]
                                                            sk_name = all_names[sk_ind_count:]
                                                            if launch_week_13 < datetime.date.today():
                                                                qb_ind_count += 1
                                                                sk_ind_count += 1
                                                                qb_name = all_names[qb_ind_count:]
                                                                sk_name = all_names[sk_ind_count:]
                                                                if launch_week_14 < datetime.date.today():
                                                                    qb_ind_count += 1
                                                                    sk_ind_count += 1
                                                                    qb_name = all_names[qb_ind_count:]
                                                                    sk_name = all_names[sk_ind_count:]
                                                                    if launch_week_15 < datetime.date.today():
                                                                        qb_ind_count += 1
                                                                        sk_ind_count += 1
                                                                        qb_name = all_names[qb_ind_count:]
                                                                        sk_name = all_names[sk_ind_count:]
                                                                        if launch_week_16 < datetime.date.today():
                                                                            qb_ind_count += 1
                                                                            sk_ind_count += 1
                                                                            qb_name = all_names[qb_ind_count:]
                                                                            sk_name = all_names[sk_ind_count:]
                                                                            if launch_week_17 < datetime.date.today():
                                                                                qb_ind_count += 1
                                                                                sk_ind_count += 1
                                                                                qb_name = all_names[qb_ind_count:]
                                                                                sk_name = all_names[sk_ind_count:]
                                                                            else:
                                                                                qb_ind_count = qb_ind_count
                                                                                sk_ind_count = sk_ind_count
                                                                        else:
                                                                            qb_ind_count = qb_ind_count
                                                                            sk_ind_count = sk_ind_count
                                                                    else:
                                                                        qb_ind_count = qb_ind_count
                                                                        sk_ind_count = sk_ind_count
                                                                else:
                                                                    qb_ind_count = qb_ind_count
                                                                    sk_ind_count = sk_ind_count
                                                            else:
                                                                qb_ind_count = qb_ind_count
                                                                sk_ind_count = sk_ind_count
                                                        else:
                                                            qb_ind_count = qb_ind_count
                                                            sk_ind_count = sk_ind_count
                                                    else:
                                                        qb_ind_count = qb_ind_count
                                                        sk_ind_count = sk_ind_count
                                                else:
                                                    qb_ind_count = qb_ind_count
                                                    sk_ind_count = sk_ind_count
                                            else:
                                                qb_ind_count = qb_ind_count
                                                sk_ind_count = sk_ind_count
                                        else:
                                            qb_ind_count = qb_ind_count
                                            sk_ind_count = sk_ind_count
                                    else:
                                        qb_ind_count = qb_ind_count
                                        sk_ind_count = sk_ind_count
                                else:
                                    qb_ind_count = qb_ind_count
                                    sk_ind_count = sk_ind_count
                            else:
                                qb_ind_count = qb_ind_count
                                sk_ind_count = sk_ind_count
                        else:
                            qb_ind_count = qb_ind_count
                            sk_ind_count = sk_ind_count
                    else:
                        qb_ind_count = qb_ind_count
                        sk_ind_count = sk_ind_count
            else:
                    qb_ind_count = qb_ind_count
                    sk_ind_count = sk_ind_count

            if qb_ind_count > 0 or sk_ind_count > 0:
                qb_name = all_names[qb_ind_count:]
                sk_name = all_names[sk_ind_count:]
            else:
                pass
        else:
            qb_name = all_names[qb_in_num:]
            sk_name = all_names[sk_in_num:]

        #print(qb_name)
        #print(sk_name)

        columnHeader = []
        #grabbing headers
        #HEADERS -> [0]Passing, [1]Rushing, [2]Receiving, [3]Ret, [4]Misc, [5]Fum, [6]Fantasy, [7]Rank, [8]Opp
        headers = soup.find('table', {'class':'tableType-player hasGroups'}).find_all('th')
        for head in headers:
            columnHeader.append(head.text)

        tableNum = []
        numbers = soup.find('table', {'class':'tableType-player hasGroups'}).find_all('span')
        for num in numbers:
            tableNum.append(num.text)
        values = tableNum
        vals = values[9:]
        vals = [v.replace('-','0') for v in vals] #changing all values to numbers
        vals = [float(v) for v in vals] #converting all values to floats
        #print(vals)

        #Setting table to pull opponents from
        table_opponent = []
        opp_names = soup.find_all('td')
        #print(opp_names)
        for opp in opp_names:
            table_opponent.append(opp.text)
        opponents = table_opponent
        ##############################################################################
        ##############################START QB########################################
        ##############################################################################

        if pos == '1':

            qb_name_1 = qb_name[0]
            print('')
            print("Num. 1 QB on Week",week)
            print(qb_name_1)
            print('Opp:',opponents[2])
            print('Passing Statistics:','Yards ->',vals[0],'TD ->',vals[1],'INT ->',vals[2])

            if sum(vals[3:5]) > 0:
                if vals[3] > 0:
                    print('Rushing Yards ->',vals[3])
                else:
                    pass
                if vals[4] > 0:
                    print('Rushig TD ->', vals[4])
                else:
                    pass
            else:
                pass
            if sum(vals[5:12]) > 0:
                if vals[5] > 0:
                    print('Receptions ->',vals[5])
                else:
                    pass
                if vals[6] > 0:
                    print('Rec. Yards ->',vals[6])
                else:
                    pass
                if vals[7] > 0:
                    print('Rec. TD ->',vals[7])
                else:
                    pass
                if vals[8] > 0:
                    print('Ret. TD ->',vals[8])
                else:
                    pass
                if vals[9] > 0:
                    print('Fumble Recovered for TD ->',vals[9])
                else:
                    pass
                if vals[10] > 0:
                    print('2PT Conv ->',vals[10])
                else:
                    pass
                if vals[11] > 0:
                    print('Fumble Lost ->',vals[11])
                else:
                    pass
            else:
                pass
            print('TOTAL QB POINTS:',vals[12])

            qb_name_2 = qb_name[1]
            print('')
            print("Num. 2 QB on Week ",week)
            print(qb_name_2)
            print('Opp:',opponents[18])
            print('Passing Statistics:','Yards ->',vals[13],'TD ->',vals[14],'INT ->',vals[15])

            if sum(vals[16:18]) > 0:
                if vals[16] > 0:
                    print('Rushing Yards ->',vals[16])
                else:
                    pass
                if vals[17] > 0:
                    print('Rushig TD ->', vals[17])
                else:
                    pass
            else:
                pass
            if sum(vals[18:25]) > 0:
                if vals[18] > 0:
                    print('Receptions ->',vals[18])
                else:
                    pass
                if vals[19] > 0:
                    print('Rec. Yards ->',vals[19])
                else:
                    pass
                if vals[20] > 0:
                    print('Rec. TD ->',vals[20])
                else:
                    pass
                if vals[21] > 0:
                    print('Ret. TD ->',vals[21])
                else:
                    pass
                if vals[22] > 0:
                    print('Fumble Recovered for TD ->',vals[22])
                else:
                    pass
                if vals[23] > 0:
                    print('2PT Conv ->',vals[23])
                else:
                    pass
                if vals[24] > 0:
                    print('Fumble Lost ->',vals[24])
                else:
                    pass
            else:
                pass
            print('TOTAL QB POINTS:',vals[25])

            qb_name_3 = qb_name[2]
            print('')
            print("Num. 3 QB on Week ",week)
            print(qb_name_3)
            print('Opp:',opponents[34])
            print('Passing Statistics:','Yards ->',vals[26],'TD ->',vals[27],'INT ->',vals[28])

            if sum(vals[29:31]) > 0:
                if vals[31] > 0:
                    print('Rushing Yards ->',vals[31])
                else:
                    pass
                if vals[32] > 0:
                    print('Rushig TD ->', vals[32])
                else:
                    pass
            else:
                pass
            if sum(vals[31:38]) > 0:
                if vals[31] > 0:
                    print('Receptions ->',vals[31])
                else:
                    pass
                if vals[32] > 0:
                    print('Rec. Yards ->',vals[32])
                else:
                    pass
                if vals[33] > 0:
                    print('Rec. TD ->',vals[33])
                else:
                    pass
                if vals[34] > 0:
                    print('Ret. TD ->',vals[34])
                else:
                    pass
                if vals[35] > 0:
                    print('Fumble Recovered for TD ->',vals[35])
                else:
                    pass
                if vals[36] > 0:
                    print('2PT Conv ->',vals[36])
                else:
                    pass
                if vals[37] > 0:
                    print('Fumble Lost ->',vals[37])
                else:
                    pass
            else:
                pass
            print('TOTAL QB POINTS:',vals[38])

            qb_name_4 = qb_name[3]
            print('')
            print("Num. 4 QB on Week ",week)
            print(qb_name_4)
            print('Opp:',opponents[50])
            print('Passing Statistics:','Yards ->',vals[39],'TD ->',vals[40],'INT ->',vals[41])

            if sum(vals[42:44]) > 0:
                if vals[42] > 0:
                    print('Rushing Yards ->',vals[42])
                else:
                    pass
                if vals[43] > 0:
                    print('Rushig TD ->', vals[43])
                else:
                    pass
            else:
                pass
            if sum(vals[44:51]) > 0:
                if vals[44] > 0:
                    print('Receptions ->',vals[44])
                else:
                    pass
                if vals[45] > 0:
                    print('Rec. Yards ->',vals[45])
                else:
                    pass
                if vals[46] > 0:
                    print('Rec. TD ->',vals[46])
                else:
                    pass
                if vals[47] > 0:
                    print('Ret. TD ->',vals[47])
                else:
                    pass
                if vals[48] > 0:
                    print('Fumble Recovered for TD ->',vals[48])
                else:
                    pass
                if vals[49] > 0:
                    print('2PT Conv ->',vals[49])
                else:
                    pass
                if vals[50] > 0:
                    print('Fumble Lost ->',vals[50])
                else:
                    pass
            else:
                pass
            print('TOTAL QB POINTS:',vals[51])

            qb_name_5 = qb_name[4]
            print('')
            print("Num. 5 QB on Week ",week)
            print(qb_name_5)
            print('Opp:',opponents[66])
            print('Passing Statistics:','Yards ->',vals[52],'TD ->',vals[53],'INT ->',vals[54])

            if sum(vals[55:57]) > 0:
                if vals[55] > 0:
                    print('Rushing Yards ->',vals[55])
                else:
                    pass
                if vals[56] > 0:
                    print('Rushig TD ->', vals[56])
                else:
                    pass
            else:
                pass
            if sum(vals[57:64]) > 0:
                if vals[57] > 0:
                    print('Receptions ->',vals[57])
                else:
                    pass
                if vals[58] > 0:
                    print('Rec. Yards ->',vals[58])
                else:
                    pass
                if vals[59] > 0:
                    print('Rec. TD ->',vals[59])
                else:
                    pass
                if vals[60] > 0:
                    print('Ret. TD ->',vals[60])
                else:
                    pass
                if vals[61] > 0:
                    print('Fumble Recovered for TD ->',vals[61])
                else:
                    pass
                if vals[62] > 0:
                    print('2PT Conv ->',vals[62])
                else:
                    pass
                if vals[63] > 0:
                    print('Fumble Lost ->',vals[63])
                else:
                    pass
            else:
                pass
            print('TOTAL QB POINTS:',vals[64])

        else:
            pass
        #~QB DONE~#

        ##############################################################################
        ##############################START RB########################################
        ##############################################################################

        if pos == '2':

            rb_name_1 = sk_name[0]
            print('')
            print("Num. 1 RB on Week "+str(week))
            print(rb_name_1)
            print('Opp:',opponents[2])
            print('Rushing Statistics:','Yards ->',vals[3],'TD ->',vals[4])

            if sum(vals[0:3]) > 0:
                print('Passing Statistics:','Yards ->',vals[0])
                if vals[1] > 0:
                    print('TD ->',vals[1])
                else:
                    pass
                if vals[2] > 0:
                    print('INT ->',vals[2])
                else:
                    pass
            else:
                pass
            if sum(vals[5:8]) > 0:
                print('Recieving Statistics:','Receptions ->',vals[5],'Yards ->',vals[6])
                if vals[7] > 0:
                    print('TD ->',vals[7])
                else:
                    pass
            else:
                pass
            if vals[8] > 0:
                print('Ret. TD ->',vals[8])
            else:
                pass
            if vals[9] > 0:
                print('Fumble Recovered for TD ->',vals[9])
            else:
                pass
            if vals[10] > 0:
                print('2PT Conv ->',vals[10])
            else:
                pass
            if vals[11] > 0:
                print('Fumble Lost ->',vals[11])
            else:
                pass

            print('TOTAL RB POINTS:',vals[12])

            rb_name_2 = sk_name[1]
            print('')
            print("Num. 2 RB on Week "+str(week))
            print(rb_name_2)
            print('Opp:',opponents[18])
            print('Rushing Statistics:','Yards ->',vals[16],'TD ->',vals[17])

            if sum(vals[13:16]) > 0:
                print('Passing Statistics:','Yards ->',vals[13])
                if vals[14] > 0:
                    print('TD ->',vals[14])
                else:
                    pass
                if vals[15] > 0:
                    print('INT ->',vals[15])
                else:
                    pass
            else:
                pass
            if sum(vals[18:21]) > 0:
                print('Recieving Statistics:','Receptions ->',vals[18],'Yards ->',vals[19])
                if vals[20] > 0:
                    print('TD ->',vals[20])
                else:
                    pass
            else:
                pass
            if vals[21] > 0:
                print('Ret. TD ->',vals[21])
            else:
                pass
            if vals[22] > 0:
                print('Fumble Recovered for TD ->',vals[22])
            else:
                pass
            if vals[23] > 0:
                print('2PT Conv ->',vals[23])
            else:
                pass
            if vals[24] > 0:
                print('Fumble Lost ->',vals[24])
            else:
                pass

            print('TOTAL RB POINTS:',vals[25])

            rb_name_3 = sk_name[2]
            print('')
            print("Num. 3 RB on week "+str(week))
            print(rb_name_3)
            print('Opp:',opponents[34])
            print('Rushing Statistics:','Yards ->',vals[30],'TD ->',vals[31])

            if sum(vals[26:29]) > 0:
                print('Passing Statistics:','Yards ->',vals[26])
                if vals[27] > 0:
                    print('TD ->',vals[27])
                else:
                    pass
                if vals[28] > 0:
                    print('INT ->',vals[28])
                else:
                    pass
            else:
                pass
            if sum(vals[31:34]) > 0:
                print('Recieving Statistics:','Receptions ->',vals[31],'Yards ->',vals[32])
                if vals[33] > 0:
                    print('TD ->',vals[33])
                else:
                    pass
            else:
                pass
            if vals[34] > 0:
                print('Ret. TD ->',vals[34])
            else:
                pass
            if vals[35] > 0:
                print('Fumble Recovered for TD ->',vals[35])
            else:
                pass
            if vals[36] > 0:
                print('2PT Conv ->',vals[36])
            else:
                pass
            if vals[37] > 0:
                print('Fumble Lost ->',vals[37])
            else:
                pass

            print('TOTAL RB POINTS:',vals[38])

            rb_name_4 = sk_name[3]
            print('')
            print("Num. 4 RB on week "+str(week))
            print(rb_name_4)
            print('Opp:',opponents[50])
            print('Rushing Statistics:','Yards ->',vals[42],'TD ->',vals[43])

            if sum(vals[39:42]) > 0:
                print('Passing Statistics:','Yards ->',vals[39])
                if vals[40] > 0:
                    print('TD ->',vals[40])
                else:
                    pass
                if vals[41] > 0:
                    print('INT ->',vals[41])
                else:
                    pass
            else:
                pass
            if sum(vals[44:47]) > 0:
                print('Recieving Statistics:','Receptions ->',vals[44],'Yards ->',vals[45])
                if vals[20] > 0:
                    print('TD ->',vals[46])
                else:
                    pass
            else:
                pass
            if vals[47] > 0:
                print('Ret. TD ->',vals[47])
            else:
                pass
            if vals[48] > 0:
                print('Fumble Recovered for TD ->',vals[48])
            else:
                pass
            if vals[49] > 0:
                print('2PT Conv ->',vals[49])
            else:
                pass
            if vals[50] > 0:
                print('Fumble Lost ->',vals[50])
            else:
                pass

            print('TOTAL RB POINTS:',vals[51])

            rb_name_5 = sk_name[4]
            print('')
            print("Num. 5 RB on week "+str(week))
            print(rb_name_5)
            print('Opp:',opponents[66])
            print('Rushing Statistics:','Yards ->',vals[55],'TD ->',vals[56])

            if sum(vals[52:55]) > 0:
                print('Passing Statistics:','Yards ->',vals[52])
                if vals[53] > 0:
                    print('TD ->',vals[53])
                else:
                    pass
                if vals[54] > 0:
                    print('INT ->',vals[54])
                else:
                    pass
            else:
                pass
            if sum(vals[57:60]) > 0:
                print('Recieving Statistics:','Receptions ->',vals[57],'Yards ->',vals[58])
                if vals[59] > 0:
                    print('TD ->',vals[59])
                else:
                    pass
            else:
                pass
            if vals[60] > 0:
                print('Ret. TD ->',vals[60])
            else:
                pass
            if vals[61] > 0:
                print('Fumble Recovered for TD ->',vals[61])
            else:
                pass
            if vals[62] > 0:
                print('2PT Conv ->',vals[62])
            else:
                pass
            if vals[63] > 0:
                print('Fumble Lost ->',vals[63])
            else:
                pass

            print('TOTAL RB POINTS:',vals[64])

        else:
            pass
        #~RB DONE~#

        ##############################################################################
        ##############################START WR########################################
        ##############################################################################

        if pos == '3':

            wr_name_1 = sk_name[0]
            print('')
            print("Num. 1 WR on week "+str(week))
            print(wr_name_1)
            print('Opp:',opponents[2])
            print('Recieving Statistics:','Receptions ->',vals[5],'Yards ->',vals[6],'TD ->',vals[7])

            if sum(vals[0:3]) > 0:
                print('Passing Statistics:','Yards ->',vals[0])
                if vals[1] > 0:
                    print('TD ->',vals[1])
                else:
                    pass
                if vals[2] > 0:
                    print('INT ->',vals[2])
                else:
                    pass
            else:
                pass
            if sum(vals[3:5]) > 0:
                print('Rushing Statistics: Yards ->',vals[3])
                if vals[4]:
                    print('TD ->',vals[4])
                else:
                    pass
            else:
                pass
            if sum(vals[8:12]):
                if vals[8] > 0:
                    print('Return TD ->',vals[8])
                else:
                    pass
                if vals[9] > 0:
                    print('Fumble Recovered for TD ->',vals[9])
                else:
                    pass
                if vals[10] > 0:
                    print('2PT Conv ->',vals[10])
                else:
                    pass
                if vals[11] > 0:
                    print('Fumble Lost ->',vals[11])
                else:
                    pass
            else:
                pass
            print('TOTAL WR POINTS:',vals[12])

            wr_name_2 = sk_name[1]
            print('')
            print("Num. 2 WR on week "+str(week))
            print(wr_name_2)
            print('Opp:',opponents[18])
            print('Recieving Statistics:','Receptions ->',vals[18],'Yards ->',vals[19],'TD ->',vals[20])

            if sum(vals[13:16]) > 0:
                print('Passing Statistics:','Yards ->',vals[13])
                if vals[14] > 0:
                    print('TD ->',vals[14])
                else:
                    pass
                if vals[15] > 0:
                    print('INT ->',vals[15])
                else:
                    pass
            else:
                pass
            if sum(vals[16:18]) > 0:
                print('Rushing Statistics: Yards ->',vals[16])
                if vals[17]:
                    print('TD ->',vals[17])
                else:
                    pass
            else:
                pass
            if sum(vals[21:25]):
                if vals[21] > 0:
                    print('Return TD ->',vals[21])
                else:
                    pass
                if vals[22] > 0:
                    print('Fumble Recovered for TD ->',vals[22])
                else:
                    pass
                if vals[23] > 0:
                    print('2PT Conv ->',vals[23])
                else:
                    pass
                if vals[24] > 0:
                    print('Fumble Lost ->',vals[24])
                else:
                    pass
            else:
                pass
            print('TOTAL WR POINTS:',vals[25])

            wr_name_3 = sk_name[2]
            print('')
            print("Num. 3 WR on week "+str(week))
            print(wr_name_3)
            print('Opp:',opponents[34])
            print('Recieving Statistics:','Receptions ->',vals[31],'Yards ->',vals[32],'TD ->',vals[33])

            if sum(vals[26:29]) > 0:
                print('Passing Statistics:','Yards ->',vals[26])
                if vals[27] > 0:
                    print('TD ->',vals[27])
                else:
                    pass
                if vals[28] > 0:
                    print('INT ->',vals[28])
                else:
                    pass
            else:
                pass
            if sum(vals[29:31]) > 0:
                print('Rushing Statistics: Yards ->',vals[29])
                if vals[30]:
                    print('TD ->',vals[30])
                else:
                    pass
            else:
                pass
            if sum(vals[34:38]):
                if vals[34] > 0:
                    print('Return TD ->',vals[34])
                else:
                    pass
                if vals[35] > 0:
                    print('Fumble Recovered for TD ->',vals[35])
                else:
                    pass
                if vals[36] > 0:
                    print('2PT Conv ->',vals[36])
                else:
                    pass
                if vals[37] > 0:
                    print('Fumble Lost ->',vals[37])
                else:
                    pass
            else:
                pass
            print('TOTAL WR POINTS:',vals[38])

            wr_name_4 = sk_name[3]
            print('')
            print("Num. 4 WR on week "+str(week))
            print(wr_name_4)
            print('Opp:',opponents[50])
            print('Recieving Statistics:','Receptions ->',vals[44],'Yards ->',vals[45],'TD ->',vals[46])

            if sum(vals[39:42]) > 0:
                print('Passing Statistics:','Yards ->',vals[39])
                if vals[40] > 0:
                    print('TD ->',vals[41])
                else:
                    pass
                if vals[42] > 0:
                    print('INT ->',vals[42])
                else:
                    pass
            else:
                pass
            if sum(vals[42:44]) > 0:
                print('Rushing Statistics: Yards ->',vals[42])
                if vals[43]:
                    print('TD ->',vals[43])
                else:
                    pass
            else:
                pass
            if sum(vals[47:51]):
                if vals[47] > 0:
                    print('Return TD ->',vals[47])
                else:
                    pass
                if vals[48] > 0:
                    print('Fumble Recovered for TD ->',vals[48])
                else:
                    pass
                if vals[49] > 0:
                    print('2PT Conv ->',vals[49])
                else:
                    pass
                if vals[50] > 0:
                    print('Fumble Lost ->',vals[50])
                else:
                    pass
            else:
                pass
            print('TOTAL WR POINTS:',vals[51])

            wr_name_5 = sk_name[4]
            print('')
            print("Num. 5 WR on week "+str(week))
            print(wr_name_5)
            print('Opp:',opponents[66])
            print('Recieving Statistics:','Receptions ->',vals[57],'Yards ->',vals[58],'TD ->',vals[59])

            if sum(vals[52:55]) > 0:
                print('Passing Statistics:','Yards ->',vals[52])
                if vals[53] > 0:
                    print('TD ->',vals[53])
                else:
                    pass
                if vals[54] > 0:
                    print('INT ->',vals[54])
                else:
                    pass
            else:
                pass
            if sum(vals[55:57]) > 0:
                print('Rushing Statistics: Yards ->',vals[55])
                if vals[56]:
                    print('TD ->',vals[56])
                else:
                    pass
            else:
                pass
            if sum(vals[60:64]):
                if vals[60] > 0:
                    print('Return TD ->',vals[60])
                else:
                    pass
                if vals[61] > 0:
                    print('Fumble Recovered for TD ->',vals[61])
                else:
                    pass
                if vals[62] > 0:
                    print('2PT Conv ->',vals[62])
                else:
                    pass
                if vals[63] > 0:
                    print('Fumble Lost ->',vals[63])
                else:
                    pass
            else:
                pass
            print('TOTAL WR POINTS:',vals[51])

        else:
            pass
        #~WR DONE~#

        ##############################################################################
        ##############################START TE########################################
        ##############################################################################

        if pos == '4':

            te_name_1 = sk_name[0]
            print('')
            print("Num. 1 TE on week "+str(week))
            print(te_name_1)
            print('Opp:',opponents[2])
            print('Recieving Statistics:','Receptions ->',vals[5],'Yards ->',vals[6],'TD ->',vals[7])

            if sum(vals[0:3]) > 0:
                print('Passing Statistics:','Yards ->',vals[0])
                if vals[1] > 0:
                    print('TD ->',vals[1])
                else:
                    pass
                if vals[2] > 0:
                    print('INT ->',vals[2])
                else:
                    pass
            else:
                pass
            if sum(vals[3:5]) > 0:
                print('Rushing Statistics: Yards ->',vals[3])
                if vals[4]:
                    print('TD ->',vals[4])
                else:
                    pass
            else:
                pass
            if sum(vals[8:12]):
                if vals[8] > 0:
                    print('Return TD ->',vals[8])
                else:
                    pass
                if vals[9] > 0:
                    print('Fumble Recovered for TD ->',vals[9])
                else:
                    pass
                if vals[10] > 0:
                    print('2PT Conv ->',vals[10])
                else:
                    pass
                if vals[11] > 0:
                    print('Fumble Lost ->',vals[11])
                else:
                    pass
            else:
                pass
            print('TOTAL TE POINTS:',vals[12])

            te_name_2 = sk_name[1]
            print('')
            print("Num. 2 TE on week "+str(week))
            print(te_name_2)
            print('Opp:',opponents[18])
            print('Recieving Statistics:','Receptions ->',vals[18],'Yards ->',vals[19],'TD ->',vals[20])

            if sum(vals[13:16]) > 0:
                print('Passing Statistics:','Yards ->',vals[13])
                if vals[14] > 0:
                    print('TD ->',vals[14])
                else:
                    pass
                if vals[15] > 0:
                    print('INT ->',vals[15])
                else:
                    pass
            else:
                pass
            if sum(vals[16:18]) > 0:
                print('Rushing Statistics: Yards ->',vals[16])
                if vals[17]:
                    print('TD ->',vals[17])
                else:
                    pass
            else:
                pass
            if sum(vals[21:25]):
                if vals[21] > 0:
                    print('Return TD ->',vals[21])
                else:
                    pass
                if vals[22] > 0:
                    print('Fumble Recovered for TD ->',vals[22])
                else:
                    pass
                if vals[23] > 0:
                    print('2PT Conv ->',vals[23])
                else:
                    pass
                if vals[24] > 0:
                    print('Fumble Lost ->',vals[24])
                else:
                    pass
            else:
                pass
            print('TOTAL TE POINTS:',vals[25])

            te_name_3 = sk_name[2]
            print('')
            print("Num. 3 TE on week "+str(week))
            print(te_name_3)
            print('Opp:',opponents[34])
            print('Recieving Statistics:','Receptions ->',vals[31],'Yards ->',vals[32],'TD ->',vals[33])

            if sum(vals[26:29]) > 0:
                print('Passing Statistics:','Yards ->',vals[26])
                if vals[27] > 0:
                    print('TD ->',vals[27])
                else:
                    pass
                if vals[28] > 0:
                    print('INT ->',vals[28])
                else:
                    pass
            else:
                pass
            if sum(vals[29:31]) > 0:
                print('Rushing Statistics: Yards ->',vals[29])
                if vals[30]:
                    print('TD ->',vals[30])
                else:
                    pass
            else:
                pass
            if sum(vals[34:38]):
                if vals[34] > 0:
                    print('Return TD ->',vals[34])
                else:
                    pass
                if vals[35] > 0:
                    print('Fumble Recovered for TD ->',vals[35])
                else:
                    pass
                if vals[36] > 0:
                    print('2PT Conv ->',vals[36])
                else:
                    pass
                if vals[37] > 0:
                    print('Fumble Lost ->',vals[37])
                else:
                    pass
            else:
                pass
            print('TOTAL POINTS:',vals[38])

            te_name_4 = sk_name[3]
            print('')
            print("Num. 4 TE on week "+str(week))
            print(te_name_4)
            print('Opp:',opponents[50])
            print('Recieving Statistics:','Receptions ->',vals[44],'Yards ->',vals[45],'TD ->',vals[46])

            if sum(vals[39:42]) > 0:
                print('Passing Statistics:','Yards ->',vals[39])
                if vals[40] > 0:
                    print('TD ->',vals[41])
                else:
                    pass
                if vals[42] > 0:
                    print('INT ->',vals[42])
                else:
                    pass
            else:
                pass
            if sum(vals[42:44]) > 0:
                print('Rushing Statistics: Yards ->',vals[42])
                if vals[43]:
                    print('TD ->',vals[43])
                else:
                    pass
            else:
                pass
            if sum(vals[47:51]):
                if vals[47] > 0:
                    print('Return TD ->',vals[47])
                else:
                    pass
                if vals[48] > 0:
                    print('Fumble Recovered for TD ->',vals[48])
                else:
                    pass
                if vals[49] > 0:
                    print('2PT Conv ->',vals[49])
                else:
                    pass
                if vals[50] > 0:
                    print('Fumble Lost ->',vals[50])
                else:
                    pass
            else:
                pass
            print('TOTAL TE POINTS:',vals[51])

            te_name_5 = sk_name[4]
            print('')
            print("Num. 5 TE on week "+str(week))
            print(te_name_5)
            print('Opp:',opponents[66])
            print('Recieving Statistics:','Receptions ->',vals[57],'Yards ->',vals[58],'TD ->',vals[59])

            if sum(vals[52:55]) > 0:
                print('Passing Statistics:','Yards ->',vals[52])
                if vals[53] > 0:
                    print('TD ->',vals[53])
                else:
                    pass
                if vals[54] > 0:
                    print('INT ->',vals[54])
                else:
                    pass
            else:
                pass
            if sum(vals[55:57]) > 0:
                print('Rushing Statistics: Yards ->',vals[55])
                if vals[56]:
                    print('TD ->',vals[56])
                else:
                    pass
            else:
                pass
            if sum(vals[60:64]):
                if vals[60] > 0:
                    print('Return TD ->',vals[60])
                else:
                    pass
                if vals[61] > 0:
                    print('Fumble Recovered for TD ->',vals[61])
                else:
                    pass
                if vals[62] > 0:
                    print('2PT Conv ->',vals[62])
                else:
                    pass
                if vals[63] > 0:
                    print('Fumble Lost ->',vals[63])
                else:
                    pass
            else:
                pass
            print('TOTAL TE POINTS:',vals[51])

        else:
            pass
        #~TE DONE~#
    ##############################################################################
    ##############################################################################

        restart = input('Go Again? [y or n]: ').lower()
        if restart =='y':
            main()
        else:
            print("Goodbye..")
            exit()

print('Hello! Welcome to my application.\n'\
        'This program pulls information from fantasy.nfl.com/research/scoringleaders\n'\
        'and returns the top 5 players by position for the week and year specified.\n'\
        '\n''**~Program is only able to pull Skill Positions (QB, RB, WR & TE).\n')
main()


#The point of this program is to demonstrate webscraping, loops, and logical skills
