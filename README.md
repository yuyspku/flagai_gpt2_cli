# Introduction to GPT-2 model(Deep Learning Class on LLMs)

# CLI interface for GPT-2 LLM
A simple cli for the GPT-2 LLM. 

## Installation 

https://github.com/FlagAI-Open/FlagAI

- To install FlagAI with pip:
```shell
pip install -U flagai
```
## Usage
After installing the CLI interface with pip you can use it from anywhere via your commandline:
```bash
gpt2_cli "据报道"
```

## Features

```
usage: GPT2 cli [-h] [--gen_type GEN_TYPE] [--model_dir MODEL_DIR] [--out_max_length OUT_MAX_LENGTH] prompt

CLI interface for GPT2 chinese

positional arguments:
  prompt                Prompt for the language model.

optional arguments:
  -h, --help            show this help message and exit
  --gen_type GEN_TYPE   type of generating text
  --model_dir MODEL_DIR
                        GPT2 model path
  --out_max_length OUT_MAX_LENGTH
                        Maximum length in tokens of the generated textIf None, then 100 is used.
```
See https://github.com/openai/gpt-2 for more information on the GPT-2 model.
