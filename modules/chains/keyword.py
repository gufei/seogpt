import dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from pydantic.v1 import BaseModel, Field

from modules.prompts.keyword import SEO_PROMPT_TMPL_MAIN_KEYWOD, SEO_PROMPT_TMPL_SEARCH_INTENT, \
    SEO_PROMPT_TMPL_TOPICAL_AUTHORITY, SEO_PROMPT_TMPL_KEYWOD_RELEVANCE

dotenv.load_dotenv()

_llm = ChatOpenAI(model_name="gpt-4")

_more_template = SEO_PROMPT_TMPL_MAIN_KEYWOD + SEO_PROMPT_TMPL_SEARCH_INTENT + SEO_PROMPT_TMPL_TOPICAL_AUTHORITY + """
現在你已經認識主要關鍵字，認識搜尋意圖search intent，認識Topical Authority。
請提供我一份跟主要關鍵字[{keyword}]在搜尋意圖關聯性高的關鍵字清單，這份關鍵字清單需要以搜尋意圖為根據找出相關聯且可以幫我建立topical Authority的關鍵字。請將這份清單用表格方式呈現，第一欄位是搜尋意圖，第二欄位是7個主要關鍵字，第三欄位是更多關聯性高的關鍵字。
"""

more_prompt_template = ChatPromptTemplate.from_template(template=_more_template)

more_keyword_chain = LLMChain(llm=_llm, prompt=more_prompt_template, output_key="關鍵字清單")

_key_list_template = SEO_PROMPT_TMPL_KEYWOD_RELEVANCE + """
当前任务：
這是1個主要關鍵字[{keyword}]，以下是和主要關鍵字關聯性高的關鍵字清單：
-------------
{關鍵字清單}
-------------

請幫我依照關鍵字關聯性強弱找到更多關鍵字，相關關鍵字不限，h2關鍵字至少需要3個，h3關鍵字至少需要5個

{format_instructions}
"""


class KeywordModel(BaseModel):
    keyword: str = Field(description="主要關鍵字,keyword")
    h1: str = Field(
        description="相關關鍵字是當人們搜尋主要關鍵字時，Google建議其他人也搜尋的內容，所以相關關鍵字是跟主要關鍵字關聯性最高的")
    h2: str = Field(
        description="h2關鍵字是當人們搜尋主要關鍵字時，出現排名第一名的文章內容用到的h2標題，h2關鍵字跟主要關鍵字關聯性排名第2重要。")
    h2: str = Field(
        description="h3關鍵字是當人們搜尋主要關鍵字時，出現排名第一名的文章內容用到的h3標題，文章h3關鍵字跟主要關鍵字關聯性排名第3重要。")


parser = PydanticOutputParser(pydantic_object=KeywordModel)
key_list_prompt_template = ChatPromptTemplate.from_template(template=_key_list_template,
                                                            partial_variables={
                                                                "format_instructions": parser.get_format_instructions()})
key_list_chain = LLMChain(llm=_llm, prompt=key_list_prompt_template, output_key="大量關鍵字")
