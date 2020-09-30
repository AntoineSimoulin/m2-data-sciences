import matplotlib.pyplot as plt
import numpy as np

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'


def plot_word_counter(word_counter, top_n=100, save_fig=False):
    frequencies = [f for (w, f) in word_counter.most_common(top_n)]
    words = [w for (w, f) in word_counter.most_common(top_n)]
    words_idx = [i for i, (w, f) in enumerate(word_counter.most_common(top_n))]

    
    fig, ax = plt.subplots(figsize=(20, 8))

    # plt.vlines(x=words_idx, ymin=0, ymax=frequencies, color='#9E3D61', alpha=0.2, linewidth=15)  # 007ACC
    # plt.plot(words_idx, frequencies, "s", markersize=15, color='#970137', alpha=0.6)  # 007ACC 
    ax.bar(words_idx, frequencies, alpha=0.8, color='#970137', linewidth=15)


    # set labels
    ax.set_ylabel('Fréquence d\'apparition du mot', fontsize=15, 
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
    plt.yscale('log')
    
    # Add labels at the top of the bar
    for idx, f, w in zip(words_idx, frequencies, words):

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
                     rotation=90, fontsize=15,  weight='bold', color='white') 
        
    if save_fig:
        now = datetime.now()
        time_stamp = now.strftime("%d_%m_%Y__%H_%M_%S")
        plt.savefig('./counter_{}.png'.format(time_stamp), dpi=300, bbox_inches='tight')
        
    plt.show();
    
    
def plot_zipf(counter, save_fig=False):
    frequencies = [f for (w, f) in counter.most_common(len(counter))]
    words = [w for (w, f) in counter.most_common(len(counter))]
    words_idx = [i for i, (w, f) in enumerate(counter.most_common(len(counter)))]

    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Add labels word examples
    log_range = [int(f) for f in np.logspace(0, 4, 10)] 
    log_range[-1] = -100
    for i in log_range:

        label = "{}".format(words[i]) 
        plt.annotate(label, (words_idx[i], frequencies[i]), 
                     textcoords="offset points", xytext=(20,20), 
                     ha='center', rotation=0, fontsize=15, fontweight='black') 

    ax.set_xlabel('Rang des mots', fontsize=15)
    ax.set_ylabel('Fréquence d\'apparition des mots', fontsize=15)

    plt.plot(words_idx, frequencies, "o", markersize=5, color='#970137', alpha=0.3)
    plt.yscale('log')
    plt.xscale('log')
    ax.grid(True)
    
    if save_fig:
        now = datetime.now()
        time_stamp = now.strftime("%d_%m_%Y__%H_%M_%S")
        plt.savefig('./zipf_{}.png'.format(time_stamp), dpi=300, bbox_inches='tight')
        
    plt.show();