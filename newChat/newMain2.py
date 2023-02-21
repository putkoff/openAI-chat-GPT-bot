import functions as fun
import guiFunctions as guiFun
import PySimpleGUI as sg
import json
from datetime import date

import os
import openai
import demoImgh64
import requests
openai.api_key = "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"
def changeGlob(x,y):
    globals()[x]=y
    return y
def openImage(x):
    return Image.open(x)
def addToLs(ls,ls2):
    for k in range(0,len(ls2)):
        ls.append(ls2[k])
    return ls
def getDate():
    return date.today()
def urlToImg(x):
    from PIL import Image
    import requests
    url = x
    response = requests.get(url,stream=True)
    img = Image.open(response.raw)
    img.show()
    return img
def generate_from_masked_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read())
def resizeImg(x,y,z):
    image = openImg(x)
    size = image.size
    if size !=(y,z):
        image = Image.open(x)
        image = image.resize((y, z))
    return image
def openImg(x):
    return Image.open(x)
def streamImage(x):
    byte_stream = BytesIO()
    x.save(byte_stream, format='PNG')
    x = byte_stream.getvalue()
    return x
def imgScreen(x):
    return [sg.Image(data=x, key="-ArtistAvatarIMG-")]
def changeGlob(x,y):
    globals()[x]=y
    return y
def getKeys(js):
    return fun.getKeys(js)
def getVals(js):
    return fun.getVals(js)
def jsGet(js,x):
    if x in js:
        js = js[x]
    return js
def getNewKeys(js,x):
    js = jsGet(js,x)
    return getKeys(js),js
def regetJs(js):
    return jsOg
def ifOnlyOne(js,var):
    if fun.isLs(js[var]):   
        if len(js[var])> 1:
            return js[var]
    return js[js[var]]
def mkJs(js,key,sel):
    jsN = {}
    if sel !=None:
        js = js[sel]
    jsN[key] = getKeys(js)
    return jsN
def ifInJsWLs(ls,js,ls2):
    for i in range(0,len(ls)):
        if ls[i] in js:
            ls2[int(i)] = js[ls[int(i)]]
    return ls2
def ifInJs(js,var):
    return js[var]
def modelSpec(na):
        default,ls = ifInJsWLs(['default','list'],getChoices()[na],['',[]])
        specializedSet['jsList'].append(mkFull(na,mkType([default,specializedSet['paramJs']['object']]),ls,specializedSet['opt'],True,'drop'))
def ifLang(i,na):
    if i == 0:
        return na
    
    elif typ == 'input':
        ls = txtInput(na,ls[0],ls[1])
    elif typ == 'file':
        guiFuns.getBrwsSect(na,parameters[na]['description'],os.getcwd())
        ls = getFileBrowse(na,ls[0],ls[1],ls[2])
def promptSpec(promptJS):
    global category,specializations,categories,specialization,catKeys,specializedSet,catLs,categoriesJs
    if 'vars' in promptJS:
        vars = fun.getKeys(promptJS['vars'])
    vars,ls = fun.mkLs(vars),[]
    for i in range(0,len(vars)):
        if promptJS['vars'][vars[i]]['type'] == 'choice':
            modelSpec(vars[i])
        elif promptJS['vars'][vars[i]]['type'] in ['text','str','list']:
            specializedSet['inputTabKeys']['descriptions'].append(promptJS['vars'][vars[i]]['input'])
            specializedSet['inputTabKeys']['names'].append(vars[i])
            specializedSet['inputTabKeys']['types'].append(promptJS['vars'][vars[i]]['type'])
            specializedSet['inputTabKeys']['index']+=1
def getlsFromBrac(x,obj):
    ls = str(x).replace('{','').replace('}','').replace(' ','').replace(':',',').split(',')
    for i in range(0,len(ls)):
        ls[i] = mkType([ls[i],obj])
    return ls
def getParamMenu(na,js):
    specializedSet['paramJs'] = js
    if na in getChoices():
        modelSpec(na)
    elif na in ['prompt','input']:
        promptSpec(returnParameters(category,specialization)['prompt'])
    else:
        defa,obj,scl = js['default'],js['object'],js['scale']
        if scl == 'upload':
            specializedSet['content'] = 'multipart/form-data' 
            specializedSet['jsList'].append(mkFull(na,'',[js['baseType'],'png.',os.getcwd(),parameters[na]['description']],specializedSet['opt'],True,'file'))
        elif js['object'] == 'bool':
            specializedSet['jsList'].append(mkFull(na,defa,na,specializedSet['opt'],True,'check'))
            
        elif js['object'] in ['float','int']:
          specializedSet['jsList'].append(mkFull(na,mkType([defa,obj]),getlsFromBrac(str(js['range']),js['object']),specializedSet['opt'],True,'slide'))
def selKeys():
    return getKeys(selections)
def ifLsSel(js,key):
    if selections[key] == '':
        return getKeys(js)
    return js[selections[key]]
def ifLsInKeyConc(keys,keyNs,js):
    for k in range(0,len(keys)):
        if returnParameters(category,specialization)['prompt']['vars'][keys[k]]['type'] == 'list':
            n = keys[k]
            for i in range(0,len(keyNs)):
                if str(keys[k])+str(i) in keyNs:
                    if js[str(keys[k])+str(i)] != None and js[str(keys[k])+str(i)] != "None":
                        n = n + ','+str(js[str(keys[k])+str(i)])
            js[keys[k]] = n
    return js
def tryJsTxt(resp):
    for i in range(0,2):
        try:
            js = resp.json()
            return js
        except:
            try:
                txt = resp.text
                return txt
            except:
                print(resp)
    return resp
def whichIsIn(js,ls):
    for i in range(0,len(ls)):
        if ls[i] in getKeys(js):
            return ls[i]
    return ls[0]
def compilePrompt(js):
    ifLsInKeyConc(fun.getKeys(returnParameters(category,specialization)['prompt']['vars']),fun.getKeys(js),js)
    vars,jsN = fun.getKeys(returnParameters(category,specialization)['prompt']['vars']),{}
    if len(vars)>0:
        isIn = whichIsIn(js,['prompt','input'])
        jsN[isIn] = returnParameters(category,specialization)['prompt']['task']+'\n'
        for i in range(0,len(vars)):
            if fun.isLs(js[vars[i]]):
                input(js)
                js[vars[i]] = str(js[vars[i]])[1:-1]
            jsN[isIn] = str(jsN[isIn])+str(returnParameters(category,specialization)['prompt']['vars'][vars[i]]['delimiter'])+str(js[vars[i]])+'\n'     
    prevKeys = specializedSet['prevKeys']
    for i in range(0,len(prevKeys)):
        if prevKeys[i] not in js:
            js[prevKeys[i]] = getAllInfo('parameters')[prevKeys[i]]['default']
        if js[prevKeys[i]] != None and js[prevKeys[i]] != 'None' and js[prevKeys[i]] != '':
            jsN[prevKeys[i]] = ifNotIntFl(js,prevKeys[i])
    try:
        return json.dumps(jsN)
    except:
        return jsN

def getParamDrop(ls):
    category,specialization=ls
    parametsCurr = returnParameters(category,specialization)
    keys= getKeys(parametsCurr)
    opt = ['required','optional']
    
    for i in range(0,len(opt)):
        specializedSet['opt'] = [True,False][i]
        paramLs = parametsCurr[opt[i]]
        for k in range(0,len(paramLs)):
            param = paramLs[k]
            specializedSet['prevKeys'].append(param)
            getParamMenu(param,getAllInfo('parameters')[param])
    specializedSet['inputTabKeys']['inputLs'] = [[sg.Tab(str(specializedSet['inputTabKeys']['names'][i]) if i < len(specializedSet['inputTabKeys']['names']) -1 else '+', tab(i), key=str(specializedSet['inputTabKeys']['names'][i])) for i in range(len(specializedSet['inputTabKeys']['names']))]]
    return  specializedSet['jsList']
def getJson(x):
  return x.json()
def getText(x):
  return x.text
def callJson(ls):
  return getJson(getCall(ls))
def callText(ls):
  return getText(getCall(ls))
def uploadFile(file,purpose):
  return openai.File.create(file=open(file, "rb"),purpose=purpose)
def retrieveFile(id):
  return openai.File.retrieve(id)
def retrieveContent(id):
  return openai.File.download(id)
def listFiles():
  return openai.File.list()
def GETHeader():
  return {"Content-Type": specializedSet['content'] ,"Authorization": "Bearer "+openai.api_key}
def reqGet(js):
  return requests.get('https://api.openai.com/v1/completions',json= json.loads(js),headers=GETHeader())
def reqPost(js):

    if specializedSet['content'] == 'multipart/form-data':
        if 'size' in js:
            sizeN = int(str(js['size']).split('x')[0])                    
        if js['spec'] == 'image_edit':
          return openai.Image.create_edit(image=open(resizeImg(str(js['image']),sizeN,sizeN),'rb'),mask=open(resizeImg(str(js['mask']),sizeN,sizeN),'rb'),prompt = js['prompt'],n=js['n'],size=js['size'],response_format=js['response_format'])
        if js['spec'] == 'image_variation':
            return openai.Image.create_variation(image=open(resizeImg(str(js['image']),sizeN,sizeN),'rb'),n=js['n'],size=js['size'],response_format=js['response_format'])
    js['resp']= requests.post(js['endPoint'],json=json.loads(js['dumped']),headers=GETHeader()).json()
    resp = json.dumps(response)
    fun.pen(resp,'ans.json')
    return getResponse(response,js['response'])
def tryJs(js):
    ls = [js,str(js),str(js).replace('"',"'"),str(js).replace('"','*&*').replace("'",'"')]
    for i in range(0,len(ls)):
        try:
            z = json.loads(ls)
            return z
        except:
            print('strike')
    return False        
def isDict(js):
    if fun.isStr(js) or fun.isInt(js) or fun.isFloat(js) or fun.isLs(js) or fun.isBool(js) or len(getKeys(js))==0 or tryJs(js) == False:
        return False
    return True
def ifThenMkJs(js):
    if isDict(js) != False:
        return json.loads(js)
    return js
def numLs():
    return str('0.1.2.3.4.5.6.7.8.9').split(',')
def ifInReturn(js,ls):
    for i in range(0,len(ls)):
        if ls[i] in js:
            js = js[ls[i]]
            return js
    return js
def ifN(resp,js):
    resp[0],resp[1] = str(resp[0]),int(0)
    if 'n' in js:
         resp[1] = int(js['n'])-1
    if str(resp[-1]) in js:
       resp[-1] = str(js[resp[-1]])
    return resp
def getResp(ls,keys,resp):
    for i in range(0,len(ls)):
        if ls[i] in keys:
            resp = resp[ls[i]]
            return resp
    return resp
