from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba
 
# 分词
def trans_CN(text):
	# 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result
 
with open("./111.txt") as fp:
    text = fp.read()
    # 将读取的中文文档进行分词
    text = trans_CN(text)
    mask = np.array(image.open("/home/malong/love.png"))
    wordcloud = WordCloud(
    	# 添加遮罩层
        mask=mask,
        # 生成中文字的字体,必须要加,不然看不到中文
        font_path = "./fonts/simhei.ttf"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()

