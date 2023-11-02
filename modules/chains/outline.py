import dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from modules.prompts.keyword import *
from modules.prompts.seo import *

dotenv.load_dotenv()

_llm = ChatOpenAI(model_name="gpt-4")

_title_template = SEO_PROMPT_TMPL_MAIN_KEYWOD + SEO_PROMPT_TMPL_SEARCH_INTENT + SEO_PROMPT_TMPL_TOPICAL_AUTHORITY + SEO_PROMPT_TMPL_EEAT + SEO_PROMPT_TMPL_TITLE + """
目前任务：
我要你使用我提供的1個主要關鍵字製作1篇文章標題。記得把1個主要關鍵字分別放入1個標題中。
我一次提供你1個主要關鍵字，同時也提供你大量[{keyword}]關鍵字，
[1]個主要關鍵字是[{keyword}]
大量關鍵字如下：

{大量關鍵字}

請你從大量關鍵字中幫我找出跟1個主要關鍵字關聯性最高的相關關鍵字、關聯性第2的h2關鍵字(不少於3個)、關聯性第3的h3關鍵字(不少於5個)，接著使用1個主要關鍵字製作1篇文章標題，請在每個標題後方加上該篇文章需包含的各個關鍵字。
記得製作文章標題時必須考量到SEO文章寫法把主要關鍵字放到標題中，也必須考量到EEAT，挑選關鍵字時需考量到搜尋意圖search intent，挑選關鍵字時也要考量到能夠成為topical authority。
"""

title_prompt_template = ChatPromptTemplate.from_template(
    template=_title_template)

title_chain = LLMChain(llm=_llm, prompt=title_prompt_template, output_key="文章標題")

_outline_template = SEO_PROMPT_TMPL_MAIN_KEYWOD + SEO_PROMPT_TMPL_SEARCH_INTENT + SEO_PROMPT_TMPL_TOPICAL_AUTHORITY + SEO_PROMPT_TMPL_EEAT + SEO_PROMPT_TMPL_TITLE + """

你已經了解搜尋意圖、主要關鍵字、topical authority、EEAT和寫SEO文章的方式。

我提供的素材为
文章主要關鍵字:[{keyword}]
相關大量關鍵字:{大量關鍵字}
文章標題與內容需要包含關鍵字:{文章標題}

当前任务:
請幫我產出一篇文章的大綱
需要列出包含進每个大纲段落的搜索關鍵字用括弧()標註，確保文章的結構明確且完整。
"""

outline_prompt_template = ChatPromptTemplate.from_template(template=_outline_template)

outline_chain = LLMChain(llm=_llm, prompt=outline_prompt_template, output_key="文章大纲")
