import dotenv
from langchain.chains import SequentialChain

from langchain.globals import set_debug

from langchain.chat_models import ChatOpenAI

from langchain.schema import StrOutputParser

from modules.chains.article import article_chain
from modules.chains.keyword import *
from modules.chains.outline import *

dotenv.load_dotenv()

set_debug(True)

llm = ChatOpenAI(model_name="gpt-4")

overall_chain = SequentialChain(
    chains=[more_keyword_chain, key_list_chain, title_chain, outline_chain, article_chain],
    # chains=[more_keyword_chain, key_list_chain],
    input_variables=["keyword"],
    output_variables=["關鍵字清單", "大量關鍵字", "文章標題", "文章大纲", "文章"],
    # output_variables=["關鍵字清單", "大量關鍵字"],
    verbose=True
)

keyword = input("请输入要生成文章的主要关键字：")

response = overall_chain.invoke({"keyword": keyword})

# 打开一个文件
fo = open("seo.txt", "w+")
fo.write(response["文章"])

# 关闭打开的文件
fo.close()
