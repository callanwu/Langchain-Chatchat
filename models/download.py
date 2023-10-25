from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download('ZhipuAI/chatglm2-6b', cache_dir='.')
embedding_dir = snapshot_download('thomas/m3e-base', cache_dir='.')