import dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from modules.prompts.keyword import *
from modules.prompts.seo import *

dotenv.load_dotenv()

_llm = ChatOpenAI(model_name="gpt-4")

_article_template = SEO_PROMPT_TMPL_MAIN_KEYWOD + SEO_PROMPT_TMPL_SEARCH_INTENT + SEO_PROMPT_TMPL_TOPICAL_AUTHORITY + SEO_PROMPT_TMPL_EEAT + SEO_PROMPT_TMPL_TITLE + """

你是一个SEO领域的专业人士，非常擅长书写SEO友好亲和的文章
以下是主要關鍵字[{keyword}]对应的文章大纲
{文章大纲}
------------
請在充分考慮到SEO、EEAT、搜尋意圖及專家、權威、可信度因素、SEO文章上首頁的方式，以幫助文章在搜尋結果中取得更好的排名的前提下。幫我把大纲的每个段落詳細地展開說明，生成符合SEO的文章
"""

article_prompt_template = ChatPromptTemplate.from_template(template=_article_template)

article_chain = LLMChain(llm=_llm, prompt=article_prompt_template, output_key="文章")