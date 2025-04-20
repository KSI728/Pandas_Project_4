import pandas as pd                # 데이터 관련 모듈
import numpy as np                 # 배열 모듈
import matplotlib.pyplot as plt    # 시각화 모듈 
import koreanize_matplotlib        # 한글화 모듈


# [1] 파일 불러오기
busanm_df = pd.read_excel('busan_man.xlsx')
busanw_df = pd.read_excel('busan_woman.xlsx')

# [2] 맨 앞 Year열을 인덱스로 변경 

# 1
busanm_df.set_index(busanm_df['Year'],inplace=True)
busanm_df.drop(columns=['Year'],inplace=True)

# 2
busanw_df.set_index(busanw_df['Year'],inplace=True)
busanw_df.drop(columns=['Year'],inplace=True)

# [3] 인구 피라미드 그래프 함수 생성 
def pyramid(year):
    
    age_labels = busanm_df.columns[:21]
    latest_year = year  # 연도 입력받기

    male_df = busanm_df.loc[latest_year, age_labels] * -1  # 남성 인구 음수화
    female_df = busanw_df.loc[latest_year, age_labels]  # 여성 인구
    
    # [4] 그래프 그리기
    plt.figure(figsize=(10, 6))
    plt.barh(age_labels, male_df, color='skyblue', label='남성')   # 왼쪽(음수) 남성 인구
    plt.barh(age_labels, female_df, color='orange', label='여성')  # 오른쪽(양수) 여성 인구

    # [5] 그래프 설정
    plt.xlabel("인구 수")
    plt.ylabel("연령대")
    plt.title(f"{latest_year}년 부산 인구 피라미드")
    plt.legend()
    plt.xticks(ticks=[-175000, -150000, -125000, -100000, -75000,-50000, -25000, 0, 25000, 50000, 75000, 100000, 125000, 150000, 175000], 
               labels=[f"175,000", "150,000", "125,000", "100,000", "75,000","50,000", "25,000", "0", "25,000", "50,000", "75,000", "100,000", "125,000", "150,000", "175,000"])  
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    plt.show()

pyramid(2024)
