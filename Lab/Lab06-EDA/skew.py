import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, gaussian_kde

# tạo dữ liệu
data_left = skewnorm.rvs(-10, size=1000)
data_normal = np.random.normal(0,1,1000)
data_right = skewnorm.rvs(10, size=1000)

datasets = [data_left, data_normal, data_right]
titles = ["skew < 0", "skew = 0", "skew > 0"]

plt.figure(figsize=(12,4))

for i, data in enumerate(datasets):

    plt.subplot(1,3,i+1)

    # histogram
    plt.hist(data, bins=30, density=True, alpha=0.6)

    # đường density liên tục
    kde = gaussian_kde(data)
    x = np.linspace(min(data), max(data), 200)
    plt.plot(x, kde(x), linewidth=2)

    plt.title(titles[i])

plt.tight_layout()
plt.show()