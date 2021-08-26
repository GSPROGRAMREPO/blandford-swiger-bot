def forty_five_day_stop_loss(current_stock, purchase_stock):
    if ((current_stock.avg_price - purchase_stock.avg_price) / purchase_stock.avg_price) < -.05 and \
            current_stock.id - purchase_stock.id > 45:
        return True
    else: return False

def one_twenty_day_stagnation_stop_loss(current_stock, purchase_stock):
    if ((current_stock.avg_price - purchase_stock.avg_price) / purchase_stock.avg_price) < .05 and \
            current_stock.id - purchase_stock.id > 120:
        return True
    else:
        return False

def  short_term_rsi_stop_loss(current_stock, purchase_stock):
    if current_stock.rsi > 70 and current_stock.id - purchase_stock.id > 5:
        return True
    else:
        return False

def trailing_stop_loss(purchase_stock):
    if purchase_stock.stop_loss_peak_breached == True:
        return True
    else:
        return False