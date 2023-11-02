# seogpt

### 命令行直接运行
```
pip install -r requirements.txt
python seo.py
```


### 生成可执行文件

```
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --paths ".venv/:modules/" --collect-data=langchain --onefile --name "ai_seo" seo.py
```