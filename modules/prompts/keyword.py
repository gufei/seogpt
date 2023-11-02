from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

SEO_PROMPT_TMPL_MAIN_KEYWOD = '''[主要關鍵字]
SEO關鍵字是添加到網路內容中的詞語，以改善這些詞語的搜尋引擎排名。大多數關鍵字是在關鍵字研究過程中發現的，並根據搜索量、競爭和商業意圖的組合選擇。
如果頁面專注於一個主題，那麼它更容易排名，因此你應該每篇文章專注於一個主要關鍵字。一篇文章中要定位4個或更多關鍵字是困難的，因為每個主要關鍵字都代表一個搜尋意圖，而一篇文章不應該有多個搜尋意圖，這樣會讓使用者混淆，導致文章在SERP頁面排名下降。
'''

SEO_PROMPT_TMPL_SEARCH_INTENT = '''[搜尋意圖search intent]
搜索意圖 search intent（也稱為“用戶意圖”）是使用者在輸入查詢詞時使用搜索引擎時的主要目標。常見的搜索意圖類型包括信息、商業、導航和交易。
例如，假設使用者想晚餐煮義大利麵，而且使用者很餓，想要立刻吃，於是使用者前往Google搜索『快速義大利麵食譜』。
第一個點擊的結果看起來還可以。但使用者將很快意識到這個食譜需要30分鐘才能完成一道義大利麵，因此，使用者將很快點擊其他搜索結果。
接下來你在第3名找到了符合需求的結果，因為這個結果是從開始到結束需要10分鐘的食譜，如果足夠多搜索『快速義大利麵食譜』的人有相同的感覺，那麼這原本在第3名的結果將獲得顯著的排名提升。
所以你提供的內容符合使用者搜尋意圖，排名將快速提升。所以你知道了，搜索意圖很重要的原因：滿足使用者搜索意圖是Google的首要目標。
搜索意圖需要成為你幫我製作SEO內容方法的重要組成部分。
知識性搜尋：使用者想要獲取特定的知識或資訊，例如如何使用某個產品、某個地方的旅遊資訊等等。這種搜尋意圖通常會以問題的形式出現，例如「如何…」、「什麼是…」等等。

導購性搜尋：使用者想要購買某種產品或服務，但還沒有確定品牌或型號。這種搜尋意圖通常會包含一些關鍵字，例如「最好的…」、「比較…」等等。

比較性搜尋：使用者想要比較不同品牌或產品之間的差異，以便做出更好的選擇。這種搜尋意圖通常會包含一些比較詞語，例如「vs.」、「與…相比」等等。

獲取性搜尋：使用者想要獲取某些特定內容，例如下載文件、看影片等等。這種搜尋意圖通常會包含一些具體的內容類型，例如「下載…」、「看…影片」等等。

了解使用者的搜尋意圖對於網站的SEO非常重要。如果網站能夠滿足使用者的搜尋意圖，那麼就能夠吸引更多的訪客，提高網站的流量和轉換率。因此，在進行關鍵字研究和編寫網站內容時，應該針對不同的搜尋意圖，撰寫相應的內容。這樣不僅能夠提高網站的排名和流量，也能夠提高使用者對網站的滿意度和忠誠度。

我再提供你關於SEO中的[搜尋意圖 search intent]的案例，使用這個案例希望能協助你更了解什麼是搜尋意圖。請先不用回答任何問題，我會陸續相關資料，看完後請回覆我[OK，請提供更多資料]。

搜尋意圖分析SEO案例

以我幫一位音樂產業的客戶進行關鍵字架構與市場為案例，當搜尋關鍵字[YOUTUBE音樂]時，你可以從搜尋意圖發現不同的目標受眾和推廣方式。

對於想要找到免費音樂素材的自媒體工作者而言，他們通常會使用搜尋關鍵字「Youtube免費音樂」，這些關鍵字通常會和「編輯」、「剪片」等相關關鍵字出現在一起，可以從各大線上音樂庫的搜尋關鍵字觀察出。

對於想要在YouTube上找到免費音樂來聽的一般使用者，他們會使用搜尋特定音樂類型的關鍵字，例如白噪音、療癒音樂，相關搜尋會出現Youtube。

根據使用者的不同需求和目的，可以將他們分為兩類目標受眾，並且可以從中得到兩個不同的市場切入方向。

自媒體工作者通常會使用關鍵字「免費」、「版權」等相關關鍵字
一般使用者則會使用關鍵字「無廣告」、「特定類型音樂」等相關關鍵字。
'''

