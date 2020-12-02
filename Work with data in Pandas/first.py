import pandas as pd
import numpy as np

'''
Так как задания взаимосвязанны,
я решил объединить все в один файл

Задание #1
'''
authors = pd.DataFrame({
                        "author_id":  [1, 2, 3,],
                        "author_name": ['Тургенев', 'Чехов', 'Островский',]
                       })

book = pd.DataFrame({
                     "author_id":  [1, 1, 1, 2, 2, 3, 3,],
                     "book_title": ['Отцы и дети', 'Рудин',
                                    'Дворянское гнездо', 'Толстый и тонкий',
                                    'Дама с собачкой', 'Гроза',
                                    'Таланты и поклонники',
                                   ],
                     "price": [450, 300, 350, 500, 450, 370, 290,]
                    })
'''
Задание #2
'''
authors_price = pd.merge(authors, book, on='author_id', how='inner')
'''
Задание #3
'''
top5 = authors_price.sort_values(by="price", ascending=False)[0:5]
'''
Задание #4
'''
authors_stat = pd.DataFrame({"author_name" : [author for author in authors['author_name']],
                             "min_price" :[authors_price[(authors_price.author_name == name)].min().price for name in authors['author_name']],
                             "max_price" :[authors_price[(authors_price.author_name == name)].max().price for name in authors['author_name']],
                             "mean_price" :[authors_price[(authors_price.author_name == name)].mean().price for name in authors['author_name']]
                            })

'''
Задание #5*
'''
authors_price["cover"] = ['твердая', 'мягкая', 'мягкая', 'твердая',
                          'твердая', 'мягкая', 'мягкая'
                         ]

book_info = pd.pivot_table(authors_price, values="price", index=['author_name'],
                    columns=['cover'], aggfunc=np.sum, fill_value=0)

book_info.to_pickle("book_info.pkl")
book_info2 = pd.read_pickle("book_info.pkl")

if book_info.equals(book_info2):
    print('''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗ ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║ ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║ ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║ ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═╝

          ''')
