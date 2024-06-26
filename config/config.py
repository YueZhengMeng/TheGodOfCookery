import os
from collections import defaultdict

# 总的config
Config = defaultdict(dict)

# global variables
Config['global'] = {
    'enable_rag': True,
    'streaming': None,
    'enable_markdown': None,
    'enable_image': None,
    'user_avatar': "assets/user.png",
    'robot_avatar': "assets/robot.png",
    'user_prompt': '<|im_start|>user\n{user}<|im_end|>\n',
    'robot_prompt': '<|im_start|>assistant\n{robot}<|im_end|>\n',
    'cur_query_prompt': '<|im_start|>user\n{user}<|im_end|>\n<|im_start|>assistant\n',
    'error_response': "我是食神周星星的唯一传人，我什么菜都会做，包括黑暗料理，您可以问我什么菜怎么做———比如酸菜鱼怎么做？我会告诉你具体的做法。如果您遇到一些异常，请刷新页面重新提问。",
    # 'rag_framework': "langchain", # 选择使用的RAG框架
    'rag_framework': "llama-index",
    'xlab_deploy': False
}

# llm
Config['llm'] = {

    'load_4bit': True,

    # 1.8b 二代
    'base_model_type': "internlm2-chat-1.8b",
    # 'finetuned': True,
    # 'llm_model_path': os.environ.get('HOME') + "/models/zhanghuiATchina/zhangxiaobai_shishen2_1_8b",
    'finetuned': False,
    'llm_model_path': os.environ.get('HOME') + "/models/Shanghai_AI_Laboratory/internlm2-chat-1_8b",

    # 7b 二代
    # 'base_model_type': "internlm2-chat-7b",
    # 'finetuned': True,
    # 'llm_model_path': os.environ.get('HOME') + "/models/zhanghuiATchina/zhangxiaobai_shishen2_full",
    # 'finetuned': False,
    # 'llm_model_path': os.environ.get('HOME') + "/models/Shanghai_AI_Laboratory/internlm2-chat-7b",

    # 7b 一代
    # 'base_model_type': "internlm-chat-7b",
    # 'finetuned': True,
    # 'llm_model_path': os.environ.get('HOME') + "/models/" + "zhanghuiATchina/zhangxiaobai_shishen_full",
    # 'finetuned': False,
    # 'llm_model_path': os.environ.get('HOME') + "/models/Shanghai_AI_Laboratory/internlm-chat-7b",
}

# speech
Config['speech'] = {
    'speech_model_type': "paraformer",
    'audio_save_path': "/tmp/audio.wav",
    'speech_model_path': os.environ.get('HOME')
                         + "/models/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
}

# RAG with LangChain
Config['rag_langchain'] = {
    # 'rag_model_type': "chroma", # 使用chroma数据库
    'rag_model_type': "faiss",  # 使用faiss数据库
    'verbose': True,  # 是否打印详细的模型输入内容信息
    'dataset_config': {
        'data_path': "./data/tran_dataset_1000.json",  # 这里更换为完整的数据集路径
        'test_count': 1000  # 测试数据量，填入-1表示使用全部数据
    },
    'emb_strategy': {
        "source_caipu": False,  # 是否编码原始菜谱
        "HyQE": True,  # 是否使用HyQE
    },
    # streamlit加载使用的相对路径格式和直接运行python文件使用的相对路径格式不同
    'faiss_config': {
        'save_path': './faiss_index',  # 保存faiss索引的路径
        'load_path': './rag_langchain/faiss_index',  # streamlit加载faiss索引的路径
        'search_type': "similarity_score_threshold", # 搜索方式，指定相似度指标
        'search_kwargs': {"k": 3, "score_threshold": 0.6} # k: 保留top-k, score_threshold为相似度阈值
    },
    # chroma_config 键已弃用
    # 'chroma_config': {
    #     'save_path': './chroma_db',  # 保存chroma索引的路径
    #     'load_path': './rag_langchain/chroma_db',  # streamlit加载chroma索引的路径
    #     'search_type': "similarity", # 使用点积相似度标准搜索
    #     'search_kwargs': {"k": 3} # 保留top-k
    # },
    'bm25_config': {
        'dir_path': './retriever',  # 保存bm25检索器的文件夹的路径
        'save_path': './retriever/bm25retriever.pkl',  # 保存bm25检索器的路径
        'load_path': './rag_langchain/retriever/bm25retriever.pkl',  # streamlit加载bm25检索器的路径
        'search_kwargs': {"k": 3} # 保留top-k
    },
    'bce_emb_config': {
        'model_name': os.environ.get('HOME') + "/models/bce-embedding-base_v1", # 模型路径
        'model_kwargs': {'device': 'cuda:0'}, # 加载模型的其他可选参数，这里设置了加载到GPU
        'encode_kwargs': {'batch_size': 32, 'normalize_embeddings': True, 'show_progress_bar': False} # 进行encode时的超参设置
    },
    'bce_reranker_config': {
        'model': os.environ.get('HOME') + "/models/bce-reranker-base_v1", # 模型路径
        'top_n': 1, # 保留top-n
        'device': 'cuda:0', # 加载设备
        'use_fp16': True # 模型参数精度是否使用fp16
    }
}

# RAG with llama-index
Config['rag_llama'] = {
    'rag_model_type': "faiss",  # 使用faiss数据库
    'verbose': True,  # 是否打印详细的模型输入内容信息
    'dataset_config': {
        'data_path': "./data/tran_dataset_1000.json",  # 这里更换为完整的数据集路径
        'test_count': 1000  # 测试数据量，填入-1表示使用全部数据
    },
    'emb_strategy': {
        "source_caipu": False,  # 是否编码原始菜谱
        "HyQE": True,  # 是否使用HyQE
    },
    # streamlit加载使用的相对路径格式和直接运行python文件使用的相对路径格式不同
    'faiss_config': {
        'save_path': './faiss_index',  # 保存faiss索引的路径
        'load_path': './rag_llama/faiss_index',  # streamlit加载faiss索引的路径
        'search_type': "similarity_score_threshold",
        'search_kwargs': {"k": 3, "score_threshold": 0.6}
    },
    'bm25_config': {
        'dir_path': './retriever',  # 保存bm25检索器的文件夹的路径
        'save_path': './retriever/bm25retriever.pkl',  # 保存bm25检索器的路径
        'load_path': './rag_llama/retriever/bm25retriever.pkl',  # streamlit加载bm25检索器的路径
        'search_kwargs': {"k": 3}
    },
    'bce_emb_config': {'model_name': os.environ.get('HOME') + "/models/bce-embedding-base_v1",
                       'max_length': 512,
                       'embed_batch_size': 32,
                       'device': 'cuda:0'
                       },
    'bce_reranker_config': {
        'model': os.environ.get('HOME') + '/models/bce-reranker-base_v1',
        'top_n': 1,
        'device': 'cuda:0',
        'use_fp16': True
    }
}

# 文生图部分config
Config['image'] = {
    'image_model_type': 'stable-diffusion',
    # 'image_model_type': 'glm-4',
    'image_model_config': {
        'stable-diffusion': {
            "model_path": os.environ.get('HOME') + "/models/Taiyi-Stable-Diffusion-1B-Chinese-v0.1",
            "lora_path": 'gen_image/lora_weights/meishi.safetensors',
            "lora_scale": 0.75  # range[0.,1.]
        },
        'glm-4': {
            "api_key": "*****"
        }
    }
}
