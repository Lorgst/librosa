import matplotlib.pyplot as plt
values = librosa.midi_to_hz(np.arange(48, 72))
plt.figure()
ax1 = plt.subplot(2,1,1)
ax1.bar(np.arange(len(values)), values)
ax1.set_ylabel('Hz')
ax2 = plt.subplot(2,1,2)
ax2.bar(np.arange(len(values)), values)
ax2.yaxis.set_major_formatter(librosa.display.NoteFormatter())
ax2.set_ylabel('Note')
plt.show()
