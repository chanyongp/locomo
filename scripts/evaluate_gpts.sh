# sets necessary environment variables
source scripts/env.sh

# # Evaluate gpt-4-turbo
# python3 task_eval/evaluate_qa.py \
#     --data-file $DATA_FILE_PATH --out-file $OUT_DIR/$QA_OUTPUT_FILE \
#     --model gpt-4-turbo --batch-size 20

# python3 task_eval/evaluate_qa.py \
#     --data-file $DATA_FILE_PATH --out-file $OUT_DIR/$QA_OUTPUT_FILE \
#     --model gpt-4o-mini --batch-size 20

python3 task_eval/evaluate_qa.py \
    --data-file $DATA_FILE_PATH --out-file $OUT_DIR/$QA_OUTPUT_FILE \
    --model gpt-4o-mini --batch-size 20

# # Evaluate gpt-3.5-turbo under different context lengths
# for MODEL in gpt-4o-mini gpt-4-turbo o1-preview; do
#     python3 task_eval/evaluate_qa.py \
#         --data-file $DATA_FILE_PATH --out-file $OUT_DIR/$QA_OUTPUT_FILE \
#         --model $MODEL --batch-size 20
#         # --data-file ./data/locomo10_copy.json --out-file ./output/locomo10_qa.json \
# done