SEO_PROMPT_TMPL_TOPICAL_AUTHORITY = '''[Topical Authority]
Imagine if your website (or clients) could rank for every single keyword related to a desired niche.
Enter topical authority.
Now imagine that you could even achieve this with no link building.
If some people in the SEO world are to be believed, this is achievable by anyone willing to write content about absolutely everything within a topic.
But realistically, you should still expect to build links and do a lot of other SEO activities. Topical authority is not a silver bullet.
But it’s still worth your time. 
In this guide, you will learn everything you need to know about topical authority and how to build it for your sites.
What is topical authority?
Topical authority is an SEO concept where a website aims to become the go-to authority on one or more topics. 
Building topical authority is about helping search engines understand a website’s topic so that it has better potential to rank for topically related keywords.
Let’s say you want to rank articles around the topic of protein powder. Writing just the one article targeting “protein powder” is probably not enough to compete in this niche.
Why? Because it’s a massive topic and you can’t possibly cover everything about it in one article.
To build topical authority, you need to cover everything related to protein, such as: 
“what is protein”
“what does protein powder do”
“what is the best protein powder”
“how to use protein powder”
“how long does protein powder last”
“how to use protein powder for weight loss”
Topical authority is achieved when a site fully covers a topic as a whole rather than focusing on just individual keywords.

Why is topical authority important (for SEO)?
Google, as a search engine, works with semantic associations. This means it has to associate a website with a topic in order to rank it as a relevant resource for keywords that are part of that topic.
If you have a lot of content about a certain topic, this allows for more relevant internal links, which allow Google and users to find your content more easily which, in turn, may land you more natural backlinks.
If you take away nothing else from the concept of building topical authority, take this:
When you create content pieces around the same subject and interlink them, your topical authority in the eyes of Google increases. This helps to show it that you’re knowledgeable, aka an authority on the topic and a trusted source.

build topical authority in four steps
So how do you build topical authority for your site?
First, you need to cover all the obvious SEO basics. Assuming you’ve got the basics covered, building topical research is pretty straightforward. 
In very simple terms, you need to:
Do keyword research to find all the talking points within a topic.
Organize that data into topic clusters.
Produce content that meets the search intent of those topic keywords.
Build relevant internal and external links to your content.
At the risk of becoming an authority on the topic of wasting time by rambling on about things no one really knows other than Google…
Let’s crack on and learn how to build some topical authority.
Create topic clusters
Topic clusters are interlinked pages about the same subject. The purpose of them is to group relevant content together so that it is easier to find by both users and Google.
Armed with your keyword research, you’ll want to organize your list of terms into clusters based on search intent while also considering traffic potential. 
Your topics should have good traffic potential and typically be informational in intent, like this:
Ahrefs’ Keywords Explorer overview for subtopics
Pick a topic for your cluster (or pillar page) that is relevant for your site to target and has enough depth that you will have subtopics to explore. 
Now, you’ll want to pick the most appropriate content format to create for the cluster: 
Guides – An evergreen content format that fully covers a specific topic. 
What is X – A deep-dive definition or answer to a question. 
How to X – A step-by-step tutorial detailing how to do a specific task.
These pages should be well structured with enough content to be useful as stand-alone articles but also link to more in-depth articles within the topic.  
'''

SEO_PROMPT_TMPL_KEYWOD_RELEVANCE = '''[關鍵字關聯性強弱]
接下來我要告訴你關鍵字關聯性強弱是什麼，我會提供你4個資料：主要關鍵字、相關關鍵字、h2關鍵字、h3關鍵字。
相關關鍵字是當人們搜尋主要關鍵字時，Google建議其他人也搜尋的內容，所以相關關鍵字是跟主要關鍵字關聯性最高的。
h2關鍵字是當人們搜尋主要關鍵字時，出現排名第一名的文章內容用到的h2標題，h2關鍵字跟主要關鍵字關聯性排名第2重要。
h3關鍵字是當人們搜尋主要關鍵字時，出現排名第一名的文章內容用到的h3標題，文章h3關鍵字跟主要關鍵字關聯性排名第3重要。
以下我開始提供案例給你：
主要關鍵字是[期貨是什麼]
相關關鍵字[期貨玩法、期貨風險、台指期貨是什麼、期貨怎麼買、期貨介紹、期貨一口]
h2關鍵字[期貨是什麼、各種類型的期貨、什麼是期貨保證金、期貨手續費、期貨的優勢]
h3關鍵字是[手續費、交易稅、交割、本金、商品流動性、交易槓桿、期貨當沖教學、技術分析教學、台指期夜盤怎麼玩]
'''

