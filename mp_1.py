import pandas as pd                # 데이터 관련 모듈
import numpy as np                 # 배열 모듈
import matplotlib.pyplot as plt    # 시각화 모듈 
import koreanize_matplotlib        # 한글화 모듈

# [1] 파일 불러오기
in_df = pd.read_excel('in.xlsx')
out_df = pd.read_excel('out.xlsx')

# [2] 맨 앞 year열을 인덱스로 변경 

# 1
in_df.set_index(in_df['Year'],inplace=True)
in_df.drop(columns=['Year'],inplace=True)

# 2
out_df.set_index(out_df['Year'],inplace=True)
out_df.drop(columns=['Year'],inplace=True)

# 결측치 확인
in_df.isna().sum()
out_df.isna().sum()

# [3] 데이터 시각화 - 광역시별 전입 인구 수 비교 
busan_sr = np.array(in_df['부산광역시'])
daegu_sr = np.array(in_df['대구광역시'])
incheon_sr = np.array(in_df['인천광역시'])
gwangju_sr = np.array(in_df['광주광역시'])
daejeon_sr = np.array(in_df['대전광역시'])
ulsan_sr = np.array(in_df['울산광역시'])

in_list = [busan_sr,daegu_sr,incheon_sr,gwangju_sr,daejeon_sr,ulsan_sr]
label_list=['부산','대구','인천','광주','대전','울산','세종']

fig=plt.figure(figsize=(12,8))   

# 연도별 추이
for i,k in zip(in_list, label_list):
    xdata = in_df.index
    plt.plot(xdata[i != 0], i[i != 0], 'o--', label=k) 

# 그래프 설정
plt.xlabel("연도", fontsize=14)
plt.ylabel("인구 수(명)", fontsize=14)
plt.title("광역시별 전입 인구 추이", fontsize=16)

plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.legend(title="도시", fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))

plt.xticks(list(in_df.index),rotation=45)
plt.tight_layout()
plt.show()

# 총 전입 인구
for i,k in zip(in_list, label_list):
    xdata = k
    ydata = i.sum()
    plt.bar(k,ydata)
    
# 그래프 설정
plt.xlabel("연도", fontsize=14)
plt.ylabel("인구 수(명)", fontsize=14)
plt.title("광역시별 전입 인구", fontsize=16)

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 부산 구별 전입인구 시각화 
busangu_df = in_df.iloc[:, 1:17]

# 각 열의 합계를 계산
sum_data = busangu_df.sum()

# 상위 5개와 하위 5개의 구를 찾기
top_5 = sum_data.nlargest(5)
bottom_5 = sum_data.nsmallest(5)

# 시각화
# 1
colors = ['#1f77b4', '#4f92d2', '#7ab1f0', '#a7ccff', '#d3eaff']
plt.figure(figsize=(10, 6))
plt.bar(top_5.index, top_5.values, color=colors)
plt.title('부산 전입자 수 상위 5개 구')
plt.xlabel('구')
plt.ylabel('전입자 수 합계')
plt.show()

# 2 
colors = ['#d62728', '#e74c3c', '#ff6347', '#ff9999', '#ffcccc']
plt.figure(figsize=(10, 6))
plt.bar(bottom_5.index, bottom_5.values, color=colors)
plt.title('부산 전입자 수 하위 5개 구')
plt.xlabel('구')
plt.ylabel('전입자 수 합계')
plt.show()

# [4] 데이터 시각화 - 광역시별 전출 인구 수 비교 
busan_sr = np.array(out_df['부산광역시'])
daegu_sr = np.array(out_df['대구광역시'])
incheon_sr = np.array(out_df['인천광역시'])
gwangju_sr = np.array(out_df['광주광역시'])
daejeon_sr = np.array(out_df['대전광역시'])
ulsan_sr = np.array(out_df['울산광역시'])

out_list = [busan_sr,daegu_sr,incheon_sr,gwangju_sr,daejeon_sr,ulsan_sr]

fig=plt.figure(figsize=(12,8))   

# 연도별 추이
for i,k in zip(out_list, label_list):
    xdata = out_df.index
    plt.plot(xdata[i != 0], i[i != 0], 'o--', label=k) 

# 그래프 설정
plt.xlabel("연도", fontsize=14)
plt.ylabel("인구 수(명)", fontsize=14)
plt.title("광역시별 전출 인구 추이", fontsize=16)

plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.legend(title="도시", fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))

plt.xticks(list(out_df.index),rotation=45)
plt.tight_layout()
plt.show()
