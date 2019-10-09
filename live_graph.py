style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'blue'
fig.facecolor:"0.75"
fig.figsize   : [8.0, 6.0]
fig.titlesize : 'large'

def animate(i):
    pullData = open("twitter.txt", "r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-50:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.set_title('Live Tweeter Review')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Sensitivity')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.grid(color='blue', linestyle='-', linewidth=0.25, alpha=0.5)
    
    ax1.plot(xar, yar)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
