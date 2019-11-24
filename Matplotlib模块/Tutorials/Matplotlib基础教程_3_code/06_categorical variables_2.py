import matplotlib.pyplot as plt

cat = ['bored', 'happy', 'bored', 'bored', 'happy', 'bored']
dog = ['happy', 'happy', 'happy', 'happy', 'bored', 'bored']

acticity = ['combing', 'drinking', 'feeding', 'napping', 'playing', 'washing']

fig, ax = plt.subplots()
ax.plot(acticity, dog, label='dog')
ax.plot(acticity, cat, label='cat')

plt.show()