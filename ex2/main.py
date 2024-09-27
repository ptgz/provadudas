def encurtar_urls(input_arquivo, output_arquivo): # exemplo de uso: encurtar_urls('ex2/urls.json','ex2/newurls.json')
    import json
    newFile = []
    with open(input_arquivo,'r',encoding='utf-8') as file:
        fr = file.read()
        urls = json.loads(fr)
    
    for url in urls:
        urlConsonants = []
        url['url'] = url['url'][12:]
        for l in url['url']:
            if l.lower() in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
                if len(urlConsonants) < 3:
                    urlConsonants.append(l)
                else:
                    break
        
        consonants = "".join(urlConsonants)
        newFile.append({"id" : url['id'], "url" : f"https://short.ly/{consonants}{url['id']}"})
        pass

    with open(output_arquivo,'w',encoding='UTF-8') as file:
        json.dump(newFile,file,indent=4)
        pass

encurtar_urls('ex2/urls.json','ex2/newurls.json')