
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:43:52 2019

@authors: Oguzhan Akan - 30223
"""
import random

class FinancialInstrument():
    def __init__(self,price=1,symbol=None):
        if((type(price) ==int or type(price) == float) and type(symbol)==str):
            self.symbol=symbol
            self.price=price
        else:print('You entered invalid symbol or price. Try again.')

class Stock(FinancialInstrument):
    ins_type='Stock'

class MutualFund(FinancialInstrument):
    ins_type='Mutual Fund'

class Bond(FinancialInstrument):
    ins_type='Bond'

class Portfolio():
    def __init__(self, owner=None, initialCash=0):
        self.owner=owner
        self.cash=initialCash
        self.instruments={}
        self.tranIterator=1
        self.tranHistory='Transaction History:'

    def __str__(self):
        __str__='Your Portfolio:\n# Cash:\n$ '+str(round(self.cash,2))+'\n# Stocks\n'
        for stock in list(self.instruments.keys()):
            if(self.instruments[stock][0]=='Stock'):
                __str__ += str(self.instruments[stock][1])+' '+stock+'\n'
        __str__+='# Mutual Funds\n'
        for mf in list(self.instruments.keys()):
            if(self.instruments[mf][0]=='Stock'):
                __str__ += str(round(self.instruments[mf][1],2))+' '+mf+'\n'
        return __str__

    def addCash(self, amount):
        self.cash+=amount
        self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') $'+str(amount)+' of cash added.'
        self.tranIterator+=1

    def buyInstrument(self, unit, s):
        try:
            if(self.cash<=unit*s.price or (s.ins_type=='Stock' and type(unit)==float)):
                print('Error')
            else:
                self.cash -= unit*s.price
                try: self.instruments[s.symbol][1] += unit
                except: self.instruments[s.symbol]  = [s.ins_type,unit,s.price]
                print('Success: Buy '+str(unit)+' units of '+s.ins_type+'.')
                self.tranHistory =self.tranHistory+'\n'+str(self.tranIterator)+') '+str(unit)+' units of '+s.ins_type+' '+s.symbol+' bought for a total of $'+str(s.price*unit)+' - $'+str(s.price)+' each.'
                self.tranIterator+=1
        except TypeError:
            print('Invalid unit/price')

    def sellInstrument(self, instrument, unit):
        if(type(unit)==float or type(unit)==int):
            if(instrument.symbol in self.instruments):
                if(self.instruments[instrument.symbol][1]>=unit):
                    if(instrument.ins_type=='Stock'):
                        selling_price=round(random.uniform(0.5*self.instruments[instrument.symbol][2],1.5*self.instruments[instrument.symbol][2]),2)
                    elif(instrument.ins_type=='Mutual Fund'):
                        selling_price=round(random.uniform(0.9,1.2),2)
                    elif(instrument.ins_type=='Bond'):
                        selling_price=instrument.price
                    self.instruments[instrument.symbol][2]-=unit
                    self.cash+=selling_price*unit
                    self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') '+str(unit)+' units of '+instrument.ins_type+' '+instrument.symbol+' sold for a total of $'+str(round(selling_price*unit,2))+' ($'+str(selling_price)+'/unit).'
                    self.tranIterator+=1
                    print('Success: Sell '+str(unit)+' units of '+instrument.ins_type+' for a total of '+str(selling_price*unit)+' ($'+str(selling_price)+'each).')
                else: print('Error: You do not have '+str(unit)+' units of '+str(instrument.symbol))
            else: print('Error: You do not have a Mutual Fund named :'+str(instrument.symbol))
        else: print('Error: Invalid amount. Please enter a number.')

    def withdrawCash(self, amount):
        if(self.cash>=amount):
            self.cash-=amount
            self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') $'+str(amount)+' amount of cash is withdrawn.'
            self.tranIterator+=1
        else: print('You do not have that much cash, honey.')

    def history(self):
        if(len(self.tranHistory)>len('Transaction History:')):
            print(self.tranHistory)
        else:
            print('There is no transaction.')


# In[2]:


# it is now easier to add the bond to our mix. we do not need to add anything to the class 'portfolio',
# as we defined the stocks, bonds, and mutual funds as a sub-class of 'FinancialInstrument'.
# Selling and buying functions run on the super-class, so just adding the following makes the code work:
# class Bond(FinancialInstrument):
#    ins_type='Bond'

# example:
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(50,'HFH')
mf = MutualFund(symbol="BRT")
b = Bond(price=30,symbol="BOND")
portfolio.buyInstrument(2,s)
portfolio.buyInstrument(5,mf)
portfolio.buyInstrument(3,b)
portfolio.sellInstrument(s,1)
portfolio.sellInstrument(mf,4)
portfolio.sellInstrument(b,2)
print(portfolio)
portfolio.history()

