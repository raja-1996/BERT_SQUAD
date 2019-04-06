


class Config:

    def __init__(self):
        self.bert_model = 'bert-base-uncased'
        self.command_line = False
        self.do_lower_case = True
        self.do_predict = True
        self.do_train = False
        self.doc_stride = 128
        self.fp16 = False
        self.gradient_accumulation_steps = 1
        self.learning_rate = 3e-05
        self.local_rank = -1
        self.loss_scale = 0
        self.max_answer_length = 30
        self.max_query_length = 64
        self.max_seq_length = 384
        self.n_best_size = 20
        self.no_cuda = False
        self.null_score_diff_threshold = 0.0
        self.num_train_epochs = 2.0
        self.output_dir = 'bert_squad_app/bert_squad/debug_squad'
        self.predict_batch_size = 8
        self.predict_file = 'bert_squad_app/bert_squad/squad/test.json'
        self.seed = 42
        self.train_batch_size = 12
        self.train_file = 'bert_squad_app/bert_squad/squad/train-v1.1.json'
        self.trained_model_path = 'bert_squad_app/bert_squad/squad_bert_base'
        self.verbose_logging = False
        self.version_2_with_negative = False
        self.warmup_proportion = 0.1