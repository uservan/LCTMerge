# LCTMerge

## train
- we use LLama-Factory to train the model
- for example
```shell
FORCE_TORCHRUN=1 NNODES=1 NODE_RANK=0 llamafactory-cli train $CONFIG examples/train_full/llama3_r1_8b_long_rope.yaml
```

## eval
- we follow the recipe of Sky-thought
```shell
python skythought_evals/eval.py \
    --model model_path \
    --evals math500,aime,gpqa_diamond,gsm8k \
    --n 5 \
    --result-dir result_dir \
    --tp 1 \
```
