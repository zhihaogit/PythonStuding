# datetime是 python处理日期和时间的标准库

# 获取当前日期和时间
# datetime是模块，还包含一个 datetime类
from datetime import datetime
now = datetime.now()
print (now, type(now))

# 获取指定日期和时间
# 指定日期时间创建 datetime
dt = datetime(2019, 12, 19, 15, 50)
print (dt)

# datetime转换为 timestamp
# 是个浮点数
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
dt = datetime(2019, 12, 20, 1, 20)
print (dt.timestamp())

# 转成东 8区时间
t = 1576776000.0
# 本地时间
localTime = datetime.fromtimestamp(t)
# UTC时间
utcTime = datetime.utcfromtimestamp(t)
print (localTime, utcTime)


# str转换为 datetime
str1 = '2019-12-19 17:20:00'
cday = datetime.strptime(str1, '%Y-%m-%d %H:%M:%S')
print (cday)

# datetime转换为 str
now = datetime.now()
print (now.strftime('%a, %b %d %H:%M'))


# datetime加减
# 需要 timedelta类
from datetime import datetime, timedelta
now = datetime.now()
now = now + timedelta(hours = 10)
print (now)
now = now - timedelta(days = 1)
print (now)
now = now + timedelta(days = 2, hours = 12)
print (now)


# 本地时间转换为 UTC时间
# datetime类型有一个时区属性 tzinfo，默认是 None
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours = 8))
now = datetime.now()
datetime(2019, 12, 20, 1, 20, 10, 871012)
dt = now.replace(tzinfo = tz_utc_8)
print (dt)


# 时区转换
# 拿到 utc时间，强制设置时间为 UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print (utc_dt)
# astimezone() 将转换时间为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print (bj_dt)
# astimezone() 将转换时间为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print (tokyo_dt)
# astimezone() 将 bj_dt转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours = 9)))
print (tokyo_dt2)

# 时间转换，要获取到正确的时区，然后强制设置时区，作为基准时间
# 利用带时区的 datetime，通过 astimezone()方法，可以转换为任意时区
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则视为本地时间
# 储存时间的时候，最好储存时间戳


















