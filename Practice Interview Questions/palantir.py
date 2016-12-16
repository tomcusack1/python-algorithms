class InsiderTraders(object):

    def __init__(self):
        self.raw_data = []
        self.trader_data = {}
        self.trade_data = {}

    def input(self, data):
        self.raw_data.append(data)

    def organise_data(self):
        for i in self.raw_data:
            if len(i) == 2:
                self.trade_data[i[0]] = i[1]
            else:
                self.trader_data[i[0]] = (i[1], i[2], i[3])

    def result(self):
        return self.trader_data


trading_analysis = InsiderTraders()
lines = [line.rstrip('\n') for line in open('data.txt')]
for data_input in lines:
    trading_analysis.input(data_input.split('|'))
trading_analysis.organise_data()
print(trading_analysis.result())
