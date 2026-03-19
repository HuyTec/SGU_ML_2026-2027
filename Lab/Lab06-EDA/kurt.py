import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, laplace, uniform, gaussian_kde, kurtosis

# tạo dữ liệu cho 3 loại kurtosis
data_lepto = laplace.rvs(size=1000)      # nhọn (kurt > 0)
data_meso = norm.rvs(size=1000)          # chuẩn (kurt ≈ 0)
data_platy = uniform.rvs(size=1000)      # bẹt (kurt < 0)

datasets = [data_lepto, data_meso, data_platy]
titles = ["Leptokurtic (Kurt > 0)", 
          "Mesokurtic (Kurt = 0)", 
          "Platykurtic (Kurt < 0)"]

plt.figure(figsize=(12,4))

for i, data in enumerate(datasets):

    plt.subplot(1,3,i+1)

    # histogram
    plt.hist(data, bins=30, density=True, alpha=0.6)

    # đường cong liên tục KDE
    kde = gaussian_kde(data)
    x = np.linspace(min(data), max(data), 200)
    plt.plot(x, kde(x), linewidth=2)

    # tính kurtosis
    k = kurtosis(data)  # excess kurtosis

    plt.title(f"{titles[i]}\nKurt={k:.2f}")

plt.tight_layout()
plt.show()