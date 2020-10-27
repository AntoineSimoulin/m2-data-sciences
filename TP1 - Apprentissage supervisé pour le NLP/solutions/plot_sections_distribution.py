# Représenter la distributions des labels

unique, counts = np.unique(X_train_df['section'], return_counts=True)
fig, ax = plt.subplots(figsize=(20, 8))

# plt.vlines(x=words_idx, ymin=0, ymax=frequencies, color='#9E3D61', alpha=0.2, linewidth=15)  # 007ACC
# plt.plot(words_idx, frequencies, "s", markersize=15, color='#970137', alpha=0.6)  # 007ACC
ax.bar(unique, counts, alpha=0.8, color='#970137', linewidth=15)


# set labels
ax.set_ylabel('Réparition des Sélections', fontsize=15,
              fontweight='black', color='#333F4B')
ax.set_xlabel('')
ax.set_title('')

# set axis
plt.xticks([])

# plt.xticks(words_idx, words)
# ax.tick_params(axis='both', which='major', labelsize=12)
# plt.xticks(rotation=70, ha='center')

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# set the spines position
ax.spines['left'].set_position(('axes', 0.015))
# plt.yscale('log')

# Add labels at the top of the bar
for idx, f, w in zip(range(len(counts)), counts, unique):

    label = "{}".format(w)
    plt.annotate(label,                      # this is the text
                 (idx, f),                   # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,20),              # distance from text to points (x,y)
                 ha='center',                # horizontal alignment can be left, right or center
                 rotation=90,
                 fontsize=15,
                 weight='bold')

    label = "{:.0f}".format(f)
    plt.annotate(label, (idx, f), textcoords="offset points",
                 xytext=(1, -40 - len(label)), ha='center',
                 rotation=90, fontsize=15,  weight='bold', color='white'