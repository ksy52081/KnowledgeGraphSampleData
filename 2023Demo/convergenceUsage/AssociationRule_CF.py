import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('/home/sangyoon/TMAX/DataFabric/KnowledgeGraphSampleData/2023Demo/convergenceUsage/Mock_Shopping_Cart_Data.csv')

# 사용자-아이템 매트릭스 생성 (user-item interaction matrix)
user_item_matrix = df.pivot_table(index='userId', columns='itemId', aggfunc='size', fill_value=0)

# 아이템 간 코사인 유사도 계산
item_similarity = cosine_similarity(user_item_matrix.T)

# 아이템 간 유사도를 데이터프레임으로 변환
item_similarity_df = pd.DataFrame(item_similarity, 
                                  index=user_item_matrix.columns, 
                                  columns=user_item_matrix.columns)

# 결과를 ItemId1, ItemId2, Score 형식으로 변환
item_similarity_melt = item_similarity_df.reset_index().melt(id_vars='itemId', var_name='ItemId2', value_name='Score')

# 자기 자신과의 유사도(1인 값) 제거
item_similarity_melt = item_similarity_melt[item_similarity_melt['itemId'] != item_similarity_melt['ItemId2']]
sorted_df = item_similarity_melt.sort_values(by=['itemId', 'ItemId2'])
print(sorted_df)

# Save the association rules to a CSV file
output_file_path = 'association_rules_CF.csv'
sorted_df.to_csv(output_file_path, index=False)