import sys  
import os
os.getcwd()

import gym
from gym import spaces
import numpy as np

# sys.path.append("D://Users//Desktop//Reinforcement-Learning-for-Automating-Pentest//Normalize-datasets")
# import Preprocessing_data

#Import Lib
import pandas as pd
import numpy as np

print("----------------------------CVE Info------------------------------------")

dataset_info_pre = pd.read_csv('D://Users//Desktop//Reinforcement-Learning-for-Automating-Pentest//Data//CVE_Info.csv', delimiter = ',')
print("Rows:",dataset_info_pre.shape[0],"Columns:",dataset_info_pre.shape[1])

print("----------------------------------------------------------------")

print(dataset_info_pre)

print("----------------------------Web Vulnerability------------------------------------")

dataset_vul_pre = pd.read_csv('D://Users//Desktop//Reinforcement-Learning-for-Automating-Pentest//Data//Web_Vulnerability.csv', delimiter = ',')
print("Rows:",dataset_vul_pre.shape[0],"Columns:",dataset_vul_pre.shape[1])

print("----------------------------------------------------------------")

print(dataset_vul_pre)


class WebPentestEnv(gym.Env):
    def __init__(self, Preprocessing_data.dataset_info_pre, Preprocessing_data.dataset_vul_pre):
        super(WebPentestEnv, self).__init__()

            self.Preprocessing_data.dataset_vul_pre = Preprocessing_data.dataset_vul_pre.copy(deep=True)
            self.action_space = spaces.Discrete(2)
            self.observation_space = spaces.Box(low=0, high=2**63-1, shape=(55,), dtype=np.int64)
            self.state = self.Preprocessing_data.dataset_vul_pre.iloc[0,:-1]

        # Danh sách lỗ hổng
        self.vulnerabilities = vulnerabilities

        # Hành động: 0 - Khám phá lỗ hổng, 1 - Tận dụng lỗ hổng, 2 - Quản lý tài nguyên
        self.action_space = spaces.Discrete(3)

        # Trạng thái: Một ma trận chứa thông tin về các lỗ hổng và trạng thái của môi trường
        self.observation_space = spaces.MultiBinary(len(vulnerabilities) + 1)

        # Trạng thái hiện tại
        self.current_state = np.zeros(len(vulnerabilities) + 1, dtype=np.int8)

        # Phần thưởng và số lần thực hiện hành động
        self.reward = 0
        self.steps_taken = 0
        self.max_steps = 10

    def reset(self):
        # Khởi tạo trạng thái ban đầu
        self.current_state = np.zeros(len(self.vulnerabilities) + 1, dtype=np.int8)
        self.reward = 0
        self.steps_taken = 0
        return self.current_state

    def step(self, action):
        # Thực hiện hành động và cập nhật trạng thái
        if action == 0:  # Khám phá lỗ hổng
            self.current_state[:len(self.vulnerabilities)] = np.random.choice([0, 1], size=len(self.vulnerabilities))
        elif action == 1:  # Tận dụng lỗ hổng
            exploitable_vulns = np.where(self.current_state[:len(self.vulnerabilities)] == 1)[0]
            if len(exploitable_vulns) > 0:
                exploited_vuln = np.random.choice(exploitable_vulns)
                self.current_state[exploited_vuln] = 0
                self.reward += 10  # Phần thưởng lớn khi tận dụng thành công
        elif action == 2:  # Quản lý tài nguyên
            self.reward += 1  # Phần thưởng nhỏ cho việc quản lý tài nguyên

        # Tăng số bước đã thực hiện
        self.steps_taken += 1

        # Kiểm tra điều kiện kết thúc
        done = self.steps_taken >= self.max_steps

        # Trả về trạng thái mới, phần thưởng và trạng thái kết thúc hay không
        return self.current_state, self.reward, done, {}

    def render(self, mode='human'):
        # In thông tin môi trường
        print(f"Current State: {self.current_state[:len(self.vulnerabilities)]}")
        print(f"Reward: {self.reward}")
        print(f"Steps Taken: {self.steps_taken}//n")

# Danh sách lỗ hổng từ dữ liệu mẫu của bạn
vulnerabilities = [
    "CVE-2010-1452", "CVE-2010-2068", "CVE-2011-0419",
    "CVE-2011-3192", "CVE-2011-3348", "CVE-2011-3368",
    "CVE-2011-3607", "CVE-2011-3639", "CVE-2011-4317",
    "CVE-2011-4415", "CVE-2012-0031", "CVE-2012-0053",
    "CVE-2012-0883", "CVE-2012-2687", "CVE-2012-3499",
    "CVE-2012-4557", "CVE-2012-4558"
]

# Tạo môi trường
env = WebPentestEnv(vulnerabilities)

# Chạy môi trường
for _ in range(5):
    state = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        state, reward, done, _ = env.step(action)
        env.render()
