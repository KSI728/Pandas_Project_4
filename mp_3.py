import pandas as pd                # 데이터 관련 모듈
import numpy as np                 # 배열 모듈
import matplotlib.pyplot as plt    # 시각화 모듈 
import koreanize_matplotlib        # 한글화 모듈

# [1] 파일 불러오기
grdp_df = pd.read_excel('GRDP1.xlsx')
in_df = pd.read_excel('inpeo.xlsx')

grdp_df.set_index(grdp_df['시점'],inplace=True)
in_df.set_index(grdp_df['시점'],inplace=True)

grdp_df.drop(grdp_df.columns[0], axis=1, inplace=True)
in_df.drop(in_df.columns[0], axis=1, inplace=True)

# 부산광역시 및 각 구 목록
busan_list = ['서구', '남구', '금정구', '연제구', '수영구', '사상구']
busan_list_top = ['해운대구','부산진구','사하구','동래구','북구']
busan_list_low = ['중구','강서구','동구','기장군','영도구']

# 시각화 - 산점도 그래프 1
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 12))
axes = axes.flatten()

for i, region in enumerate(busan_list):
    GRDP_data = np.array(grdp_df[region])
    in_data = np.array(in_df[region])
    
    # 산점도
    axes[i].scatter(GRDP_data, in_data)
    axes[i].set_title(region)
    axes[i].set_xlabel('GRDP')
    axes[i].set_ylabel('IN')
    
    # 선형 회귀선 추가
    poly_fit = np.polyfit(GRDP_data, in_data, 1)
    poly_1d = np.poly1d(poly_fit)
    
    xs = np.linspace(GRDP_data.min(), GRDP_data.max())
    ys = poly_1d(xs)
    
    axes[i].plot(xs, ys, color='gray')
    

# 마지막 빈 플롯 제거
if len(busan_list) < len(axes):
    for j in range(len(busan_list), len(axes)):
        fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# 시각화 - 산점도 그래프 2
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 12))
axes = axes.flatten()

for i, region in enumerate(busan_list_top):
    GRDP_data = np.array(grdp_df[region])
    in_data = np.array(in_df[region])
    
    # 산점도
    axes[i].scatter(GRDP_data, in_data)
    axes[i].set_title(region)
    axes[i].set_xlabel('GRDP')
    axes[i].set_ylabel('IN')
    
    # 선형 회귀선 추가
    poly_fit = np.polyfit(GRDP_data, in_data, 1)
    poly_1d = np.poly1d(poly_fit)
    
    xs = np.linspace(GRDP_data.min(), GRDP_data.max())
    ys = poly_1d(xs)
    
    axes[i].plot(xs, ys, color='gray')
    

# 마지막 빈 플롯 제거
if len(busan_list_top) < len(axes):
    for j in range(len(busan_list), len(axes)):
        fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# 시각화 - 산점도 그래프 3
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 12))
axes = axes.flatten()

for i, region in enumerate(busan_list_low):
    GRDP_data = np.array(grdp_df[region])
    in_data = np.array(in_df[region])
    
    # 산점도
    axes[i].scatter(GRDP_data, in_data)
    axes[i].set_title(region)
    axes[i].set_xlabel('GRDP')
    axes[i].set_ylabel('IN')
    
    # 선형 회귀선 추가
    poly_fit = np.polyfit(GRDP_data, in_data, 1)
    poly_1d = np.poly1d(poly_fit)
    
    xs = np.linspace(GRDP_data.min(), GRDP_data.max())
    ys = poly_1d(xs)
    
    axes[i].plot(xs, ys, color='gray')
    

# 마지막 빈 플롯 제거
if len(busan_list_low) < len(axes):
    for j in range(len(busan_list), len(axes)):
        fig.delaxes(axes[j])

plt.tight_layout()
plt.show()