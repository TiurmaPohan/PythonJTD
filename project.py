import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('Int Monthly Visitor (data) fixed.xlsx')
print(df)
df_des = df.describe()

del df[' Brunei Darussalam ']
del df[' Malaysia ']
del df[' Philippines ']
del df[' Thailand ']
del df[' Viet Nam ']
del df[' Myanmar ']
del df[' Japan ']
del df[' Hong Kong ']
del df[' China ']
del df[' Taiwan ']
del df[' Korea, Republic Of ']
del df[' India ']
del df[' Pakistan ']
del df[' Sri Lanka ']
del df[' Saudi Arabia ']
del df[' Kuwait ']
del df[' UAE ']
del df[' United Kingdom ']
del df[' USA ']
del df[' Canada ']
del df[' Australia ']
del df[' New Zealand ']
del df[' Africa ']
# df = df.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31,
# 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
# 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,
# 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
# 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
# 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170,
# 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195,
# 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
# 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
# 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269,270,
# 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295,
# 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320,
# 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345,
# 346, 347, 348, 349, 350, 351, 352, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361])

# df1 = df.head(12).sum
# df2 = df.loc[374:385].sum()
# df3 = df.loc[386:397].sum()
# df4 = df.loc[398:409].sum()
# df5 = df.loc[410:421].sum()
# df6 = df.loc[422:433].sum()
# df7 = df.loc[434:445].sum()
# df8 = df.loc[446:457].sum()
# df9 = df.loc[458:469].sum()
# df10 = df.tail(11).sum()

# new_df = {' Years ': ['2008', '2009', '2010','2011', '2012', '2013', '2014', '2015', '2016','2017'],
# ' United Kingdom ' : [492933 , 469756, 461769, 442611, 446497, 461459, 451931, 473810, 489224,  476919],
# ' Germany ': [175280, 183681, 209264, 219952, 252433, 229418, 263513, 286732, 328765, 313479],
# ' France ': [111198, 119728, 130461, 140299, 158923, 160013, 156882, 157483, 170913, 163558],
# ' Italy ' : [43035, 46770, 130461, 140299, 158923, 160013, 156882, 157483, 170913, 163558],
# ' Netherlands ': [43035, 46770, 51086, 53520, 66557, 66650, 67052, 69350, 74629, 75226],
# ' Greece ': [9045, 9250, 8006, 7130, 8137, 7200, 8295, 8867, 8744, 10426],
# ' Belgium & Luxembourg ': [21100, 21365, 24399,24979, 26824, 27352, 28695, 27579, 29358, 28582],
# ' Switzerland ': [64788, 63829, 74376, 79023,83857, 94380, 103440, 100849, 101455, 96251],
# ' Austria ': [16649, 17505, 20093, 19889, 21431, 24731, 26509, 25108, 26822, 26448],
# ' Scandinavia ': [100295, 92849, 96484, 97019, 111530, 113103, 109456, 105601, 104261, 100158],
# ' CIS & Eastern Europe ': [114284, 110429, 119746, 127926, 153765, 177536, 191209, 167018, 183524, 182871]
# }
# df = pd.DataFrame(new_df)
import pandas as pd

df = {"Country": ["United Kingdom", "Germany", "France", "Italy", "Netherlands",
                  "Greece", "Belgium & Luxemborg", "Switzerland", "Austria", "Scandinavia", "CIS & Eastern Europe"],
      "Visitors": [4666909, 2462517, 1469458, 1328337, 547225, 85100, 260233, 769152, 260233, 1030756, 1528308]}

bs = pd.DataFrame(df)
print(bs)
df_des = bs.describe()

# df.index = df[' Years ']
# del df[' Years ']


# new_df = {' Country ': [' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ',
#   ' Belgium & Luxembourg ',' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']}


# ax =df_des.plot(kind='bar', title="Avg Int Monthly Visitor(ALL)", figsize=(15,15), legend=True, fontsize=15)
# ps =df[' Country '].sort_values()
# index = np.arange(len(ps.index))
# plt.xlabel(' Country ', fontsize=5)
# plt.ylabel('Visitor', fontsize=10)
# plt.xticks(index, ps.index, fontsize=10, rotation=90)
# plt.title('Avg Visitor')
# plt.bar(ps.index, ps.values)
# plt.show();
# my_fig = ax.get_figure()
# my_fig.savefig('Avg Int Monthly Visitor(ALL).png')


bs.index = bs["Visitors"]
del bs["Visitors"]

plt.barh(bs["Country"], bs.index, label="Countrys")
plt.legend(loc="best")
plt.grid()
plt.xlabel("Visitor")
plt.ylabel("Countrys")
plt.title("No. Visitor")
plt.figure(figsize=(30, 30))
index = np.arange(len(bs.index))
plt.show()
