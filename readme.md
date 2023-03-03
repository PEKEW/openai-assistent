# OpenAI-command line assistent

> OpenAI-command line assistent 是一个使用 OpenAI GPT 模型实现的命令行助手。


## 安装

### 克隆此代码库：

```bash
git clone https://github.com/PEKEW/openai-assistent.git
```

### 安装必要的依赖：


```bash
pip install -r requirements.txt
```

## 使用

- 添加 OpenAI API 密钥到 `api.ini` 文件中。

- 运行 `bot.py 文件：


```bash
python3 bot.py
```

输入 reset!! 来重置会话，或输入 quit!! 来退出。


## TODO

- [ ] 内存优化，context太长时，考虑使用文件流
- [ ] 用户输入过滤
- [ ] 输入指示符会被删除的问题

# OpenAI-command line assistent

> OpenAI-command line assistent is a command line assistent bot implemented using OpenAI GPT model.

## Installation

### Clone this repository:

```bash
git clone https://github.com/PEKEW/openai-assistent.git
```

### Install the necessary dependencies:


```bash
pip install -r requirements.txt
```

## Usage

- Add your OpenAI API key to the `api.ini` file.

- Run the `bot.py` file:


```bash
python bot.py
```

You can enter reset!! to reset the session or quit!! to exit the Chatbot.

## TODO

- [ ] Memory optimization, consider using a file stream when the context is too long 
- [ ] User input filtering
- [ ] An issue that input indicators are deleted


