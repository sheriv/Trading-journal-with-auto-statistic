"""
The module contains math functions that performs 
list analysis.
"""

import datetime

def trade_result(dict):
    """
    This function compares Stop loss order with trade entry price 
    and returns trade result.
    """
    
    if float(dict['Stop-loss']) > float(dict['Entry point']):
        
        #direction = 'short'
        if (float(dict['Entry point']) - float(dict['Exit'])) > 0:
            trade = 'positive'
        else:
            trade = 'negative'
        
    
    else:
        
        #direction = 'long'
        if (float(dict['Exit']) - float(dict['Entry point'])) > 0:
            trade = 'positive'
        else:
            trade = 'negative'
        
    return trade

def result(contract, dict, positions):
    """
    Returns trade result - loss or profit value.
    """
    
               
    if float(dict['Stop-loss']) > float(dict['Entry point']):
        value = (float(dict['Entry point']) - float(dict['Exit']))*positions
            
    else:
        value = (float(dict['Exit']) - float(dict['Entry point']))*positions
    
        
    return str(value)

def datetime_format():
    """
    Converts date and time from today() format to
    dd.mm.yy and hh mm format
    """
    #splitting today() data into date and time parts
    today = datetime.datetime.today() 
    today_str = str(today)
    today_list = today_str.split(' ')
    #splitting data and time into elements like day hour
    date,time = today_list
    date_list = date.split('-')
    time_list = time.split(':')
    #assigning elements
    year,month,day = date_list
    hour = time_list[0]
    min = time_list[1]
    #creating lists for join() method
    time_join_list = hour, min
    date_join_list = day,month,year
    #creating output format
    time_formated = ' '.join(time_join_list)
    date_formated = '.'.join(date_join_list)
    return date_formated, time_formated
    
def statistic(list) :

    """
    This function counts the strategy statistics.
    """
    
    n_of_wins = 0
    win_trades = 0
    n_of_loses = 0
    lose_trades = 0
    balance = 0
    drawdown_flag = True
    current_drawdown = 0
    max_drawdown = 0
    prev_drawdown = 0
    lose_trade = 0
    
    #it is important for drawdown calcualtion that dicts come by time order
    list.sort(key = lambda t: datetime.datetime.strptime(t['Time'],'%H %M'))
    list.sort(key = lambda t: datetime.datetime.strptime(t['Date'],'%d.%m.%Y'))
    
    
    for dict in list:
        #only closed trades are used
        if dict['Closed']:
        
            
             
            if trade_result(dict) == 'positive':
                
                #calculating summury profit and wins number
                positions = int(dict['Positions'])
                win_trades += abs((float(dict['Exit']) - float(dict['Entry point']))*positions)
                n_of_wins += 1
                
                #resetting drawdown flag on a win trade
                drawdown_flag = False
                
                #finding max drawdown
                if current_drawdown == 0:
                    prev_drawdown = lose_trade
                
                else:
                    prev_drawdown = current_drawdown
                
                if prev_drawdown > max_drawdown:
                    
                    max_drawdown = prev_drawdown
                    
            elif trade_result(dict) == 'negative':
                
                #calculating summury loss and negative trades number
                positions = int(dict['Positions'])                
                lose_trade = abs((float(dict['Exit']) - float(dict['Entry point']))*positions)
                
                lose_trades += lose_trade
                n_of_loses += 1
                
                #calculating strategy drawdown
                #current drawdwon is reset if a positive trade occurs
                if drawdown_flag == True:
                    current_drawdown += lose_trade
                    
                else:
                                        
                    current_drawdown = lose_trade
                    drawdown_flag = True
                
            else:
                    
                print 'Error in statistics function'
            
            #overall gain or loss
            balance += float(result(dict['Contract'],dict,int(dict['Positions'])))
        
        else:
            continue
    
    trades_count = n_of_wins + n_of_loses
    
    try:
        
        avg_win =  round(win_trades/n_of_wins,2)
        
        win_procent = round(n_of_wins*100/trades_count,2)
                
        if lose_trades != 0 and n_of_loses != 0 and  trades_count !=  0:
            avg_lose =  round(lose_trades/n_of_loses,2)
            lose_procent = round(n_of_loses*100/trades_count,2)
            win_lose_ratio =  round(win_procent/lose_procent,2)
            profit_ratio = round(avg_win/avg_lose,2)
            expectancy = round(((avg_win*win_procent*0.01)-(avg_lose*lose_procent*0.01)),2)
            expectancy_procent = round(expectancy/avg_lose,2)
            drawdown_procent = round((current_drawdown/max_drawdown), 2)
            
        else:
            avg_lose = 0
            lose_procent = 0
            win_lose_ratio = '-'
            profit_ratio = '-'
            expectancy = round(((avg_win*win_procent*0.01)))
            expectancy_procent = '-'
            drawdown_procent = '-'
        list = [ str(expectancy), str(expectancy_procent), str(win_lose_ratio), 
        str(profit_ratio), str(avg_win), str(avg_lose),
        str(win_procent), str(lose_procent), str(balance),
        str(max_drawdown), str(current_drawdown), str(drawdown_procent) ]
        
        return list
        
        
    except ZeroDivisionError:
        
        pass