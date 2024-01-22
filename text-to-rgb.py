import matplotlib.pyplot as plt
def text_to_rgb_and_plot(text):
   # ステップ1: 文章を数値に変換
   numeric_values = [ord(char) for char in text]
   # ステップ2: 数値の総和を計算
   total_sum = sum(numeric_values)
   # ステップ3: 6桁の数字に変換
   six_digit_number = total_sum % 1000000
   # ステップ4: 6桁の数字を3分割
   split_numbers = [six_digit_number // (10 ** i) % 100 for i in (4, 2, 0)]
   # ステップ5: RGB値を計算
   rgb_values = [int((num / 100) * 255) for num in split_numbers]
   # ステップ6: 描画
   color = (rgb_values[0] / 255, rgb_values[1] / 255, rgb_values[2] / 255)
   plt.figure(figsize=(3, 3))
   plt.imshow([[color]])
   plt.axis('off')
   plt.show()
# 例として、"こんにちは"という日本語の文章をRGB値に変換し、描画する
example_text = "こんにちは"
text_to_rgb_and_plot(example_text)