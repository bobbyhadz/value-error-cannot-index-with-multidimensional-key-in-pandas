# Pandas ValueError: Cannot index with multidimensional key

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
    'experience': [10, 15, 20]
})

df2 = pd.DataFrame({
    'a': [0, 2]
})

#   first_name  salary  experience
# 0      Alice   175.1          10
# 2       Carl   190.3          20
print(df.loc[df2['a']])