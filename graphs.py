import matplotlib.pyplot as plt

x = [1, 2, 4, 8, 16, 32]
y1 = [0.80722948,
      0.896505439,
      0.92859484,
      0.935665122,
      0.983721184,
      0.983846046
      ]
y2 = [0.829267531,
      0.905011628,
      0.961152471,
      0.982222847,
      0.983440246,
      0.983846046
      ]
y3 = [0.879461847,
      0.946044232,
      0.975839303,
      0.982862762,
      0.983830438,
      0.983846046
      ]
y4 = [0.884518737,
      0.952615068,
      0.977634187,
      0.982519393,
      0.983846046,
      0.983846046
      ]

plt.ylim(0.7, 1)
plt.plot(x, y1, color='green', linestyle='dashdot', marker='o', markerfacecolor='green', markersize=4)
plt.plot(x, y2, color='blue', linestyle='dashdot', marker='o', markerfacecolor='blue', markersize=4)
plt.plot(x, y3, color='red', linestyle='dashdot', marker='o', markerfacecolor='red', markersize=4)
plt.plot(x, y4, color='yellow', linestyle='dashdot', marker='o', markerfacecolor='yellow', markersize=4)

plt.legend(
    ['1 - way', '2 - way', '4 - way', '8 - way'],
    loc='lower right')

plt.xlabel('Cache size(Kb)')
plt.ylabel('Hit Ratio')

plt.title('Fixed line size = 8b')
plt.show()
