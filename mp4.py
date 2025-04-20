import pandas as pd                # 데이터 관련 모듈
import numpy as np                 # 배열 모듈
import matplotlib.pyplot as plt    # 시각화 모듈 
import koreanize_matplotlib        # 한글화 모듈

# [1] 파일 불러오기
sun_df = pd.read_excel('sun.xlsx')

# [2] 데이터 전처리 
sun_df.set_index(sun_df[2024],inplace=True)
sun_df.drop(sun_df.columns[0], axis=1, inplace=True)

busan_sr = np.array(sun_df['부산'])
daegu_sr = np.array(sun_df['대구'])
incheon_sr = np.array(sun_df['인천'])
gwangju_sr = np.array(sun_df['광주'])
daejeon_sr = np.array(sun_df['대전'])
ulsan_sr = np.array(sun_df['울산'])

cities = ['부산', '대구', '인천', '광주', '대전', '울산']
city_data = [busan_sr, daegu_sr, incheon_sr, gwangju_sr, daejeon_sr, ulsan_sr]

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
axes = axes.flatten()

for i, (city, data) in enumerate(zip(cities, city_data)):
    indices = np.arange(len(data))
    
    # 음수, 양수 값 분리
    positive_values = np.where(data > 0, data, 0)
    negative_values = np.where(data < 0, data, 0)
    
    axes[i].bar(indices, positive_values, color='red')
    axes[i].bar(indices, negative_values, color='blue')
    
    axes[i].set_title(city)
    axes[i].set_xlabel('2024/월')
    axes[i].set_ylabel('순이동 인구 (단위 : 천명)')
    axes[i].axhline(0, color='black', linewidth=0.8)
    axes[i].set_xticks(indices)
    axes[i].set_xticklabels(sun_df.index)

plt.tight_layout()
plt.legend(loc='upper right')
plt.show()