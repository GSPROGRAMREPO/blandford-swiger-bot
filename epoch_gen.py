# TODO impliment epoch system so dates and id values can align
# Would look like a dictionary with the key as epochdate and id as the value
# First would be to generate epcohdates and their corrosponding ID values
# Then when setting the ids call the .timestamp function
# reference the dictionary with that key values to get the id
# Setting it would look like this

# It has to be generated based on the import data othewise it doesn't solve problem
'''
        year = int(candle.date[0:4])
        month = int(candle.date[5:7])
        day = int(candle.date[8:])
        id = some_dict.get([int(datetime.datetime(year, month, day, 0, 0, ).timestamp())])


'''
