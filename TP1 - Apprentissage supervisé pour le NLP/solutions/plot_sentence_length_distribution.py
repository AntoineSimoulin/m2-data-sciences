# Représenter la longueur des phrases

n_bins = 200

x = X_train_df['reviews'].apply(lambda x: len(x.split()))
y = X_valid_df['reviews'].apply(lambda x: len(x.split()))

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True, figsize=(20, 8))

axs[0].set_ylabel('Distribution de la longueur des phrases', fontsize=15,
              fontweight='black', color='#333F4B')

axs[0].hist(x, bins=n_bins, alpha=0.8, color='#970137', linewidth=15);
axs[1].hist(y, bins=n_bins, alpha=0.8, color='#970137', linewidth=15);