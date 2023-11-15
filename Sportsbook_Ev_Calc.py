import pandas as pd
import numpy as np

df = pd.read_excel(r"NA Excel File.xlsx")
df_eu = pd.read_excel(r"EU Excel File.xlsx") #importing sportsbooks data

def get_NA_bookmaker_data(bookmaker):
    return df[df.bookmaker == bookmaker].sort_values(by=['event_name']) 
def get_EU_bookmaker_data(bookmaker):
    return df_eu[df_eu.bookmaker == bookmaker].sort_values(by=['event_name']) #get a specific info for a specific bookamker
def add_EV_flag(bookmaker, pinnacle):
    bm = bookmaker.get_dataframe()
    pn = pinnacle.get_dataframe()
    counter_1 = 0
    counter_2 = 0
    flag_list = []
    while counter_1 < len(bm) and counter_2 < len(pn):
        if bm.iloc[counter_1,0] != pn.iloc[counter_2,0]:

            if bm.iloc[counter_1,0] in pn['event_name'].values:
                counter_2+=1

            else:
                flag_list.append('N/A')
                counter_1+=1

        elif bm.iloc[counter_1,5] != pn.iloc[counter_2,5] or bm.iloc[counter_1,6] != pn.iloc[counter_2,6]:
            flag_list.append(True)
            counter_1+= 1
            counter_2 +=1
        elif (abs(bm.iloc[counter_1,7] - pn.iloc[counter_2,7])>4) or (abs(bm.iloc[counter_1,8] - pn.iloc[counter_2,8])>4):
            flag_list.append(True)
            counter_1+= 1
            counter_2 +=1
        else:
            flag_list.append(False)
            counter_1+= 1
            counter_2 +=1
            # compares data to pinnacle data 
    bm['EV Flag'] = flag_list
    return bm
class bookmaker:
    def __init__(self, name,dataframe):
        self.name = name
        self.dataframe = dataframe
    def get_name(self):
        return self.name
    def get_dataframe(self):
        return self.dataframe
        
temp_1 = get_NA_bookmaker_data('Bovada')
temp_2 = get_EU_bookmaker_data('Pinnacle') # making sure we have unaltered copies
bovada = bookmaker('Bovada',get_NA_bookmaker_data('Bovada'))
pinnacle = bookmaker('Pinnacle',get_EU_bookmaker_data('Pinnacle'))
add_EV_flag(bovada, pinnacle)