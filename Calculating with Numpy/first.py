import numpy as np

'''
Так как задания взаимосвязанны,
я решил объединить все в один файл

Задание #1
'''
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7],
             ])
mean_a = np.array([np.mean(a[:,0]),
                   np.mean(a[:,1]),
                  ])
'''
Задание #2
'''
a_centered = a - mean_a
'''
Задание #3
'''
a_centered_sp = np.dot(a_centered[:,0],
                       a_centered[:,1]
                      )
result = a_centered_sp / (a.shape[0] - 1)
'''
Задание #4**
'''
easy_result = np.cov(a.transpose())

if result == easy_result[1, 0]:
    print('''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗ ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║ ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║ ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║ ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═╝

          ''')
