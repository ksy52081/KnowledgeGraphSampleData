import torch

import torch.nn as nn

# TensorFlow AutoEncoder 모델 정의
class AutoEncoder(tf.keras.Model):
    def __init__(self):
        super(AutoEncoder, self).__init__()
        self.encoder = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu')
        ])
        self.decoder = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(784, activation='sigmoid')
        ])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# TensorFlow 모델 인스턴스 생성
model_tf = AutoEncoder()

# TensorFlow 모델 가중치를 PyTorch 모델로 변환
model_pt = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 64),
    nn.ReLU(),
    nn.Linear(64, 128),
    nn.ReLU(),
    nn.Linear(128, 784),
    nn.Sigmoid()
)

# TensorFlow 모델 가중치를 PyTorch 모델로 복사
for i, layer in enumerate(model_tf.layers):
    model_pt[i].weight.data = torch.tensor(layer.get_weights()[0].T)
    model_pt[i].bias.data = torch.tensor(layer.get_weights()[1])

# PyTorch 모델 사용 예시
input_tensor = torch.randn(1, 784)
output_tensor = model_pt(input_tensor)