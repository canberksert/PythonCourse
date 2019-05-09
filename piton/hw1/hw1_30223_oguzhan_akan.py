
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 19:10:12 2019

@authors: Oguzhan Akan - 30223
"""
import random

class Portfolio():
    def __init__(self, owner=None, initialCash=0):
        self.owner=owner
        self.cash=initialCash
        self.stocks={} # {'stock':[unit, buying_price]}
        self.mfs={}
        self.tranIterator=1
        self.tranHistory='Transaction History:'

    def __str__(self):
        __str__='Your Portfolio:\n# Cash:\n$ '+str(round(self.cash,2))+'\n# Stocks\n'
        for stock in list(self.stocks.keys()):
            __str__ += str(self.stocks[stock][0])+' '+stock+'\n'
        __str__+='# Mutual Funds\n'
        for mf in list(self.mfs.keys()):
            __str__ += str(round(self.mfs[mf],2))+' '+mf+'\n'
        return __str__

    def addCash(self, amount):
        self.cash+=amount
        self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') $'+str(amount)+' of cash added.'
        self.tranIterator+=1

    def buyStock(self, unit, s):
        try:
            if(self.cash<=unit*s.price or type(unit)==float):
                print('Error')
                #print('Error: Insufficient cash, expected $%s, have $%s'%(unit*s.price,self.cash))
            else:
                self.cash -= unit*s.price
                try: self.stocks[s.symbol]= [self.stocks[s.symbol][0]+unit,s.price]
                except: self.stocks[s.symbol]  = [unit, s.price]
                print('Success: Buy %s units of %s stock.' %(unit,s.symbol))
                self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') '+str(unit)+' units of stock '+s.symbol+' bought for a total of $'+str(s.price*unit)+' - $'+str(s.price)+' each.'
                self.tranIterator+=1
        except TypeError:
            print('Invalid unit/price')

    def buyMutualFund(self, unit, mf):
        try:
            if(self.cash<=unit*mf.price):
                print('Error')
                #print('Error: Insufficient cash, expected $%s, have $%s'%(unit*s.price,self.cash))
            else:
                self.cash -= unit*mf.price
                try: self.mfs[mf.symbol] += unit
                except: self.mfs[mf.symbol] = unit
                print('Success: Buy %s units of %s mutual fund.' %(unit,mf.symbol))
                self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') '+str(unit)+' units of mutual fund '+mf.symbol+' bought for a total of $'+str(mf.price*unit)+' - $'+str(mf.price)+' each.'
                self.tranIterator+=1
        except TypeError:
            print('Invalid unit/price')

    def sellMutualFund(self, symbol, unit):
        if(type(unit)==float or type(unit)==int):
            if(symbol in self.mfs):
                if(self.mfs[symbol]>=unit):
                    self.mfs[symbol]-=unit
                    selling_price=round(random.uniform(0.9,1.2),2)
                    self.cash+=selling_price*unit
                    self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') '+str(unit)+' units of mutual fund '+symbol+' sold for a total of $'+str(round(selling_price*unit,2))+' ($'+str(selling_price)+'/unit).'
                    self.tranIterator+=1
                else: print('Error: You do not have '+str(unit)+' units of '+str(symbol))
            else: print('Error: You do not have a Mutual Fund named :'+str(symbol))
        else: print('Error: Invalid amount. Please enter a number.')

    def sellStock(self,symbol,unit):
        if(type(unit)==int):
            if(symbol in self.stocks):
                if(self.stocks[symbol][0]>=unit):
                    self.stocks[symbol][0]-=unit
                    selling_price=round(random.uniform(0.5*self.stocks[symbol][1],1.5*self.stocks[symbol][1]),2)
                    self.cash+=selling_price*unit
                    self.tranHistory = self.tranHistory+'\n'+str(self.tranIterator)+') '+str(unit)+' units of stock '+symbol+' sold for a total of $'+str(selling_price*unit)+' ($'+str(selling_price)+'/unit).'
                    self.tranIterator+=1
                else: print('Error: You do not have '+str(unit)+' units of '+symbol)
            else: print('Error: You do not have stock: '+symbol)
        else: print('Error: Invalid number of units. Please enter a whole number.')

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

class Stock():
    def __init__(self, price=None, symbol=None):
        self.symbol = symbol
        self.price = price

class MutualFund():
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.price = 1


# In[2]:


portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(50,'HFH')
portfolio.buyStock(2,s)
mf1 = MutualFund(symbol="BRT")
mf2 = MutualFund(symbol="GHT")
portfolio.buyMutualFund(10.3,mf1)
portfolio.buyMutualFund(2,mf2)

print(portfolio)
portfolio.sellMutualFund('BRT',3)
portfolio.sellStock('HFH',1)
portfolio.withdrawCash(50)
portfolio.history()