def getResponse(resp,rPr):
     
    if rPr[2] == 'url':
        guiFuns.defaultOverWindow(imgScreen(urlToImg(resp)),'iimage')
    resp = json.loads(fun.reader('ans.json'))
    keys = getKeys(resp)
    for k in range(0,2):
        resp=getResp([[rPr[0],'results','choices','data'],[rPr[2],'data','text','url','response_format']][k],keys,resp)
        if fun.isLs(resp):
            keys = resp
            if int(rPr[1])-1 in range(0,len(resp)):
                resp = resp[int(rPr[1])-1]
                print(resp)
            else:
                resp = resp[0]
                print(resp)
            
    print(resp[str(rPr[0])][int(rpr[1])][str(rpr[2])])           
    return resp
def getMenuLs(na,ls,defa):
        return [sg.Push(),sg.T(na+':'),  sg.Combo(ls, default_value=ls[0], readonly=True, k=na,size=(30,4), background_color=sg.theme_button_color_background())]

def getSpecInfo(ls):
    info = getAllInfo('info')
    if fun.isLs(ls):
        return info[ls[0]][ls[1]]
    return info[ls]
def getAllInfo(sect):
        infos = {"map": {"category": "", "specialization": ""}, "categories": {"completions": ["chat", "translate", "qanda", "parse"], "coding": ["editcode", "debugcode", "convertcode", "writecode"], "embeddings": ["text_search_doc", "similarityIt", "text_similarityIt", "text_search_queryIt", "text_embeddingIt", "text_insertIt", "text_editIt", "search_documentIt", "s", "instructIt", "code_editIt", "code_search_codeIt", "code_search_textIt"], "moderation": ["moderate"], "images": ["image_create", "image_edit", "image_variation"]}, "parameters": {"all": ["all", "model", "prompt", "suffix", "max_tokens", "temperature", "top_p", "n", "stream", "logprobs", "echo", "stop", "presence_penalty", "frequency_penalty", "best_of", "logit_bias", "user", "input", "instruction", "size", "response_format", "image", "mask", "file", "purpose", "file_id", "training_file", "validation_file", "n_epochs", "batch_size", "learning_rate_multiplier", "prompt_loss_weight", "compute_classification_metrics", "classification_n_classes", "classification_positive_class", "classification_betas", "fine_tune_id", "engine_id"], "model": {"object": "str", "default": "text-davinci-003", "scale": "array", "array": ["completions", "edit", "code", "embedding"], "description": "The ID of the model to use for this request"}, "max_tokens": {"object": "int", "scale": "range", "range": {"0": 2048}, "default": 2000, "description": "The maximum number of tokens to generate in the completions.The token count of your prompt plus max_tokens cannot exceed the model context length. Most model have a context length of 2048 tokens (except for the newest model, which support 4096)."}, "logit_bias": {"object": "map", "scale": "range", "range": {"-100": 100}, "default": "None", "description": "Modify the likelihood of specified tokens appearing in the completions.Accepts a json object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from : 100 to 100. You can use this tokenizer tool (which works for both GPT: 2 and GPT: 3) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between : 1 and 1 should decrease or increase likelihood of selection; values like : 100 or 100 should result in a ban or exclusive selection of the relevant token.As an example, you can pass {50256:100} to prevent the &lt;|endoftext|&gt; token from being generated."}, "size": {"object": "str", "default": "1024x1024", "scale": "choice", "choice": ["256x256", "512x512", "1024x1024"], "description": "The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024."}, "temperature": {"object": "float", "default": 0.7, "scale": "range", "range": {"-2.0": 2.0}, "description": "What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well: defined answer.We generally recommend altering this or top_p but not both."}, "best_of": {"object": "int", "default": 1, "scale": "range", "range": {"0": 10}, "description": "Generates best_of completions server: side and returns the best (the one with the highest log probability per token). Results cannot be streamed.When used with n, best_of controls the number of candidate completions and n specifies how many to return \u2013 best_of must be greater than n.Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max_tokens and stop."}, "top_p": {"object": "float", "default": 0.0, "scale": "range", "range": {"0.0": 1.0}, "description": "An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.We generally recommend altering this or temperature but not both."}, "frequency_penalty": {"object": "float", "default": 0.0, "scale": "range", "range": {"-2.0": 2.0}, "description": "Number between : 2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model likelihood to repeat the same line verbatim.See more information about frequency and presence penalties."}, "presence_penalty": {"object": "float", "default": 0.0, "scale": "range", "range": {"-2.0": 2.0}, "description": "Number between : 2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model likelihood to talk about new topics.See more information about frequency and presence penalties."}, "log_probs": {"object": "int", "default": 1, "scale": "range", "range": {"1": 10}, "description": "Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens. For example, if logprobs is 5, the API will return a list of the 5 most likely tokens. The API will always return the logprob of the sampled token, so there may be up to logprobs+1 elements in the response.The maximum value for logprobs is 5. If you need more than this, please contact us through our Help center and describe your use case."}, "stop": {"object": "str", "default": "", "scale": "array", "range": {"0": 4}, "description": "Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence."}, "echo": {"object": "bool", "default": "False", "scale": "choice", "choice": ["True", "False"], "description": "Echo back the prompt in addition to the completions"}, "n": {"object": "int", "default": 1, "scale": "range", "range": {"1": 10}, "description": "How many completions to generate for each prompt.Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max_tokens and stop."}, "stream": {"object": "bool", "default": "False", "scale": "choice", "choice": ["True", "False"], "description": "Whether to stream back partial progress. If set, tokens will be sent as data: only server: sent events as they become available, with the stream terminated by a data: [DONE] message."}, "suffix": {"object": "str", "default": "", "scale": "range", "range": {"0": 1}, "description": "The suffix that comes after a completions of inserted text."}, "prompt": {"object": "str", "default": "None", "scale": "inherit", "description": "The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.Note that &lt;|endoftext|&gt; is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document."}, "input": {"object": "str", "default": "None", "scale": "inherit", "description": "The input text to use as a starting point for the edit."}, "instruction": {"object": "str", "default": "None", "scale": "inherit", "description": "The instruction that tells the model how to edit the prompt."}, "response_format": {"object": "str", "default": "url", "scale": "choice", "choice": ["url", "b64_json"], "description": "The format in which the generated images are returned. Must be one of url or ."}, "image": {"object": "str", "default": "None", "scale": "upload", "upload": {"type": ["PNG", "png"], "size": {"scale": {"0": 4}, "allocation": "MB"}}, "description": "The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask."}, "mask": {"object": "str", "default": "None", "scale": "upload", "upload": {"type": ["PNG", "png"], "size": {"scale": {"0": 4}, "allocation": "MB"}}, "description": "An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where image should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as image."}, "file": {"object": "str", "default": "None", "scale": "upload", "upload": {"type": ["jsonl"], "size": {"scale": {"0": 100}}, "allocation": "MB"}, "description": "Name of the JSON Lines file to be uploaded.If the purpose is set to finetune, each line is a JSON record with prompt and completions fields representing your training examples."}, "purpose": {"object": "str", "default": "None", "scale": "inherit", "description": "The intended purpose of the uploaded documents.Use finetune for Finetuning. This allows us to validate the format of the uploaded file."}, "file_id": {"object": "str", "default": "None", "scale": "inherit", "description": "The ID of the file to use for this request"}, "user": {"object": "str", "default": "defaultUser", "scale": "inherit", "description": "A unique identifier representing your end: user, which can help OpenAI to monitor and detect abuse. Learn more."}}, "descriptions": {"completions": "input what youd like to say to the bot, Have a chat with ChatGPT", "Edits": "This endpoint allows users to edit a given text prompt. It uses a generative model to suggest edits to the given prompt.", "Images": "This endpoint allows users to generate images from a given text prompt. It uses a generative model to generate an image that is similar to the given prompt.", "Embeddings": "This endpoint allows users to generate embeddings from a given text prompt. It uses a generative model to generate an embedding that is similar to the given prompt.", "Files": "This endpoint allows users to upload and store files. It provides a secure way to store files in the cloud.", "Fine-Tunes": "This endpoint allows users to fine-tune a given model. It uses a generative model to fine-tune the given model to better fit the user\u2019s needs.", "Moderations": "This endpoint allows users to moderate content. It uses a generative model to detect and remove inappropriate content.", "choices": "choose from the selection", "types": "choose from the selection", "coding": "write some code", "public": "Toggle public access", "private": "Toggle private access", "help": "will display all descriptions", "temp": "pick the randomness of your interaction", "shouldBeAllGood": "below-----------^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", "stillInTesting": "below-----------VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV", "similarity": "where results are ranked by relevance to a query string", "text_similarity": "Captures semantic similarity between pieces of text.", "text_search_query": "Semantic information retrieval over documents.", "text_embedding": "Get a vector representation of a given input that can be easily consumed by machine learning model", "text_insert": "insert text", "text_edit": "edit text", "search_document": "where results are ranked by relevance to a document", "search_query": "search query ", "code_edit": "specify the revisions that you are looking to make in the code", "code_search_code": "Find relevant code with a query in natural language.", "code_search_text": "text search in code", "image_edit": "[image]-main image; [mask] secondary image;[prompt]- input how you would like to have it edited", "params": "lists definitions and information about all parameters", "uploadfile": "upload a file to be used in future queries"}, "endpoints": {"engines": {"list": {"endpoint": "https://api.openai.com/v1/engines", "type": "GET"}, "retrieve": {"endpoint": "https://api.openai.com/v1/engines/{engine_id}", "type": "GET", "var": "{engine_id}"}}, "models": {"list": {"endpoint": "https://api.openai.com/v1/models", "type": "GET"}, "retrieve": {"endpoint": "https://api.openai.com/v1/models/{model}", "type": "GET", "var": "{model}"}}, "fine-tunes": {"create": {"endpoint": "https://api.openai.com/v1/fine-tunes", "type": "POST"}, "list": {"endpoint": "https://api.openai.com/v1/fine-tunes/{fine_tune_id}/events", "type": "GET", "var": "{fine_tune_id}"}, "retrieve": {"endpoint": "https://api.openai.com/v1/fine-tunes/{fine_tune_id}", "type": "GET", "var": "{fine_tune_id}"}, "cancel": {"endpoint": "https://api.openai.com/v1/fine-tunes/{fine_tune_id}/cancel", "type": "POST", "var": "{fine_tune_id}"}, "delete": {"endpoint": "https://api.openai.com/v1/models/{model}", "type": "DELETE", "var": "{model}"}}, "files": {"list": {"endpoint": "https://api.openai.com/v1/files", "type": "GET"}, "upload": {"endpoint": "https://api.openai.com/v1/files", "type": "POST"}, "delete": {"endpoint": "https://api.openai.com/v1/files/{file_id}", "type": "DELETE", "var": "{file_id}"}, "retrieveFile": {"endpoint": "https://api.openai.com/v1/files/{file_id}", "type": "GET", "var": "{file_id}"}, "retrieveContent": {"endpoint": "https://api.openai.com/v1/files/{file_id}/content", "type": "GET", "var": "{file_id}"}}, "completions": {"create": {"endpoint": "https://api.openai.com/v1/completions", "type": "POST"}}, "moderation": {"moderation": {"endpoint": "https://api.openai.com/v1/moderations", "type": "POST"}}, "edit": {"create": {"endpoint": "https://api.openai.com/v1/edits", "type": "POST"}}, "embeddings": {"create": {"endpoint": "https://api.openai.com/v1/embeddings", "type": "POST"}}, "image": {"create": {"endpoint": "https://api.openai.com/v1/images/generations", "type": "POST"}, "edit": {"endpoint": "https://api.openai.com/v1/images/edits", "type": "POST"}, "variation": {"endpoint": "https://api.openai.com/v1/images/variations", "type": "POST"}}}, "info": {"completions": {"endpoints": {"chat": "https://api.openai.com/v1/completions", "translate": "https://api.openai.com/v1/completions", "qanda": "https://api.openai.com/v1/completions", "parse": "https://api.openai.com/v1/completions", "response": ["choices", "n", "text"]}, "choices": {"model": {"default": "text-davinci-003", "list": ["text-ada-001", "text-davinci-003", "text-curie-001", "text-babbage-001"]}}, "specifications": {"chat": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "chat", "structure": "", "vars": {"prompt": {"input": "what would you like to say to the bot?", "type": "str","ogVar":"prompt", "delimiter": ""}}}}}, "translate": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "task: translate text", "structure": "languages to translate to:[languages];translate the following text:[text]", "vars": {"languages": {"input": "specify the target languages", "type": "list","ogVar":"prompt", "delimiter": "languages to translate to:\n"}, "text": {"input": "input the text you would like to have translated", "type": "text","ogVar":"prompt", "delimiter": "translate the following text:\n"}}}}}, "qanda": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "task: question and answer", "structure": "[question]- input a question,question mark will auto add, [answer] - proposed answer to a question", "vars": {"question": {"input": "pose a question to have answered", "type": "str", "delimiter": "Q:"}, "answer": {"input": "pose answer to a proposed question", "type": "str","ogVar":"prompt", "delimiter": "A:"}}}}}, "parse": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "task: parse text,", "structure": " a [summary] of the [data] will be given in order to parse specific [subjects]:", "vars": {"summary": {"input": "summarize the text you would like to parse", "type": "text","ogVar":"prompt", "delimiter": "summary of data:\n"}, "subjects": {"input": "specific subjects you want to have parsed", "type": "list","ogVar":"prompt", "delimiter": "subjects:\n"}, "data": {"input": "text you would like to have parsed", "type": "text","ogVar":"prompt", "delimiter": "data to parse:\n"}}}}}}}, "coding": {"endpoints": {"editcode": "https://api.openai.com/v1/completions", "debugcode": "https://api.openai.com/v1/completions", "convertcode": "https://api.openai.com/v1/completions", "writecode": "https://api.openai.com/v1/completions", "response": ["choices", "n", "text"]}, "choices": {"language": {"default": "python", "list": ["Python", "Java", "C++", "JavaScript", "Go", "Julia", "R", "MATLAB", "Swift", "Prolog", "Lisp", "Haskell", "Erlang", "Scala", "Clojure", "F#", "OCaml", "Kotlin", "Dart"]}, "model": {"default": "code-davinci-002", "list": ["code-cushman-001", "text-davinci-003", "code-davinci-002"]}}, "specifications": {"writecode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "write code in [language] based off of specific [instruction]:", "structure": "[prompt]-describe the code; [language] - specify the target language", "vars": {"instruction": {"input": "describe what you are looking for, be specific", "type": "str","ogVar":"prompt", "delimiter": "instructuions:\n"}, "language": {"input": "which language would you like the code to be written in?", "type": "choice","ogVar":"prompt", "delimiter": "language:\n,"}}}}}, "editcode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "edit code", "structure": "edit [code] based off of specific [instructions]", "vars": {"instruction": {"input": "provide specific instructions on what you are looking to have edited about this code:", "type": "str","ogVar":"prompt", "delimiter": "instructions:\n"}, "code": {"input": "enter the code you would like to have edited:", "type": "str","ogVar":"prompt", "delimiter": "code:\n"}}}}}, "debugcode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "debug the code:", "structure": "debug the following code:\n", "vars": {"code": {"input": "the code you would like to have debugged", "type": "str","ogVar":"prompt", "delimiter": ""}}}}}, "convertcode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "convert code to another language:", "structure": "convert the following [code] to [language]", "vars": {"language": {"input": "the language you would like the code converted to:", "type": "str","ogVar":"prompt", "delimiter": "language:\n"}, "code": {"input": "the code you would like to have converted", "type": "str","ogVar":"prompt", "delimiter": "code:\n"}}}}}}}, "images": {"endpoints": {"image_create": "https://api.openai.com/v1/images/generations", "image_variation": "https://api.openai.com/v1/images/variations", "image_edit": "https://api.openai.com/v1/images/edits", "response": ["data", "n", "response_format"]}, "choices": {"response_format": {"default": "url", "list": ["url", "b64_json"]}, "size": {"default": "1024x1024", "list": ["256x256", "512x512", "1024x1024"]}}, "specifications": {"image_variation": {"type": "images", "refference": ["image", "create", "image_variation"], "parameters": {"required": ["image"], "optional": ["prompt", "size", "n", "response_format", "user", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "image variation", "structure": "create a variation of the [image] based off of [instructions] if given:\n", "vars": {"instructions": {"input": "describe what you would like to have done with the image(s):", "type": "str","ogVar":"prompt", "delimiter": "instructions:\n"}}}}}, "image_create": {"type": "images", "refference": ["image", "create", "image_create"], "parameters": {"required": ["prompt"], "optional": ["size", "n", "response_format", "user", "suffix", "logit_bias"], "prompt": {"task": "image creation", "structure": "create an image based on the following [instructions]:\n", "vars": {"instructions": {"input": "describe the image you would like to create:", "type": "str","ogVar":"prompt", "delimiter": "instructions:"}}}}}, "image_edit": {"type": "images", "refference": ["image", "create", "image_edit"], "parameters": {"required": ["image", "prompt"], "optional": ["mask", "size", "n", "response_format", "user", "suffix", "max_tokens", "logit_bias"], "prompt": {"task": "image creation", "structure": "[image]-main image; [mask] secondary image;[prompt]- input how you would like to have it edited", "vars": {"instructions": {"input": "provide instructions describing what you would like to have done with the image(s):", "type": "str","ogVar":"prompt", "delimiter": "instructions:"}}}}}}}, "edit": {"endpoints": {"edit": "https://api.openai.com/v1/embeddings", "response": ["data", "n", "embedding"]}, "choices": {"model": {"default": "text-ada-001", "list": ["text-ada-001", "text-davinci-003", "text-curie-001", "text-babbage-001"]}}, "specifications": {"edits": {"type": "edits", "refference": ["edits", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop"], "prompt": {"task": "edit text", "structure": "[image]-main image; [mask] secondary image;[prompt]- input how you would like to have it edited", "vars": {"instructions": {"input": "provide instructions describing what you would like to have edited:", "type": "str","ogVar":"prompt", "delimiter": "instructions:"}}}}}}}, "moderation": {"endpoints": {"moderate": "https://api.openai.com/v1/moderations", "response": ["results", "n", "text"]}, "choices": {"model": {"default": "None", "list": ["text-moderation-004", "davinci"]}}, "specifications": {"moderate": {"type": "moderation", "refference": ["completions", "moderation"], "parameters": {"required": ["input"], "optional": ["model"], "prompt": {"task": "moderation", "structure": "text to moderate:\n", "vars": {"input": {"input": "provide the text you would like to have moderated", "type": "text","ogVar":"prompt", "delimiter": "moderate the following"}}}}}}}}, "prevKeys": [], "jsList": [], "content": "application/json"}
        return infos[sect]
def getSpecification():
    return getAllInfo(category)['specifications'][specialization]
def getRefference():
    return getAllInfo('info')[category]['specifications'][specialization]['refference']
def returnParameters(category,specialization):
    return getAllInfo('info')[category]['specifications'][specialization]['parameters'] 
def tallyRespSink():
    return ifN(getAllInfo(category)['endpoints'][specialization]['response'],json.loads(js))
def getChoices():
    return getAllInfo('info')[category]['choices']
def getEndPoint():
    return getAllInfo('info')[category]['endpoints'][specialization]
def reqDelete():
  return requests.delete(ls[0], json=ls[1], headers=GETHeader())
def retrieveModel(model):
  return reqGet([model,None])
def getModels():
  pen(callJson(None,endpoints['models']['list']),'modelsList.json')
def getEngines():
  pen(callJson(None,endpoints['engines']['list']),'enginesList.json')
def getFiles():
  pen(callJson(None,endpoints['files']['list']),'filesList.json')
def mkType(ls):
    x,obj = ls
    if specializedSet['paramJs']['scale'] == 'upload':
        if ky in ['image','mask']:
            return str(x)#generate_from_masked_image(js[ky])
        return open(js[ky], "rb")
    if obj == 'float':
        return float(str(x).replace("'",'').replace("'",''))
    if obj == 'int':
        return int(str(x).split('.')[0].replace("'",'').replace("'",''))
    if obj == 'bool':
        return bool(x)
    else:
        return str(fun.eatAll(str(x),['"',"'"]))
def ifNotIntFl(js,ky):
    specializedSet['paramJs'] =getAllInfo('parameters')[ky]
    return mkType([fun.eatAll(str(js[ky]),['"',"'"]),getObj(ky)])
def simpleWindow(window):
    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == 'OK':
            return values
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
            window.close()
    return event,values

def grisk(sg1):
    grisk_theme = {'BACKGROUND': '#353535',
             'TEXT': '#ffffff',
             'INPUT': '#191919',
             'TEXT_INPUT': '#ffffff',
             'SCROLL': '#505F69',
             'BUTTON': ('#ffffff', '#454545'),
             'PROGRESS': ('#505F69', '#32414B'),
             'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,}
    sg.theme_add_new('grisk', grisk_theme)
    sg.theme('grisk')
    top_button_size = 16
    bottom_text_size = 20
    layout = [[sg.Push(), sg.T('Stable Diffusion GRisk GUI 0.1', font='_ 15 bold'), sg.Push()],sg1,[sg.Multiline(size=(60,6), k='-MLINE TEXT INPUTS-')]]
    bottom_layout = [[sg.B('Render', expand_x=True)],[sg.OK('OK'),sg.Button('Info'),sg.Button('Run'),sg.Button('Auto'),sg.Button('Exit')]]
    layout += bottom_layout
    window = sg.Window('Grisk-a-like', layout,)
    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == 'OK':
            return values
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
            window.close()
def ifNotLs(ls):
    
    for i in range(0,len(ls)):
        bef == False
        if isLs(ls[i]) == False:
            lsN.append(ls[i])
            bef = True
        else:
           if len(lsA) != 0:
               lsA = []
def mkDefCats():
    lsN = []
    cats=fun.getKeys(getAllInfo('categories'))
    for i in range(0,len(cats)):
        lsN.append(button(cats[i],'category_'+cats[i],True))
    return lsN
def getLongestLen(ls):
    highest = [len(str(ls[0])),0]
    for i in range(0,len(ls)):
        if len(str(ls[i]))>highest[0]:
            highest = [len(str(ls[i])),i]
    return highest[0]
def mkListInp(na,k,w,w2):
    pad = [4,4]
    lsN = [],pad[0],pad[1]
    col = w/w2
    for i in range(0,k):
        for i in range(0,len(row)):
            lsC = []
            for k in range(0,len(col)):
                lsC.apput(size=(), pad=(4,4),key = 'name')
  
def mkDefspecs(ls):
    keys=fun.getKeys(getAllInfo('categories'))
    return 
def callopenAi():
    global category,specialization,specializedSet
    specializedSet = {'jsList':[],'prevKeys':[],'userMgs':'','resp':'','content':'application/json'}
    category,specialization = getStart()    
    js =getDrops(getParamDrop(category,specialization))                
def txtBox(na):
    return sg.Text(na, font='Any 10')
def slider(na,defa,ls,event):
    return 
def checkBox(na,ky,event,defa,state):
    return sg.Checkbox(na, enable_events=event, key=ky,default=defa,disabled=False, size=(1, 0),pad=(0,0))
def checkBoxStnd(ky,event,defa,state):
    return sg.Checkbox('',key=ky,enable_events=event,default=defa,disabled=False,size=(1, 0))
def getList(na,count):
    return [[sg.Input(ifLang(row,na),size=(15,5), pad=(4,4),key = na) for col in range(1)] for row in range(count)]
def txtInputDis(txt,na,w,l):
    if len(txt)/int(w) <l:
        l = len(txt)/int(w)
    return [sg.Multiline(txt, size=(w,l),font='Tahoma 13', key=na, autoscroll=True,disabled=True),sg.VerticalSeparator(pad=None)]
def txtInput(na,w,h):
    return [sg.Multiline(size=(w,h), font='Tahoma 13', key=na, autoscroll=True),sg.VerticalSeparator(pad=None)]
def getFileBrowse(na,typ,ext,loc,txt):
    return [[txt],sg.Input(change_submits=True,key=na),sg.FileBrowse(file_types=((typ, "*."+str(ext)),),key=na)]
def button(na,ky,event):
    return sg.Button(na, border_width=4,enable_events=event, key=ky,tooltip="get info")
def getRange(ls,na):
    return (fun.getObjObj(getObj(na),ls[0]),fun.getObjObj(getObj(na),ls[1]))
def getTop(sg1):
    return sg.Frame('', sg1, size=(920, 100), pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)
def scriptOutput():
    return sg.Output(size=(100, 20), font='Courier 10')
def getbaseNum(na):
     return fun.getObjObj(getObj(na),fun.getObjObj(getObj(na),'0.990')*100+1)
def getRes(na):
    return fun.getObjObj(getObj(na),fun.getObjObj(getObj(na),1)/getbaseNum(na))
def getObjAll(na,k):
    return fun.getObjObj(getObj(na),k)
def getFullSlider(na,defa,ls,event,opt):
    
    return [checkBoxStnd(na+'default_'+str(defa),True,True,opt),checkBoxStnd(na+'disable',True,True,opt),button(na,na+'_info',True),guiFun.getSlider({"title":na,"range":getRange(ls,na),"visible":True,"key":None,"default_value":defa,"resolution":res,"tick_interval":getbaseNum(na),"pad":(0,0),"orientation":'h',"disable_number_display":True,"enable_events":False,"size":(25,15)})]
def getFullParams(na,defa,event,opt):
    return [checkBoxStnd(na+'default_'+str(defa),True,True,opt),checkBoxStnd(na+'disable',True,True,opt),button(na,na+'_info',True)]
def getdropDown(na,ls,defa):
    return sg.Combo(ls,key=na,size=(getLongestLen(ls),len(ls)),default_value=defa)
def getDownMenu(na,ls,defa,event,opt):
    return [getFullParams(na,defa,event,opt),getdropDown(na,ls,defa)]
def mkFull(na,defa,ls,opt,event,typ):
    lsN = getFullParams(na,defa,True,opt)
    if typ == 'slide':
        if getObj(na) == 'float':
            ls = guiFun.slider({"title":na,"range":getRange(ls,na),"visible":True,"key":na,"default_value":getObjAll(na,defa),"resolution":getRes(na),"tick_interval":getbaseNum(na),"pad":(0,0),"orientation":'h',"disable_number_display":False,"enable_events":True,"size":(25,15)})
        if getObj(na) == 'int':
            ls = guiFun.slider({"title":na,"range":ls,"visible":True,"key":na,"default_value":int(defa),"resolution":int(1),"tick_interval":int(1),"pad":(0,0),"orientation":'h',"disabled":False,"disable_number_display":False,"enable_events":True,"size":(25,15)})
    elif typ == 'drop':
        input(ls)
        ls = getdropDown(na,ls,defa)
    elif typ == 'input':
        ls = txtInput(na,ls[0],ls[1])
    elif typ == 'file':
        ls = getFileBrowse(na,ls[0],ls[1],ls[2],ls[3])
    elif typ == 'check':
        ls = checkBox(na,ls,event,defa,opt)
    ls = fun.mkLs(ls)
    for i in range(0,len(ls)):
        lsN.append(ls[i])
    return lsN
def mkFullDrop(na,defa,ls,opt,event):
    lsN = getFullParams(na,5,True,opt)
    lsN.append(slider(na,defa,ls,event))
    return lsN
def frameWorkForLayOut():
   return {'top_banner': {'frame': {'pad': (0,0), 'background_color': '#1B2838', 'expand_x': True, 'border_width': '0', 'grab': True}, 'column': {}}, 'top': {'frame': {'size': (920, 100), 'pad': ((20,20), (20, 10)), 'expand_x': True, 'relief': sg.RELIEF_GROOVE, 'border_width': '3'}, 'column': {}}, 'querySection': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True}, 'column': {}}, 'previousQuery': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True}, 'column': {}}, 'outputSection': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True}, 'column': {}}, 'chatInput': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True, 'element_justification': 'c'}, 'column': {}}}
