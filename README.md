
# How to containerize a HuggingFace Transformers Model using Docker? 

*I assume you already a little bit familiar with below libraries and docker.* 
**Required libraries:** Flask, transformers, tensorflow. (pip or conda as you wish, I used pip) 
- If you are using tensorflow, as I do, you will need PyTorch only if you are using a hf model trained on PyTorch, with the flag from_pt=true. But, to reload and re-use the model from local you don’t need PyTorch again, so will not be needed in your container. 
 - Step 1: Load and save the transformer model in a local directory using save_hf_models.py 
 - Step 2: Create a minimal flask app, in fact you can use the above one without changing anything. Just replace your model with the one in the models directory. Recommend to test your app at this level. 
 - Step 3: Containerize the app using Dockerfile:
		  `docker build --tag mlapp . `
		  `docker run -i -p 9000:5000 mlapp` *(add -d flag to run in detach mode in the background, you can 9000 as you need)* 
		- Check if your docker is up and running 
		  `docker ps`

| CONTAINER ID |  IMAGE |  COMMAND |  CREATED |  STATUS  | PORTS | NAMES | 
|--------------|--------|----------|----------|----------|-------|-------|
| 1fbcac69069c |  mlapp |  "python app.py" |  50 seconds ago |  Up 49 seconds |  0.0.0.0:9000->5000/tcp |  crazy_pike | 

- Check if the container is responding `curl 127.0.0.1:9000 -v`
- Step 4: Test your model with make_req.py. Please note that your data should be in the correct format, for example, as you tested your model in save_hf_model.py. 
- Step 5: To stop your docker container 
			`docker stop 1fbcac69069c`

Your model is now running in your container, ready to deploy anywhere. 

## Happy machine learning!
