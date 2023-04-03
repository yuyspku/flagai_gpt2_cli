import argparse
from flagai.auto_model.auto_loader import AutoLoader
from flagai.model.predictor.predictor import Predictor

def process_args():
    # 定义命令行参数
    parser = argparse.ArgumentParser(prog='GPT2 cli',
                                     description='CLI interface for GPT2 chinese')
    parser.add_argument(
                        'prompt', 
                        type=str, 
                        default="介绍一下这款篮球鞋", 
                        help='Prompt for the language model. \n'
    )
    
    parser.add_argument('--gen_type', 
                        type=int, 
                        default=0, 
                        help='type of generating text')
    
    parser.add_argument('--model_dir', 
                        type=str, 
                        default="./checkpoints/", 
                        help='GPT2 model path')

    parser.add_argument(
                        '--out_max_length', 
                        type=int, 
                        default=100,
                        help="Maximum length in tokens of the generated text"
                        "If None, then 100 is used."
    )

    return parser.parse_args()


def main(args):
    loader = AutoLoader("seq2seq",
                        "GPT2-base-ch",
                        model_dir=args.model_dir)
    
    model = loader.get_model()
    tokenizer = loader.get_tokenizer()
    predictor = Predictor(model, tokenizer)

    text = args.prompt
    out_max_len = args.out_max_length
    #print(text)

    if args.gen_type == 0:
        out = predictor.predict_generate_beamsearch(text,
                                                    beam_size=5,
                                                    input_max_length=512,
                                                    out_max_length=out_max_len)
    else:
        out = predictor.predict_generate_randomsample(text,
                                                    input_max_length=512,
                                                    out_max_length=out_max_len,
                                                    repetition_penalty=1.5,
                                                    top_k=20,
                                                    top_p=0.8)

    print(f"结果如下：{text}{out}")

if __name__ == '__main__':
    main(process_args())
