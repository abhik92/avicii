from pandas_datareader import data
from datetime import datetime,timedelta

class Slam:

    def __init__(self, symbol, data_source, start_date, end_date):
        self.symbol = symbol
        self.data_source = data_source
        self.start_date = start_date
        self.end_date = end_date
        self.panel_data =  data.DataReader(self.symbol, self.data_source, self.start_date, self.end_date)

    def serve(self, days):
        x= (self.panel_data['Close'].loc[:]).rolling(window=days).mean()
        return x[-1]

    def lob(self, day):
        date = datetime.fromisoformat(day)
        while day not in self.panel_data['Close'] and date:
            date = date - timedelta(days=1)
            day = date.strftime("%Y-%m-%d")
        return self.panel_data['Close'][day]
