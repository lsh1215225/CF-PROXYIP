import pandas as pd

# 读取CSV文件
df = pd.read_csv('latest.csv')

# 创建一个新的列，其中包含"峰值速度"列的值，但是已经去掉了单位（kB/s）
df['峰值速度数值'] = df['峰值速度'].str.replace(' kB/s', '').astype(float)

# 按照"峰值速度数值"列的值进行排序
df_sorted = df.sort_values(by='峰值速度数值', ascending=False)

# 添加双重筛选条件：国家为US且IP类型为隧道
df_gj = df_sorted[(df_sorted['国家'] == 'US') & (df_sorted['IP类型'] == '隧道')]

# 使用正则表达式匹配IPv6地址
ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

# 筛选出回源IP是IPv6地址的行
df_gj_ipv6 = df_gj[df_gj['回源IP'].str.contains(ipv6_pattern, na=False)]

# 将排序后的DataFrame保存回CSV文件
df_gj_ipv6.to_csv('latest_sorted.csv', index=False)