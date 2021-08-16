#%% import required libraries
from transformers import pipeline
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification    
model_path = 'models' # will be created automatically if not exists

#%% download and save the model to local directory
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
model = TFAutoModelForSequenceClassification.from_pretrained(model_name, from_pt=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
classifier.save_pretrained(model_path)
#%% test if it works
classifier(["iyi"]) # iyi --> good in turkish
# [{'label': '5 stars', 'score': 0.5322708487510681}]
#%% load model from local directory if it works
model = TFAutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
print("----------- transformer model loaded ------------")
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
print("----------- transformer tokenizer loaded ------------")
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
classifier(["iyi"]) # iyi --> good in turkish
# [{'label': '5 stars', 'score': 0.5322708487510681}]
# %%