def columnDefaults():
   return {'background_color': None, 'size': None, 's': None, 'size_subsample_width': '1', 'size_subsample_height': '2', 'pad': None, 'p': None, 'scrollable': False, 'vertical_scroll_only': False, 'right_click_menu': None, 'key': None, 'k': None, 'visible': True, 'justification': None, 'element_justification': None, 'vertical_alignment': None, 'grab': None, 'expand_x': None, 'expand_y': None, 'metadata': None, 'sbar_trough_color': None, 'sbar_background_color': None, 'sbar_arrow_color': None, 'sbar_width': None, 'sbar_arrow_width': None, 'sbar_frame_color': None, 'sbar_relief': None}
def frameDefaults():
   return {'title_color': None, 'background_color': None, 'title_location': None, 'relief': 'groove', 'size': None, 's': None, 'font': None, 'pad': None, 'p': None, 'border_width': None, 'key': None, 'k': None, 'tooltip': None, 'right_click_menu': None, 'expand_x': False, 'expand_y': False, 'grab': None, 'visible': True, 'element_justification': '"left"', 'vertical_alignment': None} 

def getSizeGroup(colr):
    return sg.Sizegrip(background_color=colr)
def getColumn(sg1,js):
    return sg.Column(sg1, background_color = js["background_color"],size = js["size"],s = js["s"],size_subsample_width = js["size_subsample_width"],size_subsample_height = js["size_subsample_height"],pad = js["pad"],p = js["p"],scrollable = js["scrollable"],vertical_scroll_only = js["vertical_scroll_only"],right_click_menu = js["right_click_menu"],key = js["key"],k = js["k"],visible = js["visible"],justification = js["justification"],element_justification = js["element_justification"],vertical_alignment = js["vertical_alignment"],grab = js["grab"],expand_x = js["expand_x"],expand_y = js["expand_y"],metadata = js["metadata"],sbar_trough_color = js["sbar_trough_color"],sbar_background_color = js["sbar_background_color"],sbar_arrow_color = js["sbar_arrow_color"],sbar_width = js["sbar_width"],sbar_arrow_width = js["sbar_arrow_width"],sbar_frame_color = js["sbar_frame_color"],sbar_relief = js["sbar_relief"])
