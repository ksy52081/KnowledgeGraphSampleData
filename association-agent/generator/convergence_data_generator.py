import pandas as pd

class ConvergenceDataGenerator:
  def __init__(self):
    None
  def generateDataFrame(self) -> pd.DataFrame:
    # Parameters
    user_ids = [str(i) for i in range(1, 51)]  # userId from "1" to "50"
    item_ids = [f"Item{i}" for i in range(1, 15)]  # itemId from "Item1" to "Item14"
    rows = 100  # Number of rows for the mock data

    # Generate mock data
    mock_data = {
      "userId": [random.choice(user_ids) for _ in range(rows)],
      "itemId": [random.choice(item_ids) for _ in range(rows)]
    }

    # Create DataFrame
    df = pd.DataFrame(mock_data)
    return df

  def generateDataFrameWithFilePath(self, file_path):
    # Parameters
    user_ids = [str(i) for i in range(1, 51)]  # userId from "1" to "50"
    item_ids = [f"Item{i}" for i in range(1, 15)]  # itemId from "Item1" to "Item14"
    rows = 100  # Number of rows for the mock data

    # Generate mock data
    mock_data = {
      "userId": [random.choice(user_ids) for _ in range(rows)],
      "itemId": [random.choice(item_ids) for _ in range(rows)]
    }

    # Create DataFrame and FileWrite
    df = pd.DataFrame(mock_data)
    df.to_csv(file_path, index=False)