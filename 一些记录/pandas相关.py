
# 选取dataframe 列 = xxx 的行
# 选取 列anno_tag1 都为 是 和 audit_hidden_detail 都为NaN 的行
# df[(df['anno_tag1'] == '是') & df['audit_hidden_detail'].isnull()]

# query用法
# data.query('anno_tag1=="是" and audit_hidden_detail=="通过" and deliver_hidden_detail!="已交付"')

# 选取指定的两列
# new_data = data.query('anno_tag1=="是" and audit_hidden_detail=="通过" and deliver_hidden_detail!="已交付"')[['article_url','Video_review_writing']]


# ==自己是空值？
# df1 = df.query('A<10 & C==C')


# 读取
# filename = 'xxx.xlsx'
# data = pd.read_excel(filename)

# 写入
# new_data.to_csv('new1.csv', index=False, encoding="utf_8_sig")
# new_data.to_excel('new1.xlsx', index=False, encoding="utf_8_sig")