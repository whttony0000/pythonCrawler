import tushare

realtime_stockindex = tushare.get_latest_news()
realtime_stockindex_json = realtime_stockindex.to_json(orient='records')

print(realtime_stockindex_json)
print(realtime_stockindex)