def getFrame(sg1,js):
    frJs = frameDefaults()
    keys = fun.getKeys(frameDefaults())
    for k in range(0,len(keys)):
      if frJs[keys[k]] != None and fun.isBool(frJs[keys[k]]) == False:
        frJs[keys[k]] = frJs[keys[k]].replace('"','')
      if 'None' in str(frJs[keys[k]]):
        frJs[keys[k]] = None
      if keys[k] in js:
        if 'None' in str(js[keys[k]]) and keys[k] == 'size':
          js[keys[k]] =(None, None) 
        frJs[keys[k]] = js[keys[k]]
      if 'None' in str(frJs[keys[k]]) and keys[k] == 'size':
          frJs[keys[k]] =(0, 0) 
   
    
    js = frJs

    fr = sg.Frame('',sg1,title_color = js["title_color"],background_color = js["background_color"],title_location = js["title_location"],relief = js["relief"],size = js["size"],s = js["s"],font = js["font"],pad = js["pad"],p = js["p"],border_width = js["border_width"],key = js["key"],k = js["k"],tooltip = js["tooltip"],right_click_menu = js["right_click_menu"],expand_x = js["expand_x"],expand_y = js["expand_y"],grab = js["grab"],visible = js["visible"],element_justification = js["element_justification"],vertical_alignment = js["vertical_alignment"])

    return fr
