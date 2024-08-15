from datetime import datetime
from read_excel import ReadExcel
# 提供的时间数据
# time_data = [
#     "20:25:59", "20:13:30", "17:11:59", "22:00:50", "21:49:59", "21:49:59",
#     "21:20:52", "20:39:50", "20:31:35", "20:25:51", "20:17:24", "19:06:01",
#     "18:23:05", "17:52:11", "17:48:43", "17:10:10", "22:06:22", "20:25:59",
#     # ... 更多时间数据
# ]
time_data = ReadExcel('D:\\01.餐饮\\交易时间.xlsx')
# 筛选17点到23点的数据
filtered_time_data = [time for time in time_data if 17 <= int(time.split(":")[0]) <= 23]

# 将时间字符串转换为datetime对象
converted_time_data = [datetime.strptime(time, "%H:%M:%S") for time in filtered_time_data]


# 以30分钟为单位对时间进行分组
def group_time(data, interval=30):
    grouped_data = {}
    for time in data:
        # 计算时间所在的组
        group = time.hour * 60 + time.minute // interval * interval
        if group in grouped_data:
            grouped_data[group] += 1
        else:
            grouped_data[group] = 1
    return grouped_data


# 统计每个时间段的交易次数
grouped_time_data = group_time(converted_time_data)

print(grouped_time_data)
