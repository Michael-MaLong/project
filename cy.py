# coding = "utf-8"
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import jieba
import time


class  Cy(object):

	def GetWordCloud(self):
	    path_txt = './23tips.txt'
	    path_img = "/home/malong/love.png"
	    f = open(path_txt, 'r', encoding='UTF-8').read()
	    background_image = np.array(Image.open(path_img))
	    cut_text = " ".join(jieba.cut(f))
	    wordcloud = WordCloud(
	        # 设置字体，不然会出现口字乱码
	        font_path="./fonts/simhei.ttf",
	        # background_color="white",
	        mask=background_image
	    ).generate(cut_text)
	    # 生成颜色值
	    image_colors = ImageColorGenerator(background_image)
	    # 下面代码表示显示图片
	    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
	    plt.axis("off")
	    plt.show()



	def run(self):
		while True:
			Cy().GetWordCloud()
			time.sleep(5)


if __name__ == '__main__':
	while  True:
	    Cy().run()
	# Cy().GetWordCloud()