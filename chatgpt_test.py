import openai
from openai import OpenAI
import os
import requests
from datetime import datetime, timedelta

from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 读取环境变量
api_key = os.getenv("OPENAI_API_KEY")
  

# 设置 API 密钥
openai.api_key = api_key


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "你是一名乐于助人的AI助手。"},
        {"role": "user", "content": "我先要开始一个故事,你能够接收我的故事模板吗,[葬送的芙莉蓮(角色名) =精靈,魔法使,雙馬尾,藍色雙眼,精靈耳朵,白皮膚, 個性冷靜,熱衷週遊各方蒐集魔法, 喜歡賴床 , 喜歡的花卉是冬天綻放的冰柱櫻, 對戀愛方面遲鈍,對於慶祝生日的觀念很淡薄但在辛美爾過世後意識到人類的壽命短暫, 對人的情感遲鈍仍會盡力在同行夥伴的生日期間精心準備慶祝禮物, 受辛美爾的影響養成看護病患期間會握住對方的手的習慣, 透過恩師伏拉梅傳授常年維持限制魔力的技巧,一旦解除魔力限制便會發揮強大的力量]"}
    ],
    model="gpt-4o",
    max_tokens=100,
    temperature=0.7,
)


# 输出结果
print(chat_completion.choices[0].message.content)


# headers = {
#     "Authorization": f"Bearer {api_key}"
# }

# # 查询最近 30 天的用量
# end_date = datetime.now().strftime("%Y-%m-%d")
# start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

# url = "https://api.openai.com/v1/dashboard/billing/usage"
# params = {
#     "start_date": start_date,
#     "end_date": end_date
# }

# response = requests.get(url, headers=headers, params=params)

# if response.status_code == 200:
#     data = response.json()
#     total_usage = data.get("total_usage", 0) / 100  # 转换为美元
#     print(f"最近 30 天的 API 使用费用：${total_usage:.2f}")
# else:
#     print("查询失败：", response.text)