def getFrameNow(sg1,name):
    js = {'top_banner':{'pad': (0,0), 'background_color': '#1B2838', 'expand_x': True, 'border_width': 0, 'grab': True},'top':{'size': (920, 100), 'pad': ((20,20), (20, 10)), 'expand_x': True, 'relief': sg.RELIEF_GROOVE, 'border_width': 3},'previousQuery':{'pad': (0, (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True},'querySection':{'pad': (0, (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True},'chatInput':{'pad': (0, (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True},'outputSection':{'pad': (0, (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True},'parameterSection':{'pad': ((10,20), (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True}}
    js = js[name]
    keys = fun.getKeys(frameDefaults())
    for k in range(0,len(keys)):
      if keys[k] not in js:
        js[keys[k]] = frameDefaults()[keys[k]]

        
    return sg.Frame('', sg1, pad=js['pad'], border_width=js['border_width'], expand_x=js['expand_x'], expand_y=js['expand_y'], grab=js['grab'], element_justification=js['element_justification'])#[sg.Frame('', sg1,  background_color = js["background_color"],size = js["size"],s = js["s"],size_subsample_width = js["size_subsample_width"],size_subsample_height = js["size_subsample_height"],pad = js["pad"],p = js["p"],scrollable = js["scrollable"],vertical_scroll_only = js["vertical_scroll_only"],right_click_menu = js["right_click_menu"],key = js["key"],k = js["k"],visible = js["visible"],justification = js["justification"],element_justification = js["element_justification"],vertical_alignment = js["vertical_alignment"],grab = js["grab"],expand_x = js["expand_x"],expand_y = js["expand_y"],metadata = js["metadata"],sbar_trough_color = js["sbar_trough_color"],sbar_background_color = js["sbar_background_color"],sbar_arrow_color = js["sbar_arrow_color"],sbar_width = js["sbar_width"],sbar_arrow_width = js["sbar_arrow_width"],sbar_frame_color = js["sbar_frame_color"],sbar_relief = js["sbar_relief"])]

def mkBanner(sg1,js):
    frames(sg1,pad,bgkrndColor,borderWidth,expand,js,eleJust)
def mkTop(sg1):
    return sg.Frame('', sg1, size=(920, 100), pad=BPAD_TOP,  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)
def frames(sg1,js):
    return sg.Frame('', sg1, pad=js['pad'], border_width=js['border_width'], expand_x=js['expand_x'], expand_y=js['expand_y'], element_justification=js['element_justification'])
def createMidToLast(sg1,bgkrndColor):
    return
def mkJss():
  st = '''
  sg.Column(parameterSection, pad=BPAD_RIGHT,  expand_x=True, expand_y=True, grab=True)
  [sg.Frame('', top_banner,  pad=(0,0), background_color='#1B2838',  expand_x=True, border_width=0, grab=True)],
  
  'chatInput':{'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True, 'element_justification'=c}
  [sg.Frame('', top, size=(920, 100), pad=BPAD_TOP,  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)],
  [sg.Frame('', querySection, pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, )],

  [sg.Frame('', outputSection, pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, )],
  [sg.Frame('', outputSection, pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, )],
  [sg.Frame('', chatInput,  pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, element_justification='c')],
    
  )'''
  st = st.split('\n')
  js,n = {},''
  dicJs = {'BACKGROUND': '#2B475D','TEXT': '#FFFFFF','INPUT': '#F2EFE8','TEXT_INPUT': '#000000','SCROLL': '#F2EFE8','BUTTON': ('#000000', '#C2D4D8'),'PROGRESS': ('#FFFFFF', '#C7D5E0'),'BORDER': 0,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,'BPAD_BANNER':(0,0),'BORDER_COLOR':'#C7D5E0','DARK_HEADER_COLOR':'#1B2838','BPAD_TOP':((20,20), (20, 10)),'BPAD_LEFT':((20,10), (0, 0)),'BPAD_LEFT_INSIDE':(0, (10, 0)),'BPAD_RIGHT':((10,20), (10, 0)),'expand_x':True,'expand_y':True,'relief':sg.RELIEF_GROOVE,'border_width':0,'right_click_menu':sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT,'resizable':True,'no_titlebar':True}
  frameWork = frameWorkForLayOut()
  jsCol = columnDefaults()
  jsFram = frameDefaults()
  names = fun.getKeys(frameWorkForLayOut())
  dicsKeys = fun.getKeys(dicJs)
  cFrame = ['column','frame']
  for k in range(0,len(names)):
    currKeys,colKeys,frameKeys,jsFramKeys  = fun.getKeys(frameWork[names[k]]),fun.getKeys(jsCol),fun.getKeys(frameWork[names[k]]),fun.getKeys(jsFram)
    for i in range(0,len(frameKeys)):
      cKeys = fun.getKeys(frameWork[names[k]][frameKeys[i]])
      for c in range(0,len(cKeys)):
        currVar = frameWork[names[k]][frameKeys[i]][cKeys[c]]
        if currVar in dicsKeys:
          frameWork[names[k]][frameKeys[i]][cKeys[c]] = dicJs[currVar]
        if currVar == 'sg.RELIEF_GROOVE':
          frameWork[names[k]][frameKeys[i]][cKeys[c]] = sg.RELIEF_GROOVE
      for c in range(0,len(colKeys)):
        if colKeys[c] not in frameWork[names[k]][frameKeys[i]]:
          if cFrame == 'frame':
            frameWork[names[k]][frameKeys[i]][colKeys[c]] = jsFram[jsFramKeys]
          else:
            frameWork[names[k]][frameKeys[i]][colKeys[c]] = jsCol[colKeys[c]]
      if fun.isNum(frameWork[names[k]][frameKeys[i]][colKeys[c]]):
        frameWork[names[k]][frameKeys[i]][colKeys[c]] = int(frameWork[names[k]][frameKeys[i]][colKeys[c]])
          
    print(frameWork[names[k]][frameKeys[i]]['background_color'])
    
  return frameWork
def maybe():
  for i in range(1,len(st)-1):
    if ',' in st[i]:
      na = st[i].split(',')[1].replace(' ','')
      sects = st[i].split(', ')
      js[na] = {'frame':{},'column':{}}
      js = {}
      for k in range(0,len(lsSt)):
       js[na] = {'frame':jsN,'column':jsN}
  return js
mkJss()
def getObj(x):
    return getAllInfo('parameters')[x]['object']

def getStart():
    cats,keyLs = []
    specializations
    #keyLs.append(getDrop({'category':fun.getKeys(cats)}))
    #keyLs.append(getDrop({'specialization':cats[keyLs[-1]]}))
    specializations,specialization
    
    return    
def getDrops(js):
    #specializedSet['userMgs']=json.loads(js)
    #specializedSet['resp']=reqPost(js)
    #if js != 'exit':
    #    getResponse()
    return js
def getDrop(js):
  keys,lsA = getKeys(js),[]
  if fun.isLs(keys[0]):
      changeGlob('varDesc',st[0])
      st= st[1]
  for i in range(0,len(keys)):
    key = keys[i]
    lsA.append(getMenuLs(key,js[key],js[key][0]))
  return desktopTheme(lsA)[key]
def eventCall(window):
  event,values = window.read()
  if 'defVals' =={}:
      values['defVals'] = values
  values['currVals'] = values
  curr = values['currVals']
  if event == sg.WIN_CLOSED or event == 'Exit':
    window.close()
    return 'exit'
  elif '_Info' in str(event):
      from dataSheets import parameters
      popUp(event[:-len('_Info')],parameters[event[:-len('_Info')]]['description'])
  elif '_ch' in str(event):
      if values[event] == True:
          updateValues(window,event[:-len('_ev')],values['defVals'][:-len('_ev')])
  elif event in ['best_of','n']:
      if 'best_of' in fun.getKeys(values):
          if curr['n']>=curr['best_of']:
                  updateValues(window,'n',values['best_of']-1)
  elif event == 'override':
      window.close()
      return values
  elif event == '_Info':
      if varDesc != None:
          from dataSheets import dataSheets
          popUp('variable descriptions',createListFromJs(defVals,getKeys(values),'description'))
  elif event == 'OK':
    if checkValues(values):
      window.close()
      return values
  elif event == 'Run':
    if checkValues(values):
        changeGlob('gogo',False)
        return values
  if 'defVals' not in values:
      values['defVals'] = {}    
  return False
def getParamNeeds(category,specialization):
    n = paramNeeds[category]
    if 'specialized' in fun.getKeys(n):
      n = n['specialized'][specialization]
    return n 
def tab(i):
   return [[sg.Text(specializedSet['inputTabKeys']['names'][i])], [


       sg.Multiline(size=(100,10), font='Tahoma 13', autoscroll=True,key=str(specializedSet['inputTabKeys']['names'][i])),sg.VerticalSeparator(pad=None)]]

#callopenAi()
def getDefMenu():
    return [sg.Menu([['File', ['Open', 'Save', 'Exit',]],['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],['Help', 'About...'],])]
def getDefButtons():
    return [sg.OK('OK'),sg.Button('Info'),sg.Button('Run'),sg.Button('Auto'),sg.Button('Exit')]
def getDefaultSetOptions():
    return sg.set_options(suppress_raise_key_errors=bool(False), suppress_error_popups=bool(False), suppress_key_guessing=bool(False))
def getDefaults():
    return [getDefMenu(),getDefButtons()]
def getDefaultLayout(sg1):
    lsA = getDefaults()
    lsA.append(sg1)
    return lsA

def defaultWindow2(sg1,title):
    gogo = True
    getDefaultSetOptions()
    layout = [[getDefaultLayout(sg1)]]
    window = sg.Window(title,layout , finalize=False)
    while gogo == True:
      vals = eventCall(window)
      if vals != False:
        return vals
def createLayout(ls,name):
    lsA =[]
    for i in range(0,len(ls)):
      lsA.append()
    
    return lsA
def searchVals(x,k,values):
    keys = getKeys(values)[1:]
    for i in range(0,len(keys)):
      
        if fun.isNum(keys) == False:
            if x in keys[i]:
                return keys[i].split(x)[k] 
    return None
def getAllThings():
    js ={'category':getInfoSec(category,info),
         'specifications':getInfoSec('specifications',info[category]),
         'specialization':getInfoSec(specialization,info[category]['specifications']),
         'parameters':getInfoSec('parameters',info[category]['specifications'][specialization])
         }
    js['prompt'] = getInfoSec('prompt',js['parameters']['parse'])
    js['structure'] = getInfoSec('structure',js['prompt']['parse'])
    js['categoryDefinition']=ifInRet2(category,descriptions)[1]
    js['specializationDeffinition']=ifInRet2(specialization,descriptions)[1]
    
    return js
def txtBox(na,key,font,background_color,enable_events,grab):
    return sg.Text(na,key=key,font=font,background_color=background_color,enable_events=enable_events, grab=grab)
def pushBox(background_color):
    return sg.Push(background_color=background_color)
def getT(na,key):
    return sg.T(na,key=key)
def queryDropDown(ls,key,defa):
    return sg.Combo(ls,key=key,size=(getLongestLen(ls),1),default_value=defa)
def getButton(name,key,enable_events, button_color,bind_return_key):
    return sg.Button(name,key=key,enable_events=enable_events, button_color=button_color,bind_return_key=bind_return_key)
def txtInputs(na,key,size,font,autoscroll,disable,pad):
    return sg.Multiline(na, size=size,font=font, key=key, autoscroll=autoscroll,disabled=disable),sg.VerticalSeparator(pad=pad)
def getTab(na,layout,key,visible,disable,title_color):
    return sg.Tab(na, layout,key=key,visible=visible,disabled=disable,title_color=title_color)
def getTabGroup(tabs,key):
    return sg.TabGroup(tabs,key=key)
{'top_banner': {'frame': {'pad': (0,0), 'background_color': '#1B2838', 'expand_x': True, 'border_width': '0', 'grab': True}, 'column': {}},
 'top': {'frame': {'size': (920, 100), 'pad': ((20,20), (20, 10)), 'expand_x': True, 'relief': sg.RELIEF_GROOVE, 'border_width': '3'}, 'column': {}},
 'querySection': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True}, 'column': {}},
 'previousQuery': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True}, 'column': {}},
 'outputSection': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True}, 'column': {}},
 'chatInput': {'frame': {'pad': (0, (10, 0)), 'border_width': '0', 'expand_x': True, 'expand_y': True, 'element_justification': 'c'}, 'column': {}}}
def getBanner():
    txt0 = txtBox('Chat GPT-3 Console',None,'Any 20',templateJs['DARK_HEADER_COLOR'],True,False)
    push = pushBox(templateJs['DARK_HEADER_COLOR'])
    txt1 = txtBox(getDate(),None,'Any 20',templateJs['DARK_HEADER_COLOR'],False,False)
    struct = [[txt0,push,txt1]]
    return getFrameNow(struct,'top_banner')
def getTop():
    txtPush = pushBox(None), txtBox('category','categoryDisplay','Any 20',None,False,False),pushBox(None)
    T0 = getT('desctiption','categoryDescription')
    struct = [txtPush,[T0]]
    return getFrameNow(struct,'top')
def getquerySection():
    print('querysection')
    txt0 =txtBox('Specialization','specializationDisplay','Any 20',None,False,False)
    txt1 = txtBox('specialization description','specializationDescription',None,None,False,False)
    drop = queryDropDown(specializedLs,'catCombo',specialization)
    cats = mkDefCats()
    butt = getButton('Generate','Generate',True,templateJs['BUTT_COLOR_Y_B'],False)
    struct = [[txt0],[txt1],cats,[drop],[butt]]
    #frame = [sg.Frame('',struct,pad=(0,(10, 0)),border_width=0,expand_x=True,expand_y=True)]
    return getFrameNow(struct,'querySection')
def getPrevQuery():
    txt0 = sg.Text('previous query', font='Any 20')
    txtIn0 = txtInputDis('previous statememt','previous statememt',50,10)
    txtIn1 = txtInputDis('previous Answer','previousQuery',50,10)
    struct = [[sg.Text('Query Selection', font='Any 20')],mkDefCats(),[sg.Combo(specializedLs,key='catCombo',default_value=specializedLs[0]),sg.Button('Generate',key='Generate',enable_events=True, button_color=templateJs['BUTT_COLOR_Y_B'])]]
    #frame = [sg.Frame('',struct,pad=(0,(10, 0)),border_width=0,expand_x=True,expand_y=True)]
    return getFrameNow(struct,'previousQuery')
def getOutput():
    print('getOutput')
    txt0 = txtBox('Script output',None,'Any 20',None,True,False)
    outSect = txtBox('Script output',None,'Any 20',None,True,False)#sg.Output(size=(50, 10), font='Courier 10')
    struct = [[txt0],[outSect]]
    frame = [sg.Frame('',struct,pad=(0,(10, 0)),border_width=0,expand_x=True,expand_y=True)]
    return frame
def getInput():
    print('getInput')
    txt0 = txtBox('Chat Input',None,'Any 20',None,True,False)
    T0 = getT('structure','structure')
    js = getAllThings()
    varKeys = getKeys(js['prompt']['parse']['vars'])
    #group,tabIndex = checkTabCreate(None)
    #group = getTabGroup([group],'tabGroupInput')
    butt0 = getButton('Compile','Compile',True,templateJs['BUTT_COLOR_Y_B'],True)
    butt1 = getButton('SEND','SEND',True,templateJs['BUTT_COLOR_Y_B'],True)
    butt2 = getButton('EXIT','EXIT',True,templateJs['BUTT_COLOR_Y_G'],False)
    struct = [[txt0],[T0],[butt0,butt1,butt2]]
    frame = [sg.Frame('',struct,pad=(0,(10, 0)),border_width=0,expand_x=True,expand_y=True,element_justification='c')]
    return frame
def findStrInLs(ls,x):
    lsN = []
    for k in range(0,len(ls)):
        if str(x) == str(ls[k]):
            lsN.append(ls[k])
    return lsN
def findLsStrsInLs(ls,ls2):
    lsN = []
    for k in range(0,len(ls)):
        if ls[k] in ls2:
            lsN.append(ls[k])
    return lsN
def stripNumJS(js):
    jsN,jsA,keys = {},{},fun.getKeys(js)
    for i in range(0,len(keys)):
        key = keys[i]
        if fun.isNum(key)== False:
            jsN[js[key].split('_')[0]]={'num':key,'active':js[key]}
        else:
            jsA[key] = js[key]
    print(jsA,js)
    return jsA,jsN
def getCatFroSpec(spec):
    for k in range(0,len(getKeys(categories))):
        categoryLs = categories[getKeys(categories)[k]]
        if spec in categoryLs:
            return getKeys(categories)[k]
def getParaMect():
    changeGlob('parameterSection',[[sg.Text('Parameters', font='Any 20')],[txtBox('def  '),txtBox('dis  '),txtBox('   inf  ')],specializedSet['jsList']])
def completePrompt(event,values):
    js,paramJs,promptJs = getCurrentTab(event,values),{},{}
    parametersSpec,js['paramAll'] = info[js['category']]["specifications"][js['spec']]['parameters'],[]
    for k in range(0,2):
        params = parametersSpec[['required','optional'][k]]
        
        for i in range(0,len(params)):
            js['paramAll'].append(params[i])
            param = params[i]
            if param in values:
                paramJs[param]=mkType([values[param],parameters[param]['object']])
    prompt =  js['varKeys'][0]
    promptJs[prompt] = '#'+str(parametersSpec['prompt']['task'])+'\n'+parametersSpec['prompt']['structure']+'\n\t'
    for k in range(0,len(js['varKeys'])):
       prompt = js['varKeys'][k]
       if prompt not in promptJs:
            promptJs[prompt]= ''
       print(js['varKeys'][k])
       promptJs[prompt] = promptJs[prompt]+js[prompt]['delimiter']+'\n'+str(js[prompt]['varPrompt']+'\n')
    for k in range(0,len(js['varKeys'])):
        prompt = js['varKeys'][k]
        if js[prompt]['ogVar'] not in paramJs:
            paramJs[js[prompt]['ogVar']] = ''
        paramJs[js[prompt]['ogVar']] = str(paramJs[js[prompt]['ogVar']]) + str(promptJs[prompt])
    specializedSet['content'] =info[js['category']]['endpoints']['form']
    js['endPoint'] = info[js['category']]['endpoints'][js['spec']]
    js['response'] = info[js['category']]['endpoints']['response']
    if js['response'][1] in values:
        js['response'][1] = values[js['response'][1]]
    js['dumped'] = json.dumps(paramJs)

    return js
def pasteEm(xJs):


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#  CODE-TEXT-EDITOR
#  israel.dryer@gmail.com
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    VERSION = '0.1.079'
    VERSION_DATE = '2019-10-06'

    import PySimpleGUI as sg 
    from tkinter import font as tkfont
    from datetime import datetime
    import sys

    # `application_active` flag used when updating the window after the first read, and after a theme change
    # this is currently used as a work-around for the `finalize=True` bug, and can be
    # removed when that issue is fixed
    application_active = False 


    ##-----CREATE CUSTOM RE-DIRECT STDOUT OBJECT-------------##
    class RedirectText:
        def __init__(self, window):
            ''' constructor '''
            self.window = window
            self.saveout = sys.stdout

        def write(self, string):
            self.window['_OUT_'].Widget.insert("end", string)

        def flush(self):
            sys.stdout = self.saveout 
            sys.stdout.flush()
    ##-----SETUP DEFAULT USER SETTINGS-----------------------##
    save_user_settings = False
    # if flag is `False` the settings are saved in active session only with a `dict`
    # if flag is `True` the settings are saved in a local directory in a shelve file
    if save_user_settings:
        import shelve
        settings = shelve.open('app_settings')
    else:
        settings = {}
    # check to see if settings dict/shelf contains default values, create if not
    if len(settings.keys()) == 0:
        settings['theme'] = 'BluePurple'
        settings['themes'] = sg.list_of_look_and_feel_values()
        settings['font'] = ('Consolas', 12)
        settings['tabsize'] = 4
        settings['filename'] = None
        settings['body'] = ''
        settings['info'] = '> New File <'
        settings['out'] = ''
    # default theme or user saved theme
    sg.change_look_and_feel(settings['theme'])
    # string to output initial start settings
    outstring = "STARTUP SETTINGS:\n"+"-"*40+"\nTheme"+"."*10+" {}\nTab size"+"."*7+" {}\nFont"+"."*11+" {} {}\nOpen file"+"."*6+" {}\n\n"
    settings.update(out = outstring.format(settings['theme'], settings['tabsize'], settings['font'][0], settings['font'][1], settings['filename']))
    def close_settings():
        ''' Close the the shelve file upon exit '''
        settings.update(filename=None, body='', out='', info='> New File <')
        if save_user_settings:
            settings.close()
    ##----SETUP GUI WINDOW-----------------------------------##

    def main_window(settings):
        
        ''' Create the main window; also called when the application theme is changed '''
        elem_width= 80 # adjust default width
        menu_layout = [
            ['File',['New','Open','Save','Save As','---','Exit']],
            ['Edit',['Undo','---','Cut','Copy','Paste','Delete','---','Find...','Replace...','---','Select All','Date/Time']],
            ['Format',['Theme', settings['themes'],'Font','Tab Size','Show Settings']],
            ['Run',['Run Module']],
            ['Help',['View Help','---','About Me']]]

        col1 = sg.Column([[sg.Multiline(default_text=settings['body'], font=settings['font'], key='_BODY_', size=(elem_width,20))]])
        col2 = sg.Column([[sg.Multiline(default_text=settings['out'], font=settings['font'], key='_OUT_', autoscroll=True, size=(elem_width,8))]])         

        window_layout = [
            [sg.Menu(menu_layout)],
            [sg.Text(settings['info'], key='_INFO_', font=('Consolas',11), size=(elem_width,1))],
            [sg.Pane([col1, col2])]]

        window = sg.Window('Text-Code Editor', window_layout, resizable=True, margins=(0,0), return_keyboard_events=True)
       

        redir = RedirectText(window)
        sys.stdout = redir

        while True:
            application_active = True
            event, values = window.read()
         
            window['_BODY_'].update(value=xJs)
            close_settings()
            # adjust window when application is activated
            if not application_active:
                application_active = True
                set_tabsize(window)
            # listen for window events
            if event in (None, 'Exit'):
                close_settings()
                break
    main_window(settings)

def getCurrentTab(event,values):
    #allTabs,promptTabsGroup,str(specialization)+'_Tab',str(specialization)+"_fileUpload_tab",str(specialization)+"_"+str(varKey)+'_tab',
    js={}
    js['spec'] = 'chat' 
    if 'allTabs' in values:
        js['spec'] = values['allTabs'].split('_')[0]
    js['category'] = getCatFroSpec(js['spec'])
    js['varKeys'] = getKeys(info[js['category']]["specifications"][js['spec']]['parameters']['prompt']['vars'])
    for k in range(0,len(js['varKeys'])):
        varKey,varTab,varPrompt = js['varKeys'][k],str(js['spec'])+"_"+str(js['varKeys'][k])+'_tab',str(js['spec'])+"_"+str(js['varKeys'][k])
        if varPrompt in values:
            js[varKey] = info[js['category']]["specifications"][js['spec']]['parameters']['prompt']['vars'][varKey]
            js[varKey]['varPrompt']=values[varPrompt]
    return js         
def desktopTheme():
  import getPrompTabs
  from infoSheets import mid,categories,parameters,specifications,choi,descriptions,endpoints,paramNeeds,models,engines,cats,info
  start = True
  choices = {"completions": ["chat", "translate", "qanda", "parse"], "coding": ["editcode", "debugcode", "convertcode", "writecode"], "embeddings": ["text_search_doc", "similarityIt", "text_similarityIt", "text_search_queryIt", "text_embeddingIt", "text_insertIt", "text_editIt", "search_documentIt", "s", "instructIt", "code_editIt", "code_search_codeIt", "code_search_textIt"], "moderation": ["moderate"], "images": ["image_create", "image_edit", "image_variation"]}
  theme_dict = {'BACKGROUND': '#2B475D','TEXT': '#FFFFFF','INPUT': '#F2EFE8','TEXT_INPUT': '#000000','SCROLL': '#F2EFE8','BUTTON': ('#000000', '#C2D4D8'),'PROGRESS': ('#FFFFFF', '#C7D5E0'),'BORDER': 0,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}
  sg.theme_add_new('Dashboard', theme_dict)
  
    
  sg.theme('Dashboard')
  files = [[getDefMenu()]]
  top_banner,top,quFr,prQu =getBanner(),getTop(),getquerySection(),getPrevQuery()
  #querySection = [[sg.Text('Query Selection', font='Any 20')],mkDefCats(),[sg.Combo(specializedLs,key='catCombo',default_value=specializedLs[0]),sg.Button('Generate',key='Generate',enable_events=True, button_color=templateJs['BUTT_COLOR_Y_B'])]]
  previousQuery = [[sg.Text('previous query', font='Any 20')],txtInputDis('previous statememt','previous statememt',50,10),txtInputDis('previous Answer','previousQuery',50,10),]
  prQu = getFrameNow(previousQuery,'previousQuery')
  chatInput,outputSection = [[sg.Text('chatInput', font='Any 20')],getPrompTabs.getTabs(),[sg.Button('Compile', button_color=templateJs['BUTT_COLOR_Y_B'], bind_return_key=True),sg.Button('SEND', button_color=templateJs['BUTT_COLOR_Y_B'], bind_return_key=True),sg.Button('EXIT', button_color=templateJs['BUTT_COLOR_Y_G'])]],[[sg.Text('Script output', font='Any 20')],[sg.Output(size=(88, 20), font='Courier 10')]]
  js = {'top_banner':{'pad': (0,0), 'background_color': '#1B2838', 'expand_x': True, 'border_width': 0, 'grab': True},'top':{'size': None, 'pad': ((20,20), (20, 10)), 'expand_x': True, 'relief': sg.RELIEF_GROOVE, 'border_width': 3},'querySection':{'pad': (0, (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True},'chatInput':{'pad': ((20,20), (20, 10)), 'border_width': 0, 'expand_x': True, 'expand_y': True},'outputSection':{'pad': (0, (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True},'parameterSection':{'pad': ((10,20), (10, 0)), 'border_width': 0, 'expand_x': True, 'expand_y': True}}
  chatInput,outputSection = getFrameNow(chatInput,'chatInput'),getFrameNow(outputSection,'outputSection')
  layout =  [files,[top_banner],[[top],[sg.Frame('', [[quFr],[prQu],[outputSection],[chatInput]],pad=templateJs['BPAD_LEFT'], background_color=templateJs['BORDER_COLOR'], border_width=0, expand_x=True, expand_y=True),sg.Column(specializedSet['jsList'], pad=templateJs['BPAD_RIGHT'],  expand_x=True, expand_y=True, grab=True),],[sg.Sizegrip(background_color=templateJs['BORDER_COLOR'])]]]
  window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(5,5), element_padding=(5,5), background_color=templateJs['BORDER_COLOR'], keep_on_top=False, no_titlebar=False, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT)
  while True:
        try:      
            event, values = window.read()
          
            valKeys = fun.getKeys(values)[1:]
            event = str(event)
            #values,numJs = stripNumJS(values)
            if start == True:
                fun.pen(json.dumps({'defaul':values}),'valuesJs.json')
                start = False
            
            if '_default_' in str(event):
                spl = event.split('_default_')
                defa = mkType([spl[1],parameters[spl[0]]['object']])
                if values[event] == True:
                    window[spl[0]].update(value=mkType([spl[1],parameters[spl[0]]['object']]))
                if mkType([spl[1],parameters[spl[0]]['object']]) == defa:
                    window[event].update(value=True)
            elif event in parameters['all']:
                defa,obj,eVal,defaultKey = parameters[event]['default'],parameters[event]['object'],values[event],findStrInLs(valKeys,event+'_default_')
                for k in range(0,len(defaultKey)):
                    defa,eVal=mkType([defa,obj]),mkType([eVal,obj])
                    if eVal == defa:
                        window[defaultKey[k]].update(value=True)
                    elif eVal != defa:
                        window[defaultKey[k]].update(value=False)
            elif '_info' in event:
                req,na = 'optional',event.split('_info')[0]
                if na in getParamNeeds(category,specialization)['required']:
                    req = 'required'
                sg.popup_scrolled('name:'+str(na)+',  | default:'+str(req)+' | type:'+str(parameters[na]['object'])+'\ndescription: ',parameters[na]['description'],keep_on_top=False)
            elif 'upload_' in event:
                if specialization+'_browser' in values:
                    path = values[specialization+'_browser']
                    if path != '':
                        if event == 'upload_Image':
                            window['preview'].update(path)
                        if event == 'upload_File':
                            text = fun.reader(path)
                            window['preview'].update(value=text)
                            uploads = findStrInLs(valKeys,event+'_upload')
                            for k in range(0,len(uploads)):
                                if values[uploads[k].split('_upload')[0]] == True:
                                    window[fun.getKeys(infoS.getAllThings(category,specialization)['prompt']['parse']['vars'])[0]].update(value=text)
                                    len(text)
                                    window.getScreen()
                            if len(uploads) == 0:
                                window[fun.getKeys(infoS.getAllThings(category,specialization)['prompt']['parse']['vars'])[0]].update(value=text)
            elif 'convert_image' in event:
                    import demoImgh64
                    try:
                        demoImgh64.main()
                    except:
                        print('that didnt go well')
            elif 'Compile' in event:
                
                specializedSet['pastedInWindow']=completePrompt(event,values)
                pasteEm(specializedSet['pastedInWindow'])
         
                print('and now its gone')
            elif 'SEND' in event:
                print('doingit')
                reqPost(completePrompt(event,values))
                #command_history.apchatInput,outputSection = [[sg.pend(query)]]
                #history_offset = len(command_history)-1
                #window['query'].update('')
                #window['history'].update('\n'.join(command_history[-3:]))
            elif event in (sg.WIN_CLOSED, 'EXIT'):
                break
            elif 'Up' in event and len(command_history):
                command = command_history[history_offset]
                # decrement is not zero
                history_offset -= 1 * (history_offset > 0)
                window['query'].update(command)
            elif 'Down' in event and len(command_history):
                history_offset += 1 * (history_offset < len(command_history)-1)
                command = command_history[history_offset]
                window['query'].update(command)
            elif 'Escape' in event:
                window['query'].update('')
            elif event == sg.WIN_CLOSED or event == 'Exit':
                break
                window.close()
            elif 'default_' in event:
                na,defa = event.split('default_')[0],event.split('default_')[1]
                if values[event] == True:
                    defa = str(defa).replace("'",'').replace('"','')
                    if str(defa) in ['True','False','None']:
                        window[na].update(value=bool(defa))
                    elif '.' in str(defa):
                        window[na].update(value=float(defa))
                    elif fun.isNum(defa):
                        window[na].update(value=int(defa))
                    else:
                        window[na].update(value=str(defa))   
            elif 'disable' in event:
                na = event.split('disable')[0]
                if values[na] == True:
                    keys = getKeys(values)[1:]
                    for i in range(0,len(keys)):
                        if fun.isNum(keys) == False:
                            if na+'default_' in keys[i]:
                                defa = keys[i].split(na+'default_')[-1]
                                window[na].update(value=defa)
            elif event == 'Edit Me':
                  sg.execute_editor(__file__)
            elif event == 'Version':
                  sg.popup_scrolled(sg.get_versions(), keep_on_top=True)
            elif event == 'File Location':
                  sg.popup_scrolled('This Python file is:', __file__)
            elif 'category_' in event:
                js = getAllThings()
                ls = categoriesJs[event.split('category_')[1]]
                changeGlob('category',event.split('category_')[1])
                changeGlob('specializedLs',categoriesJs[category])
                changeGlob('specialization',specializedLs[0])
                varKeys = getKeys(js['prompt']['parse']['vars'])
                specializedTabs(window)
                window.refresh()
                window['categoryDisplay'].update(value=js['category']['names'])
                window['categoryDescription'].update(value=js['categoryDefinition'])
                window["catCombo"].update(values = ls)
                window["catCombo"].update(value=ls[0])
                window['structure'].update(value=js['structure']['parse'])
                window['specializationDisplay'].update(value=js['specialization']['names'])
                window['specializationDescription'].update(value=js['specializationDeffinition'])
                window.refresh()
            elif event == 'Generate':
                specializedSet['jsList'] = [[sg.Text('Parameters', font='Any 20')],[txtBox('def  '),txtBox('dis  '),txtBox('   inf  ')]]
                getParamDrop([category,changeGlob('specialization',values['catCombo'])])
                window.refresh()
            #allTabs,promptTabsGroup,str(specialization)+'_Tab',str(specialization)+"_fileUpload_tab",str(specialization)+"_"+str(varKey)+'_tab',
            
                
                activeTab = window['allTabs'].Get()
                print(activeTab)
                
                
                lsN = []
                spec = activeTab.split('_')[0]
                for k in range(0,len(categories)):
                    categoryLs = categories[categories[k]]
                    if spec in categoryLs:
                        cat = categories[k]
                    for i in range(0,len(categoryLs)):
                        lsN.append(categoryLs[i])
                
                varKey = activeTab2.split('_')
                varKeys = getKeys(infoS.getAllThings(cat,spec)['prompt']['parse']['vars']['prompt'])
                keys = fun.getKeys(numJs)
                for k in range(0,len(keys)):
                    if varKeys[k] == varKey:
                                     
                        print(varKey)
                    if activeTab == 'tab2':
                        print('success2')
        except:
            print('wooohooo')
  return values
def startIt():
        #chatInput = [[sg.Text('chatInput', font='Any 20')],txtInput('chat Input',100,10),[sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
    params = parameters['all']
    for k in range(0,len(params)):
        specializedSet['opt'] = True
        try:
            getParamMenu(params[k],getAllInfo('parameters')[params[k]])
        except:
            specializedSet['notFound'].append(params[k])
    desktopTheme()

global category,specializations,categories,specialization,catKeys,specializedSet,catLs,categoriesJs,specializations,info,tabIndex,parameters, pastedinwindow
import infoSheets as infoS
from infoSheets import mid,categories,parameters,specifications,choi,descriptions,endpoints,paramNeeds,models,engines,cats,info
info ={"completions":{"categories":["chat","translate","qanda","parse"],
                      "endpoints": {"chat": "https://api.openai.com/v1/completions", "chat": "https://api.openai.com/v1/completions", "translate": "https://api.openai.com/v1/completions", "qanda": "https://api.openai.com/v1/completions","parse": "https://api.openai.com/v1/completions", 'form':'application/json',"response": ["choices", "n", "text"]},
                      "choices":{"model":{'default': 'text-davinci-003', 'list': ['text-ada-001', 'text-davinci-003', 'text-curie-001', 'text-babbage-001']}},
                      "specifications":{
                        'chat':{'type': 'completions','refference':['completions','create'],"parameters":{'required':['model','prompt'],'optional':['user','stream','n','suffix','max_tokens','logit_bias','temperature','best_of','top_p','frequency_penalty','presence_penalty','stop','echo'],'prompt':{"task":"chat","structure": '','vars': {'prompt':{"input":"what would you like to say to the bot?","delimiter":''}}}}
                                },
                        "chat": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "chat", "structure": "", "vars": {"prompt": {"input": "what would you like to say to the bot?", "type": "str","ogVar":"prompt", "delimiter": ""}}}}
                                 },
                        "translate": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "task: translate text", "structure": "languages to translate to:[languages];translate the following text:[text]", "vars": {"languages": {"input": "specify the target languages", "type": "list","ogVar":"prompt", "delimiter": "languages to translate to:\n"}, "text": {"input": "input the text you would like to have translated", "type": "text","ogVar":"prompt", "delimiter": "translate the following text:\n"}}}}
                                      },
                        "qanda": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "task: question and answer", "structure": "[question]- input a question,question mark will auto add, [answer] - proposed answer to a question", "vars": {"question": {"input": "pose a question to have answered", "type": "str","ogVar":"prompt","delimiter": "Q:"}, "answer": {"input": "pose answer to a proposed question", "type": "str","ogVar":"prompt", "delimiter": "A:"}}}}
                                  },
                        "parse": {"type": "completions", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "task: parse text,", "structure": " a [summary] of the [data] will be given in order to parse specific [subjects]:", "vars": {"summary": {"input": "summarize the text you would like to parse", "type": "text","ogVar":"prompt", "delimiter": "summary of data:\n"}, "subjects": {"input": "specific subjects you want to have parsed", "type": "list","ogVar":"prompt", "delimiter": "subjects:\n"}, "data": {"input": "text you would like to have parsed", "type": "text","ogVar":"prompt", "delimiter": "data to parse:\n"}}}}
                                  }
                        }
                        
                      },
       "coding": {"categories":["writecode","editcode","debugcode","convertcode"],
                  "endpoints": {"editcode": "https://api.openai.com/v1/completions", "debugcode": "https://api.openai.com/v1/completions", "convertcode": "https://api.openai.com/v1/completions", "writecode": "https://api.openai.com/v1/completions", "form":"application/json", "response": ["choices", "n", "text"]},
                  "choices": {"language": {"default": "python", "list": ["Python", "Java", "C++", "JavaScript", "Go", "Julia", "R", "MATLAB", "Swift", "Prolog", "Lisp", "Haskell", "Erlang", "Scala", "Clojure", "F#", "OCaml", "Kotlin", "Dart"]},
                              "model": {"default": "code-davinci-002", "list": ["code-cushman-001", "text-davinci-003", "code-davinci-002"]}},
                  "specifications": {
                    "writecode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "write code in [language] based off of specific [instruction]:", "structure": "[prompt]-describe the code; [language] - specify the target language", "vars": {"instruction": {"input": "describe what you are looking for, be specific", "type": "str","ogVar":"prompt", "delimiter": "instructuions:\n"}, "language": {"input": "which language would you like the code to be written in?", "type": "choice","ogVar":"prompt", "delimiter": "language:\n,"}}}}},
                    "editcode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "edit code", "structure": "edit [code] based off of specific [instructions]", "vars": {"instruction": {"input": "provide specific instructions on what you are looking to have edited about this code:", "type": "str","ogVar":"prompt", "delimiter": "instructions:\n"}, "code": {"input": "enter the code you would like to have edited:", "type": "str","ogVar":"prompt", "delimiter": "code:\n"}}}}},
                    "debugcode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "debug the code:", "structure": "debug the following code:\n", "vars": {"code": {"input": "the code you would like to have debugged", "type": "str","ogVar":"prompt", "delimiter": ""}}}}},
                    "convertcode": {"type": "coding", "refference": ["completions", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "convert code to another language:", "structure": "convert the following [code] to [language]", "vars": {"language": {"input": "the language you would like the code converted to:", "type": "str","ogVar":"prompt", "delimiter": "language:\n"}, "code": {"input": "the code you would like to have converted", "type": "str","ogVar":"prompt", "delimiter": "code:\n"}}}}}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       },
       "images": {"categories":["image_variation","image_create","image_edit"],
                  "endpoints": {"image_create": "https://api.openai.com/v1/images/generations", "image_variation": "https://api.openai.com/v1/images/variations", "image_edit": "https://api.openai.com/v1/images/edits", "form":"multipart/form-data","response": ["data", "n", "response_format"]}, "choices": {"response_format": {"default": "url", "list": ["url", "b64_json"]}, "size": {"default": "1024x1024", "list": ["256x256", "512x512", "1024x1024"]}},
                  "specifications": {
                    "image_variation": {"type": "images", "refference": ["image", "create", "image_variation"], "parameters": {"required": ["image"], "optional": ["prompt", "size", "n", "response_format", "user", "n", "suffix", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop", "echo"], "prompt": {"task": "image variation", "structure": "create a variation of the [image] based off of [instructions] if given:\n", "vars": {"instructions": {"input": "describe what you would like to have done with the image(s):", "type": "str","ogVar":"prompt", "delimiter": "instructions:\n"}}}}},
                    "image_create": {"type": "images", "refference": ["image", "create", "image_create"], "parameters": {"required": ["prompt"], "optional": ["size", "n", "response_format", "user", "suffix", "logit_bias"], "prompt": {"task": "image creation", "structure": "create an image based on the following [instructions]:\n", "vars": {"instructions": {"input": "describe the image you would like to create:", "type": "str","ogVar":"prompt", "delimiter": "instructions:"}}}}},
                    "image_edit": {"type": "images", "refference": ["image", "create", "image_edit"], "parameters": {"required": ["image", "prompt"], "optional": ["mask", "size", "n", "response_format", "user", "suffix", "max_tokens", "logit_bias"], "prompt": {"task": "image creation", "structure": "[image]-main image; [mask] secondary image;[prompt]- instructions on how it should be edited ", "vars": {"instructions": {"input": "provide instructions describing what you would like to have done with the image(s):", "type": "str","ogVar":"prompt", "delimiter": "instructions:"}}}}}}
                  },
       "edit": {"categories":["edits"],
                "endpoints": {"edit": "https://api.openai.com/v1/embeddings",  "form:":"application/json", "response": ["data", "n", "embedding"]}, "choices": {"model": {"default": "text-ada-001", "list": ["text-ada-001", "text-davinci-003", "text-curie-001", "text-babbage-001"]}},
                "specifications": {
                  "edits": {"type": "edits", "refference": ["edits", "create"], "parameters": {"required": ["model", "prompt"], "optional": ["user", "stream", "n", "max_tokens", "logit_bias", "temperature", "best_of", "top_p", "frequency_penalty", "presence_penalty", "stop"], "prompt": {"task": "edit text", "structure": "[image]-main image; [mask] secondary image;[prompt]- input how you would like to have it edited", "vars": {"instructions": {"input": "provide instructions describing what you would like to have edited:", "type": "str","ogVar":"prompt", "delimiter": "instructions:"}}}}
                            }
                  }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             },
       "moderation": {"categories":["moderate"],
                      "endpoints": {"moderate": "https://api.openai.com/v1/moderations", "form":"application/json", "response": ["results", "n", "text"]}, "choices": {"model": {"default": "None", "list": ["text-moderation-004", "davinci"]}},
                      "specifications": {
                        "moderate": {"type": "moderation", "refference": ["moderation"], "parameters": {"required": ["input"], "optional": ["model"], "prompt": {"task": "moderation", "structure": "text to moderate:\n", "vars": {"input": {"input": "provide the text you would like to have moderated", "type": "text","ogVar":"prompt", "delimiter": "moderate the following"}}}}}}
                      }
       }

specializedSet = {'pastedInWindow':'','notFound':[],'fileUps':[],'inputTabKeys':{'types':[],'inputLs':[],'index':1,'names':[],'descriptions':[]},'jsList':[[sg.Text('Parameters', font='Any 20')],[txtBox('def  ',None,'Any 20',None,True,False),txtBox('dis  ',None,'Any 20',None,True,False),txtBox('   inf  ',None,'Any 20',None,True,False)]],'prevKeys':[],'userMgs':'','resp':'','content':'application/json'}
changeGlob('templateJs',{'BPAD_BANNER':(0,0),'BORDER_COLOR':'#C7D5E0','DARK_HEADER_COLOR':'#1B2838','BPAD_TOP':((20,20), (20, 10)),'BPAD_LEFT':((20,10), (0, 0)),'BPAD_LEFT_INSIDE':(0, (10, 0)),'BPAD_RIGHT':((10,20), (10, 0)),'BUTT_COLOR_Y_G':(sg.YELLOWS[0], sg.GREENS[0]),'BUTT_COLOR_Y_B':(sg.YELLOWS[0], sg.BLUES[0])})

categoriesJs = categories
catKeys = fun.getKeys(categoriesJs)
category = catKeys[0]
specializedLs = categoriesJs[category]
specialization = specializedLs[0]

pastedinwindow = ''


