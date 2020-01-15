
# 选取dataframe 列 = xxx 的行
# 选取 列anno_tag1 都为 是 和 audit_hidden_detail 都为NaN 的行
# df[(df['anno_tag1'] == '是') & df['audit_hidden_detail'].isnull()]