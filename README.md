# Own-ChatGPT 

Use ChatGPT in the Terminal with custom Data.

## Installation

```bash
pip3 install langchain
pip3 install openai
pip3 install chromadb
pip3 install tiktoken
```

Modify `constants.py` to use your own [OpenAI API Key](https://platform.openai.com/account/api-keys).

Place your own data into `data.txt`.

## Example usage

```bash
$ python3 chatgpt.py "What's my favorite Color?"
Your favorite color is blue.
```
